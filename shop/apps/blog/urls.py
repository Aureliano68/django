from django.urls import path
import apps.blog.views as views

urlpatterns = [
    path('',views.blog1),
    path('authors/',views.author1),
    path('author',views.author2),



]




