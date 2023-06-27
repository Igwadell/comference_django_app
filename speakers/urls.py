from django.urls import path, re_path
from . import views
from .views import (
    speakerList,
    createSpeakers,
    viewSpeaker,
    speakerUpdate,
    speakerDelete,
    choosetopic,
)

urlpatterns = [
    path("", speakerList),
    path("topic/", choosetopic),
    path("create/", createSpeakers),
    path("create/", createSpeakers),
    path("<int:id>/", viewSpeaker),
    path("<int:id>/update/", speakerUpdate),
    path("<int:id>/delete/", speakerDelete),
    path('speakers/', views.speakerList, name='speakers'),
]
