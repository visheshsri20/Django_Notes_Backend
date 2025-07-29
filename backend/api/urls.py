from django.urls import path
from . import views

urlpatterns = [
    path('notes/read/', views.NoteList.as_view(), name='note-list'),
    path('notes/create/', views.NoteCreate.as_view(), name='note-create'),
    path('notes/delete/<int:pk>/', views.NoteDelete.as_view(), name='delete-note'),
    path('notes/update/<int:pk>/', views.NoteUpdate.as_view(), name='update-note'),
]
