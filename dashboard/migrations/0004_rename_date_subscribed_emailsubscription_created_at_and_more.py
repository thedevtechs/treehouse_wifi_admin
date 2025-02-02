# Generated by Django 4.1 on 2024-08-04 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailsubscription',
            old_name='date_subscribed',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='emailsubscription',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='emailsubscription',
            name='last_name',
        ),
        migrations.AddField(
            model_name='emailsubscription',
            name='join_mailing_list',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterModelTable(
            name='emailsubscription',
            table='users',
        ),
    ]
