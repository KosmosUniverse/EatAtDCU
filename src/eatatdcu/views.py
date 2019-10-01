from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant,Campus

def index(request):
   context = {}
   return render(request,'eatatdcu/index.html',context)

def restaurants(request):
   context = {}

   #TODO get the campus name from the request
   #TODO retrieve the campus id from the db given this campus name
   #TODO find all restaurants for that campus 
   #TODO put the restaurant info in the context dictionary
   #TODO handle invalid campus names

   return render(request,'eatatdcu/restaurants.html',context)
