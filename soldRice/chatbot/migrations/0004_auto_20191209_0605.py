# Generated by Django 2.2.7 on 2019-12-09 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_customer_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]
