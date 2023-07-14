from django.urls import path
from .import views
from InfoCollect import settings
from django.conf.urls.static import static
urlpatterns = [
    path('get_user_info_form', views.get_user_info_form, name = 'get_user_info_form'),
    path('save_user_info', views.save_user_info, name = 'save_user_info'),
]