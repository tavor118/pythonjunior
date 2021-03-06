# Generated by Django 2.0.9 on 2019-01-10 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0006_auto_20190103_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='maincategory',
            name='number_of_cards',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='number_of_cards',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tag',
            name='number_of_cards',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
