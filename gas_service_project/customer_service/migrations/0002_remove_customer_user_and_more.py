# Generated by Django 4.2.4 on 2023-08-13 06:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='resolution_timestamp',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='service_type',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='submission_timestamp',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(default='Default Address', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.TextField(default='Default first name', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.TextField(default='Default ast name', null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='attached_file',
            field=models.FileField(blank=True, null=True, upload_to='service_request_files/'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='request_type',
            field=models.CharField(default='Default Request Type', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='resolved_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='submitted_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]