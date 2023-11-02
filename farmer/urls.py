from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('fhome',views.fhome,name="fhome"),
    path('flog',views.flog,name="flog"),
    path('freg',views.freg,name="freg"),
    path('addfish',views.addfish,name="addfish"),
    path('viewfish',views.viewfish,name="viewfish"),
    path('forder',views.forder,name="forder"),
    path('vfeed',views.vfeed,name="vfeed"),
    path('viewpond',views.viewpond,name="viewpond"),
    path('fmap<int:id>',views.fmap,name="fmap"),


    path('bookfeed<int:id>',views.bookfeed,name="bookfeed"),
    path('ordertb',views.ordertb,name="ordertb"),
    path('feedpay',views.feedpay,name="feedpay"),
    path('feedbill<int:id>',views.feedbill,name="feedbill"),
    path('ordremove<int:id>',views.ordremove,name="ordremove"),

    path('useraccp<int:id>',views.useraccp,name="useraccp"),
    path('userrej<int:id>',views.userrej,name="userrej"),
    path('hotelaccp<int:id>',views.hotelaccp,name="hotelaccp"),
    path('hotelrej<int:id>',views.hotelrej,name="hotelrej"),



    path('delfish<int:id>',views.delfish,name="delfish"),
    path('editproduct<int:id>',views.editproduct,name="editproduct"),
    path('fprofile',views.fprofile,name="fprofile"),
    path('cart',views.cart,name="cart"),
    path('fremove<int:id>',views.fremove,name="fremove"),
    path('feditpro<int:id>',views.feditpro,name="feditpro"),
    path('salesreport',views.salesreport,name="salesreport"),
   

]
    
