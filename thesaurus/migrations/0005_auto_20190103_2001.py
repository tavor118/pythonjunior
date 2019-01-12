# Generated by Django 2.0.9 on 2019-01-03 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesaurus', '0004_card_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['main_category', 'sub_category', '-rating', 'title']},
        ),
        migrations.AlterModelOptions(
            name='maincategory',
            options={'ordering': ['priority']},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['-priority']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='card',
            name='notes',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
