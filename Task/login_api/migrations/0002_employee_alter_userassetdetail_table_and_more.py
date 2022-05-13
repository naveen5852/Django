# Generated by Django 4.0.4 on 2022-05-11 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('emp_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('d_o_b', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('project', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.AlterModelTable(
            name='userassetdetail',
            table='asset_detail',
        ),
        migrations.AlterModelTable(
            name='userfamilydetail',
            table='family_detail',
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
        migrations.AlterField(
            model_name='userassetdetail',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_api.employee'),
        ),
        migrations.AlterField(
            model_name='userfamilydetail',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_api.employee'),
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
