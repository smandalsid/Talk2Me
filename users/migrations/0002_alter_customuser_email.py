# Generated by Django 3.2.7 on 2021-09-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
