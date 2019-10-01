
from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant,Campus

def index(request):
   context = {}
   return render(request,'eatatdcu/index.html',context)

def restaurants(request):
   context = {'campus':None, 'restaurant':None}

   campus = request.GET.get('campus').lower()

   campusList = Campus.objects.filter(name=campus)
   if (len(campusList) >= 1):
      context["campus"] = campus
      restList = Restaurant.objects.filter(campus_id=campusList[0].campus_id)
      if (len(restList) >= 1):
         context["restaurant"] = restList
      

   #TODO get the campus name from the request
   #TODO retrieve the campus id from the db given this campus name
   #TODO find all restaurants for that campus 
   #TODO put the restaurant info in the context dictionary
   #TODO handle invalid campus names

   return render(request,'eatatdcu/restaurants.html',context)
