from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/entity/$', views.EntityList.as_view()),
    url(r'^api/space/$', views.SpaceList.as_view())
]
