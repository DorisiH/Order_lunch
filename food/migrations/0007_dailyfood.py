# Generated by Django 3.2.6 on 2021-08-18 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_delete_dailymenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.foodmenu')),
            ],
        ),
    ]