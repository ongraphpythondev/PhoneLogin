# Generated by Django 2.2.5 on 2019-09-19 07:07

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('verify_app', '0004_auto_20190919_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=31, unique=True),
        ),
    ]
