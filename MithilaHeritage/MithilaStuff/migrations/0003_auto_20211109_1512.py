# Generated by Django 3.2.8 on 2021-11-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MithilaStuff', '0002_categories_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='desc',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(default='MithilaStuff/img/image.jpg', upload_to='MithilaStuff/img'),
        ),
    ]
