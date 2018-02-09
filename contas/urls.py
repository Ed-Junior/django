from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$^', views.paginainicial),
    url(r'^login/', views.login),
]
