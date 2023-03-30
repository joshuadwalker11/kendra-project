from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.index, name='index'),
    path('', views.RegFormView.as_view(), name='reg_view'),
    path('reg_complete/', views.reg_complete, name='reg_complete'),
]
