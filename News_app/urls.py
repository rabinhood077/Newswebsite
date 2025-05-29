from django.contrib import admin
from django.urls import path,include
from News_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Post_list,name="post-list"),
    path('post-details/<int:pk>/',views.Post_list,name="post-details"),
    
]