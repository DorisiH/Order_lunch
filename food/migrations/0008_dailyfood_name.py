# Generated by Django 3.2.6 on 2021-08-18 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_dailyfood'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyfood',
            name='name',
            field=models.CharField(default='deff', max_length=100),
            preserve_default=False,
        ),
    ]
