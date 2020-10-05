from django.urls import path
from .views import ArticlesView


urlpatterns = [
    path('', ArticlesView.as_view(), name='articles')
]
