from django.urls import path, re_path
from . import views
from .views import (
    speaker_list,
    createSpeakers,
    viewspeaker,
    speakerUpdate,
    speakerDelete,
    choosetopic,
)

urlpatterns = [
    path("", speaker_list),
    path("topic/", choosetopic),
    path("create/", createSpeakers),
    path("create/", createSpeakers),
    path("<int:id>/", viewspeaker),
    path("<int:id>/update/", speakerUpdate),
    path("<int:id>/delete/", speakerDelete),
    path("speakers/", views.speaker_list, name="speakers"),
    path("speakers/<int:id>/", views.viewspeaker, name="viewspeaker"),
]
