from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('ahome',views.ahome,name="ahome"),
    path('alog',views.alog,name="alog"),
    path('areg',views.areg,name="areg"),
    path('addfish',views.addfish,name="addfish"),
    path('addfeed',views.addfeed,name="addfeed"),
    path('tables',views.tables,name="tables"),
    path('tables1',views.tables1,name="tables1"),
    path('tables2',views.tables2,name="tables2"),

    path('faccept<int:id>',views.faccept,name="faccept"),
    path('freject<int:id>',views.freject,name="freject"),

    path('viewpond',views.viewpond,name="viewpond"),
    path('vfish',views.vfish,name="vfish"),
    path('vfeed',views.vfeed,name="vfeed"),
    path('ponddel<int:id>',views.ponddel,name="ponddel"),
    path('bookdtls',views.bookdtls,name="bookdtls"),

    

   
    
]
    
