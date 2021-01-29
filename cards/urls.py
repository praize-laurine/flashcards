from django.urls import path, include
from . import views
from cards import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index, name = 'index'),
    path('accounts/signUp/', views.signUp, name='signUp'),
    # path('userProfile/', views.userProfile,name = 'userProfile'),
    # path('update_profile/', user_views.update_profile,name = 'update_profile'),
    path('search/', views.search_subject_results, name = 'search_subject_results'),
    path('post_subject/', views.post_subject,name ='post_subject'),

]