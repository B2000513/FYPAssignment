from django.urls import path
from . import views


urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/<int:pk>/", views.NoteDelete.as_view(), name="delte-note"),
]