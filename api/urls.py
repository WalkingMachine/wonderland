from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/entity/$', views.EntityList.as_view()),
    url(r'^api/area/$', views.AreaList.as_view()),
    url(r'^api/waypoint/$', views.WaypointList.as_view())
]
