from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Click

import json

# fakeDB = [{'date':"02-02-2021", 'time':"05:45:32", 'x':1, 'y':2, 'hue':255}]

@csrf_exempt
def index(request):
  return HttpResponse("heellloooOOOOOOO")

@csrf_exempt
def all(request):
  allClicks = list(Click.objects.values())
  # print(allClicks)
  # return JsonResponse(fakeDB, safe=False, status=200)
  return JsonResponse(allClicks, safe=False, status=200)

@csrf_exempt
def new(request):
  errorMessage = validInput(request)
  if len(errorMessage) > 0:
    error = {}
    error["message"] = errorMessage
    return JsonResponse(error, status=400)

  data = request.body.decode('utf-8')
  data_json = json.loads(data)

  click = Click(x=data_json['x'], y=data_json['y'],hue=data_json['hue'])
  click.save()
  # newData = {'date':"", 'time':"", 'x':data_json['x'], 'y':data_json['y'], 'hue':data_json['hue']}
  # fakeDB.append(newData)
  # print(fakeDB)
  return HttpResponse("added!")

def validInput(request):
  if request.method == 'POST':
    data = request.body.decode('utf-8')
    data_json = json.loads(data)

    if len(data) == 0:
      return "fields cannot be empty."
    requestFields = data_json.keys()
    expectedFields = ["x", "y", "hue"]
    diff = requestFields - expectedFields
    if len(diff) > 0:
      badField = diff.pop()
      # return error message about bad field
      return badField + " not recognized."

      # check for empty field value
    for field in requestFields:
      if data_json[field] is None or data_json[field] == "":
        return field + " cannot be empty."
  
  else:
    return "not post request"
  
  # no errors
  return ""