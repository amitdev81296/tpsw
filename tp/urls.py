from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^signup/', views.signup_form_display, name='signup_form_display'),
]