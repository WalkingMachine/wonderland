from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^api/entity/$', views.EntityList.as_view()),
    url(r'^api/human/$', views.HumanList.as_view()),
    url(r'^api/object/$', views.ObjectList.as_view()),
    url(r'^api/room/$', views.RoomList.as_view()),
    url(r'^api/waypoint/$', views.WaypointList.as_view()),
    url(r'^api/artag/$', views.ArTagList.as_view()),
]
