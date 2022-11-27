from django.urls import path
from articles.views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    )

urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view(), name= 'article_detail' ),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name= 'article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
]