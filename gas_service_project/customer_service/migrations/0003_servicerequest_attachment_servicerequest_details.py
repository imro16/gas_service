# Generated by Django 4.2.4 on 2023-08-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0002_remove_customer_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='details',
            field=models.TextField(default='Default Request Type', max_length=100, null=True),
        ),
    ]
