# Generated by Django 3.2.6 on 2021-08-25 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_dailyfood_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='fatura',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
