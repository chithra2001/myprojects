from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('uhome',views.uhome,name="uhome"),
    path('hhome',views.hhome,name="hhome"),
    path('ulog',views.ulog,name="ulog"),
    path('ureg',views.ureg,name="ureg"),
    path('hreg',views.hreg,name="hreg"),
    path('hlog',views.hlog,name="hlog"),
    

    path('vcatla',views.vcatla,name="vcatla"),
    path('vkarimeen',views.vkarimeen,name="vkarimeen"),
    path('vmushi',views.vmushi,name="vmushi"),
    path('vrohu',views.vrohu,name="vrohu"),
    path('vprawns',views.vprawns,name="vprawns"),
    path('vvaala',views.vvaala,name="vvaala"),
    path('vvaraal',views.vvaraal,name="vvaraal"),
    path('vnutter',views.vnutter,name="vnutter"),
    path('vthilopia',views.vthilopia,name="vthilopia"),
    path('vkaari',views.vkaari,name="vkaari"),
    path('vchempally',views.vchempally,name="vchempally"),
    path('vparal',views.vparal,name="vparal"),
    path('vpallathi',views.vpallathi,name="vpallathi"),
    path('vkanambu',views.vkanambu,name="vkanambu"),
    path('vpullan',views.vpullan,name="vpullan"),

    path('vfishcate',views.vfishcate,name="vfishcate"),
    path('viewfishcate',views.viewfishcate,name="viewfishcate"),
    path('hcatla',views.hcatla,name="hcatla"),
    path('hkarimeen',views.hkarimeen,name="hkarimeen"),
    path('hmushi',views.hmushi,name="hmushi"),
    path('hrohu',views.hrohu,name="hrohu"),
    path('hprawns',views.hprawns,name="hprawns"),
    path('hvaala',views.hvaala,name="hvaala"),
    path('hvaraal',views.hvaraal,name="hvaraal"),
    path('hnutter',views.hnutter,name="hnutter"),
    path('hthilopia',views.hthilopia,name="hthilopia"),
    path('hkaari',views.hkaari,name="hkaari"),
    path('hchempally',views.hchempally,name="hchempally"),
    path('hparal',views.hparal,name="hparal"),
    path('hpallathi',views.hpallathi,name="hpallathi"),
    path('hkanambu',views.hkanambu,name="hkanambu"),
    path('hpullan',views.hpullan,name="hpullan"),



    path('viewpond',views.viewpond,name="viewpond"),
    path('vhbook',views.vhbook,name="vhbook"),
    path('hotelprof',views.hotelprof,name="hotelprof"),


    path('bookf<int:id>',views.bookf,name="bookf"),
    path('booking',views.booking,name="booking"),
    path('uremove<int:id>',views.uremove,name="uremove"),
    path('fishpay<int:id>',views.fishpay,name="fishpay"),
    
    path('uprofile',views.uprofile,name="uprofile"),
    path('ueditpro<int:id>',views.ueditpro,name="ueditpro"),

    path('frate<int:id>',views.frate,name="frate"),
    path('umap<int:id>',views.umap,name="umap"),
    path('bill<int:id>',views.bill,name="bill"),
    path('hotelbook<int:id>',views.hotelbook,name="hotelbook"),
    path('hbookrem<int:id>',views.hbookrem,name="hbookrem"),
    path('hotelpay<int:id>',views.hotelpay,name="hotelpay"),
    path('hotelbill<int:id>',views.hotelbill,name="hotelbill"),
    path('heditpro<int:id>',views.heditpro,name="heditpro"),

]
    
