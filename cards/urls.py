from django.urls import path, include
from .views import FlashcardUpdateView,FlashcardDeleteView,FlashcardListView
from cards import views as user_views
from django.conf.urls.static import static
from django.conf import settings
from . import views 


urlpatterns=[
    path('',views.index,name = 'index'),
    path('accounts/signUp/', views.signUp, name='signUp'),
    path('userProfile/', views.userProfile,name = 'userProfile'),
    path('update_profile/', user_views.update_profile,name = 'update_profile'),
    path('search/', views.search_subject_results, name = 'search_subject_results'),
    path('post_subject/', views.post_subject,name ='post_subject'),
    path('post/<int:pk>/update/',FlashcardUpdateView.as_view(), name="updateForm"),
    path('post/<int:pk>/delete/',FlashcardDeleteView.as_view(), name="deleteForm"),


]