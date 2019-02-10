from django.shortcuts import get_object_or_404
from django.views import generic
from . import models


# Create your views here.
class HomePageView(generic.TemplateView):

    template_name = "thesaurus/thesaurus_home.html"


class SubCategoryListView(generic.ListView):
    model = models.SubCategory
    context_object_name = 'sub_categories'
    template_name = 'thesaurus/sub_categories.html'

    def get_context_data(self, **kwargs):
        kwargs['main_category'] = self.main_category
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.main_category = get_object_or_404(models.MainCategory, name=self.kwargs.get('category'))
        queryset = self.main_category.sub_categories.order_by('-priority')
        return queryset


class CardListView(generic.ListView):
    model = models.Card
    context_object_name = 'cards'
    template_name = 'thesaurus/sub_category_cards.html'

    def get_context_data(self, **kwargs):
        kwargs['sub_category'] = self.sub_category
        kwargs['main_category'] = self.sub_category.main_category
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.sub_category = get_object_or_404(
            models.SubCategory,
            main_category__name=self.kwargs.get('category'),
            name=self.kwargs.get('sub_category')
            )
        queryset = self.sub_category.cards.order_by('-rating', 'title')
        return queryset


class TagCardListView(generic.ListView):
    model = models.Card
    context_object_name = 'cards'
    template_name = 'thesaurus/tag_cards.html'

    def get_context_data(self, **kwargs):
        kwargs['tag'] = self.kwargs.get('tag')
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.tags = get_object_or_404(
            models.Tag,
            name=self.kwargs.get('tag')
            )
        queryset = self.tags.cards.order_by('-rating', 'title')
        return queryset


class CardDetail(generic.DetailView):
    model = models.Card
    context_object_name = 'card'

    def get_context_data(self, **kwargs):
        kwargs['card_details'] = True
        kwargs['sub_category'] = self.object.sub_category
        kwargs['main_category'] = self.object.main_category
        return super().get_context_data(**kwargs)
