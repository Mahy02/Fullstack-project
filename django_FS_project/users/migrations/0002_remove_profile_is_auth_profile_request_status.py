# Generated by Django 4.1.4 on 2023-01-02 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_auth',
        ),
        migrations.AddField(
            model_name='profile',
            name='request_status',
            field=models.CharField(choices=[('requested', 'requested'), ('approved', 'approved'), ('denied', 'denied'), ('none', 'none')], default='none', max_length=10),
        ),
    ]
