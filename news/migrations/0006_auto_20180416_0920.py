# Generated by Django 2.0 on 2018-04-16 09:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180414_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anews',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
