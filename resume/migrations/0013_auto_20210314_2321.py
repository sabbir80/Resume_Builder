# Generated by Django 3.1.7 on 2021-03-14 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_auto_20210314_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='user_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.user'),
        ),
    ]
