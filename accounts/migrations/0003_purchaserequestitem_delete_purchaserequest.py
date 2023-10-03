# Generated by Django 4.1.11 on 2023-10-02 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_purchaserequest_delete_purchaserequestitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseRequestItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255)),
                ('purpose', models.TextField()),
                ('item_name', models.CharField(max_length=100)),
                ('item_description', models.TextField()),
                ('item_unit', models.CharField(max_length=50)),
                ('item_quantity', models.IntegerField()),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='PurchaseRequest',
        ),
    ]
