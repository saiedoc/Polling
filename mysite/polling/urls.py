from django.urls import path
from . import views

urlpatterns = [
    path(route = '', view = views.users_list, name='users_list')
]