from django.urls import path

from . import views

urlpatterns = [
    path('', views.uindex, name='uindex'),
    path('uaboutus', views.uaboutus, name='uaboutus'),
    path('ucontactus', views.ucontactus, name='ucontactus'),
    path('usignup', views.usignup, name='usignup'),
    path('uproduct', views.uproduct, name='uproduct'),
    path('usubcategory', views.usubcategory, name='usubcategory'),
    path('uproductdetails', views.uproductdetails, name='uproductdetails'),
    path('uprofile', views.uprofile, name='uprofile'),
    path('ubooking', views.ubooking, name='ubooking'),
    path('ucart', views.ucart, name='ucart'),
    path('ubills', views.ubills, name='ubills'),
    path('upayment', views.upayment, name='upayment'),
    path('upaymentlist', views.upaymentlist, name='upaymentlist'),
    path('usignin', views.usignin, name='usignin'),
    path('usignout', views.usignout, name='usignout'),
    path('uforgotpassword', views.uforgotpassword, name='uforgotpassword'),
    path('set_city/', views.set_city, name='set_city'),
    
    ]

