from django.shortcuts import render, HttpResponse
from .models import item
# Create your views here.


def get_todo(request):
    items = item.objects.all()
    context: {
        'items': items
    }
    return render(request, "todo/todo_list.html", context)
