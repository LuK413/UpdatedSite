# Generated by Django 3.0.7 on 2020-06-09 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20200608_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.FilePathField(path='/Users/kailu/Desktop/projects/UpdatedSite/project/static/img'),
        ),
    ]
