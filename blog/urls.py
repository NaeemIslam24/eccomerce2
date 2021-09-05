from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog, name='blog'),
    path('detail_blog/<int:id>/<slug:sl>', views.detail_blog, name='detail_blog'),
    
]
