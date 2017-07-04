from django.shortcuts import render
from django.http import Http404

from inventory.models import Item

def index(request):
  return HttpResponse('<p>In Index view</p>')

def item_detail(request, id):
  return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id))
