# Generated by Django 3.1.2 on 2020-10-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUserModel', '0003_auto_20201006_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
