from django.conf.urls import url

import views

urlpatterns = [
    url(r'^api/entity/$', views.EntityList.as_view()),
    url(r'^api/people/$', views.PeopleList.as_view()),
    url(r'^api/clear-people/$', views.ClearPeople.as_view())
]
