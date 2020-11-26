from django.urls import path
from . import views


urlpatterns = [
    path('', views.data_schemas, name='data_schemas'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add/', views.SchemaCreate.as_view(), name='add'),
]