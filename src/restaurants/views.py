#import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import RestaurantLocation

# Create your views here.
#function based views
# def home_old(request):
#    html_var ="Narendra Singh Parihar"
#    html_ = f"""<!DOCTYPE html>
#    <html lang=en>
#
#    <head>
#    </head>
#    <body>
#    <h1>Hello World!</h1>
#    <p>This is {html_var} </p>
#    </body>
#
#    </html>
#    """
#    return HttpResponse(html_)
    #return render(request,"home.html",{})#response

# def home(request):
#     num = None
#     some_list = [
#                 random.randint(0,100000),
#                 random.randint(0,100000),
#                 random.randint(0,100000)
#                 ]
#     condition_bool_item = True
#     if condition_bool_item:
#         num = random.randint(0,100000)
#     context = {
#              "num":num,
#              "some_list":some_list
#              }
#     return render(request,"home.html",context) #response
#
# def about(request):
#     context = {}
#     return render(request,"about.html",context) #response
#
# def contact(request):
#     context = {}
#     return render(request,"contact.html",context) #response


# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         contex = {}
#         return render(request,"contact.html",contex)
#
#     def post(self, request, *args, **kwargs):
#         return render(request,"contact.html",contex)
#
#     def put(self, request, *args, **kwargs):
#         return render(request,"contact.html",contex)
# class HomeView(TemplateView):
#     template_name = "home.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(HomeView,self).get_context_data(**kwargs)
#         num = None
#         some_list = [
#                     random.randint(0,100000),
#                     random.randint(0,100000),
#                     random.randint(0,100000)
#                     ]
#         condition_bool_item = True
#         if condition_bool_item:
#             num = random.randint(0,100000)
#         context = {
#                  "num":num,
#                  "some_list":some_list
#                  }
#         return context

def restaurant_listview(request):
    template_name = "restaurants/restaurantlocation_list.html"
    queryset = RestaurantLocation.objects.all()
    context = {
              "object_list" : queryset
              }
    return render(request,template_name,context)

class RestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all()
    template_name = "restaurants/restaurantlocation_list.html"

class MexicanRestauratListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='mexican')
    template_name = "restaurants/restaurantlocation_list.html"

class AsianFusionRestauratListView(ListView):
    queryset = RestaurantLocation.objects.filter(category__iexact='asian fusion')
    template_name = "restaurants/restaurantlocation_list.html"
