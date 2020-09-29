from django.urls import path
from rest_framework import routers

from rfapi.views.get_land_characteristics_info_view import GetLandCharacteristicsInfoView
from rfapi.views.get_title_info_view import GetTitleInfoView
from .views import get_floor_info_view

# PropertyListViewSet,AddressInfoViewSet , address_info_list,kakao_coord,
# from listings.coord import get_coord,land_search

router = routers.DefaultRouter()
#router.register('AddressInfo', views.AddressInfoViewSet)
#router.register('PropertyList', views.PropertyListViewSet)
#router.register('PhotoList', views.PhotoViewSet)



app_name = 'rfapi'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # #path('AddressInfoList/', address_info_list),
    # #path('getKakaoCoord/', kakao_coord),
    path('getFloor/', get_floor_info_view.get_floor_info_view, name='getFloor'),
    path('getTitle-info/', GetTitleInfoView.as_view(), name='getTitle-info'),
    path('getLand-info/', GetLandCharacteristicsInfoView.as_view(), name='getTitle-info'),
]


# from django.urls import path

# from . import views

# from .views import PropertyCreateView


# from django.conf.urls import url

# from django.views.generic import TemplateView

