from django.shortcuts import render
from django.http import HttpResponse
from .models import Click


def index(request):
  click = Click(date="124432", time="12312", x=4,y=4,hue=34)
  click.save()
  return HttpResponse("Hello, world. You're at the clicks index.")