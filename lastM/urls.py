
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

        (r'^myapp/', include('myapp.urls')),
        (r'^home',include('myapp.urls')),
        #(r'^$', 'myapp.views.home'),
        (r'^admin/', include(admin.site.urls)),
        (r'^club','myapp.views.club'),
        (r'^about','myapp.views.about'),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)