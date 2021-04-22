from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Click

import json

@csrf_exempt
def index(request):
  if request.method == 'POST':
    data = request.body.decode('utf-8')
    data_json = json.loads(data)
    print(data_json)
  click = Click(x=4,y=4,hue=34)
  click.save()
  return HttpResponse("Hello, world. You're at the clicks index.")