from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
     path('', views.homepage,name='homepage'),
     path('registerasbuyer/', views.registerasbuyer,name='registerasbuyer'),
     path('registerasseller/', views.registerasseller,name='registerasseller'),
     path('login/', views.login,name='login'),
     path('about/', views.about,name='about'),
    path("logout/", views.logout,name = "logout"),
    path("mycrops/", views.mycrops,name = "mycrops"),
    path("myorders/", views.myorders,name = "myorders"),
    path("mycrops/deletecrop/<int:id>", views.deletecrop,name = "deletecrop"),
    path("mycrops/editcrop/<int:id>", views.editcrop,name = "editcrop"),
    path("crops/", views.crops,name = "crops"),
    path("crops/<int:id>/", views.readmore,name = "readmore"),
    path("crops/negotiate/<int:id>", views.negotiate,name = "negotiate"),
    path("sellernegotiations/", views.sellernegotiations,name = "sellernegotiations"),
    path("sellernegotiations/accept/<int:id>", views.accept,name = "accept"),
    path("sellernegotiations/reject/<int:id>", views.reject,name = "reject"),
    path("buyernegotiations/", views.buyernegotiations,name = "buyernegotiations"),
    path("buyernegotiations/buynow/<int:id>", views.buynow,name = "buynow"),
    
]
