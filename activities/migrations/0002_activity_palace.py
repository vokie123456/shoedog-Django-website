# Generated by Django 2.0 on 2018-05-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='palace',
            field=models.CharField(default='Not Know', max_length=100),
        ),
    ]
