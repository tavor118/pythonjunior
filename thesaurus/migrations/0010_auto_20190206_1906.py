# Generated by Django 2.0.9 on 2019-02-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0009_auto_20190205_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='slug',
            field=models.SlugField(allow_unicode=True, editable=False, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
