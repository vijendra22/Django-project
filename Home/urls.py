from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_to_all, name='home_to_all'),
    path('<int:page_num>/', views.in_page, name='in_page'),

]
