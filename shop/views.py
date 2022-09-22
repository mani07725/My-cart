import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from math import ceil
# Create your views here.
def index(request):
    allprods=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides=0
        if(n%4!=0):
            nslides=n//4+1
        else:
            nslides=n//4
        allprods.append([prod,range(1,nslides),nslides])
    params={"allprods":allprods}
    return render(request, 'shop/index.html',params)
def about(request):
    return render(request, 'shop/about.html')

def checkout(request):
    if request.method == 'POST':
        print(request)
        items_json= request.POST.get('itemJson', '')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zipcode','')
        order= Order(items_json=  items_json,name=name,email=email,phone=phone,address=address,city=city,state=state,zipcode=zipcode)
        order.save()
        update=Order_update(order_id=order.order_id,update_description="your order has been placed sucessfully")
        update.save()
        context={
        'product':Product.objects.all
            };
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id, 'product':Product.objects.all()})
    return render(request, 'shop/checkout.html')
def contact(request):
    if request.method == 'POST':
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank=True
        return render(request, 'shop/contact.html',{'thank':thank})
    return render(request, 'shop/contact.html')
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = Order_update.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_description, 'time': item.timestemp})
                    Response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(Response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')
def search(request):
    return HttpResponse("search")
def productview(request,myid):
    # we are ganna fetch the product using its id since we haven't defined any primary key in the models.py file
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/prodview.html',{'product': product[0]})

def productlist(request):
    # this Product.object.all() is used to retrieve all the objects in the data base
    context={
        'product':Product.objects.all
    }
    return render(request, 'shop/product.html', context)