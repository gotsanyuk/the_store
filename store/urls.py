from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

app_name = 'store'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('category/', category_show, name='category_show'),
    path('category/<slug:slug>/', category_show, name='category_filter'),
    path('detail/<slug:slug>/', product_detail, name='product_detail'),
]
