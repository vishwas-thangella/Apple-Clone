from django.contrib import admin
from django.urls import path
from myapp import views

admin.site.site_header = "Apple"
admin.site.index_title = "Welcome to Apple.inc"
admin.site.site_title = "Apple.inc"

urlpatterns = [
    path('',views.Home,name='homepage'),
    path('store',views.Store,name="store"),
    path('services',views.Services,name="support"),
    path('shop/<device>',views.shop),
    path('signin',views.Signin)
]
