from django.conf.urls import url

from . import views

app_name = 'menu'

urlpatterns = [
    url(r'^$', views.DishList.as_view()),
    url(r'^page(?P<page>\d+)', views.DishList.as_view()),
]