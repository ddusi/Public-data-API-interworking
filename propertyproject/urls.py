
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#      #path('',)
#  ]

urlpatterns = [
    path('', include('pages.urls')),

    #path('listings/', include('listings.urls')),
    #path('accounts/', include('accounts.urls')),
    #path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
    #path('sample/', include('sample.urls')),
    path('rfapi/', include('rfapi.urls')),

   #path('admin_app/', include('admin_app.urls')),
   


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
