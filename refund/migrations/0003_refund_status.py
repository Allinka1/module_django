# Generated by Django 3.2.3 on 2021-06-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refund', '0002_alter_refund_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='status',
            field=models.IntegerField(choices=[[1, 'Pending'], [2, 'Confirmed'], [3, 'Rejected']], default=1),
        ),
    ]
