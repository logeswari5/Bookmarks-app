from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookmarks/', views.BookmarkListView.as_view(), name='bookmarks'),
    path('bookmarks/<int:pk>', views.BookmarkDetailView.as_view(), name='bookmarks-detail'),
    path('bookmarks/create/', views.CreateBookmark.as_view(), name='bookmarks-create'),
    path('bookmarks/<int:pk>/update/', views.UpdateBookmark.as_view(), name='bookmarks-update'),
    path('bookmarks/<int:pk>/delete/', views.DeleteBookmark.as_view(), name='bookmarks-delete'),

]
