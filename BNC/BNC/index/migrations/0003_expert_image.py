# Generated by Django 3.0.2 on 2020-05-31 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200531_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='image',
            field=models.ImageField(default=0, upload_to='static\\images'),
            preserve_default=False,
        ),
    ]
