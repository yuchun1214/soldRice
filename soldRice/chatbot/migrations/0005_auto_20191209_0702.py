# Generated by Django 2.2.7 on 2019-12-09 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_auto_20191209_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='order',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='user_modified',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
