from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('profile/',views.profile,name="profile"),
    path('create_model/',views.create_model,name="create_model"),
    path('delete_model/<int:id>',views.delete_model,name="delete_model"),
    path('update/<int:id>',views.update,name="update"),
    
]

