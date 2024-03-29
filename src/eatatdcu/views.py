
from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant,Campus
import requests
import json

def index(request):
   context = {'campusNB':None, 'campusList':None}

   campusList = Campus.objects.all()
   if (len(campusList) >= 1):
       context["campusNB"] = len(campusList)
       for cmps in campusList:
           cmps.name.replace(" ", "+");
       context["campusList"] = campusList

   return render(request,'eatatdcu/index.html',context)

def restaurants(request):
   context = {'campus':None, 'restaurant':None}

   campus = request.GET.get('campus').lower()
   staff = request.GET.get('staff')
   weekends = request.GET.get('weekends')
   specials = request.GET.get('specials')

   try:
       staff = staff.lower()
   except AttributeError:
       staff = "off"
   try:
        weekends = weekends.lower()
   except AttributeError:
        weekends = "off"
   try:
       weekends = weekends.lower()
   except AttributeError:
       weekends = "off"


   campusList = Campus.objects.filter(name=campus)
   if (len(campusList) >= 1):
      context["campus"] = campus
      restList = Restaurant.objects.filter(campus_id=campusList[0].campus_id)
      if (len(restList) >= 1):
         context["restaurant"] = restList


   # get the campus name from the request
   campus_name = request.GET.get('campus').lower()

   try:
      # retrieve the campus id from the db given this campus name
      campus = Campus.objects.get(name=campus_name)
      # find all restaurants for that campus
      restaurants = Restaurant.objects.filter(campus_id=campus)

      if (staff == "on"):
          restaurants = restaurants.filter(staff_only=True)
      if (weekends == "on"):
         restaurants = restaurants.filter(is_open_we=True)

      restaurants = restaurants.values()

      # put the information returned from the db in the context dictionary
      #context = {'restaurants':restaurants}

      for restau in restaurants:
          if (specials == "on"):
              webservice_url = 'http://jfoster.pythonanywhere.com/specials/'+restau.get("name")

              # call the web service to get the daily special for "restaurant"

              # pass the information returned by the web service into the "specials.html" template using render function
              webServ = requests.get(webservice_url)

              load = json.loads(webServ.text)
              if ('error_num' in load.keys()):
                 restau['error_num'] = load['error_msg']
              else:
                 restau['specials'] = "hey"
                 restau['daily'] = load['daily_special']
                 restau['date'] = load['date']
      context['restaurants'] = restaurants
   except Campus.DoesNotExist:
      # handles the case where an invalid campus name is entered
      context = {'error':'No such campus'}

   return render(request,'eatatdcu/restaurants.html',context)

def specials(request,restaurant):
   context = {}
   webservice_url = 'http://jfoster.pythonanywhere.com/specials/'+restaurant

   # call the web service to get the daily special for "restaurant"

   # pass the information returned by the web service into the "specials.html" template using render function
   webServ = requests.get(webservice_url)

   load = json.loads(webServ.text)

   if ('error_num' in load.keys()):
      context = {'error':load['error_msg']}
   else:
      context = {'daily':load['daily_special'], 'name':load['restaurant_name'], 'date':load['date']}

   return render(request, 'eatatdcu/specials.html', context)
