from django.urls import path

from . import views
from .views import IndexView

app_name = 'hotel'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', views.search, name='search'),
    path('reserve/', views.reserve, name='reserve'),
    path('confirm/', views.confirm, name='confirm'),
    ]
