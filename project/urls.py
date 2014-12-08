from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('main_site.urls', namespace="main_site", app_name="main_site")),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'administration/', include(admin.site.urls), name="admin"),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logged-out/$', 'django.contrib.auth.views.logout', {'template_name': 'account/logout.html'}, name="logout"),

    url(r'', include('posts.urls', namespace="posts", app_name="posts")),
)
