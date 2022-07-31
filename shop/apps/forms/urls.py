from django.urls import path
import apps.forms.views as views

urlpatterns = [
    path('',views.form1),
    path('form2/',views.form2),
    path('form3/',views.form3),
    path('form4/',views.form4),




]