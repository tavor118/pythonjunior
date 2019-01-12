from django.urls import path

from . import views

app_name = 'thesaurus'

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("tag/<str:tag>/", views.TagCardListView.as_view(), name='tag_cards'),
    path("<str:category>/", views.SubCategoryListView.as_view(), name='sub_categories'),
    path("<str:category>/<str:sub_category>/", views.CardListView.as_view(), name='cards'),
    path("<str:category>/<str:sub_category>/<slug:slug>/", views.CardDetail.as_view(), name='card'),
]
