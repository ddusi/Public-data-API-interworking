from django.urls import path

from . import views

# from .views import PropertyCreateView, LandCreateView

app_name = 'pages'
urlpatterns = [

	path('property-detail/', views.property_detail, name='property-detail'),

]
