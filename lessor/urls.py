from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('lhome',views.lhome,name="lhome"),
    path('Llog',views.Llog,name="Llog"),
    path('lreg',views.lreg,name="lreg"),
    path('addpond',views.addpond,name="addpond"),
    path('editpond<int:id>',views.editpond,name="editpond"),
    path('vpond',views.vpond,name="vpond"),
    path('lprofile',views.lprofile,name="lprofile"),
    path('leditpro<int:id>',views.leditpro,name="leditpro"),
    path('delpond<int:id>',views.delpond,name="delpond"),
    path('PondDet',views.PondDet,name="PondDet"),
    path('pondpay<int:id>',views.pondpay,name="pondpay"),
    path('remove<int:id>',views.remove,name="remove"),



    

]
    
