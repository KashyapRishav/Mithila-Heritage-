# Generated by Django 3.2.8 on 2021-11-15 07:28

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('MithilaStuff', '0007_alter_categories_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='desc',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
