from django.urls import path, include
from . import views
from cards import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index, name = 'index'),
    path('accounts/signUp/', views.signUp, name='signUp'),
    path('search/', views.search_subject_results, name = 'search_subject_results'),
  
   

]