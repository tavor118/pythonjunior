from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class MainCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    priority = models.PositiveSmallIntegerField(default=1)
    icon = models.FileField(upload_to='category_icons/', default='category_icons/none/no-img.jpg')
    number_of_cards = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["priority"]

    def get_cards_count(self):
        return Card.objects.filter(main_category=self).count()


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    priority = models.PositiveSmallIntegerField(default=1)
    main_category = models.ForeignKey(MainCategory, related_name='sub_categories', on_delete=models.CASCADE)
    number_of_cards = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.main_category, self.name)

    class Meta:
        ordering = ["main_category", "-priority"]

    def get_cards_count(self):
        return Card.objects.filter(sub_category=self).count()


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    priority = models.PositiveSmallIntegerField(default=1)
    number_of_cards = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    def get_cards_count(self):
        return Card.objects.filter(card__tag=self).count()


class Card(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, allow_unicode=True, unique=True, editable=False)
    description = models.TextField(blank=True)
    note = models.CharField(blank=True, max_length=255)
    url = models.URLField()
    img = models.ImageField(upload_to='images/card_img/', default='images/card_img/default.jpg')
    rating = models.PositiveSmallIntegerField(default=1)
    reviews = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    main_category = models.ForeignKey(MainCategory, related_name='cards', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, related_name='cards', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.sub_category, self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        self.main_category.number_of_cards += 1
        self.main_category.save()
        self.sub_category.number_of_cards += 1
        self.sub_category.save()
        for tag in self.tags.all():
            tag.number_of_cards += 1
            tag.save()


    def get_absolute_url(self):
        return reverse(
            "thesaurus:card",
            kwargs={
                "category": self.main_category,
                "sub_category": self.sub_category,
                "slug": self.slug,
            })

    class Meta:
        ordering = ['main_category', 'sub_category', '-rating', 'title']


class SavedPost(models.Model):
    title = models.CharField(max_length=100)
    original_url = models.URLField()
    content = models.TextField()
    card = models.OneToOneField(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
