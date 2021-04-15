
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import bookmarks


def index(request):
    return render(request, 'index.html')
class BookmarkDetailView(generic.DetailView):
    model = bookmarks
    paginate_by = 2


class BookmarkListView(generic.ListView):
    model = bookmarks
    paginate_by = 2


class CreateBookmark(generic.CreateView):
    model = bookmarks
    fields = {'url', 'name', 'description', 'tag'}


class UpdateBookmark(generic.UpdateView):
    model = bookmarks
    fields = '__all__'
    context_object_name = 'bookmarks'


class DeleteBookmark(generic.DeleteView):
    model = bookmarks
    template_name = 'bookmarks/bookmarks_delete.html'
    success_url = reverse_lazy('bookmarks')