# Generated by Django 3.2.9 on 2021-11-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='{{ user.first_name }}', upload_to='images/'),
        ),
    ]
