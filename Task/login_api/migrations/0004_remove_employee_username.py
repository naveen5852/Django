# Generated by Django 4.0.4 on 2022-05-13 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_api', '0003_remove_employee_email_remove_employee_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='username',
        ),
    ]