# Generated by Django 4.1 on 2022-08-10 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coureses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coures',
            name='contant',
            field=models.TextField(max_length=1000),
        ),
    ]
