from django.conf.urls import patterns, include, url
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','repository.views.home', name="home"),           #this home page url
    (r'^course/', include('course.urls')),
    (r'^assignment/', include('assignment.urls')),
    (r'^notice/', include('notice.urls')),
    (r'^lecturenotes/', include('lecturenotes.urls')),
    (r'^notification/', include('notification.urls')),
    (r'^student/', include('student.urls')),
    (r'^userauth/', include('userauth.urls')),
    (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root: settings.STATIC_ROOT'}),
    (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root: settings.MEDIA_ROOT'}),
    url(r'^admin/', include(admin.site.urls)),
)
