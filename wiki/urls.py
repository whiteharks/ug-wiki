from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('base.css',views.base, name="base_css"),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]



