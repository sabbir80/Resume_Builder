# Generated by Django 3.1.7 on 2021-03-16 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_auto_20210314_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_history',
            name='personal_info_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.personal_info'),
        ),
    ]
