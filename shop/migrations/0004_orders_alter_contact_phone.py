# Generated by Django 4.1.1 on 2022-09-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=0, max_length=70),
        ),
    ]
