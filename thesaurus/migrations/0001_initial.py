# Generated by Django 2.0.9 on 2018-12-30 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(allow_unicode=True, editable=False, unique=True)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('rating', models.PositiveSmallIntegerField(default=1)),
                ('reviews', models.PositiveSmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-rating', 'title'),
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('priority', models.PositiveSmallIntegerField(default=1)),
                ('icon', models.ImageField(default='category_icons/none/no-img.jpg', upload_to='category_icons/')),
            ],
            options={
                'ordering': ('-priority',),
            },
        ),
        migrations.CreateModel(
            name='SavedPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('original_url', models.URLField()),
                ('content', models.TextField()),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='thesaurus.Card')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('priority', models.PositiveSmallIntegerField(default=1)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='thesaurus.MainCategory')),
            ],
            options={
                'ordering': ('-priority',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('priority', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='card',
            name='main_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='thesaurus.MainCategory'),
        ),
        migrations.AddField(
            model_name='card',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='thesaurus.SubCategory'),
        ),
        migrations.AddField(
            model_name='card',
            name='tags',
            field=models.ManyToManyField(to='thesaurus.Tag'),
        ),
    ]
