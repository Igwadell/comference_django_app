from django.urls import path, re_path
from . import views
from .views import (
    speakerList,
    createSpeakers,
    viewspeaker,
    speakerUpdate,
    speakerDelete,
    choosetopic,
)

urlpatterns = [
    path("", speakerList),
    path("topic/", choosetopic),
    path("create/", createSpeakers),
    path("create/", createSpeakers),
    path("<int:id>/", viewspeaker),
    path("<int:id>/update/", speakerUpdate),
    path("<int:id>/delete/", speakerDelete),
    path("speakers/", views.speakerList, name="speakers"),
    path("speakers/<int:id>/", views.viewspeaker, name="viewspeaker"),
]
