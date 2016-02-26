from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls import include, url
from django.views.debug import default_urlconf
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('caterlist.urls')),
    url(r'^$', default_urlconf),
)

# from django.conf.urls import include, url
# from django.contrib import admin

# urlpatterns = [
# 	url(r'^', include('caterlist.urls')),
#     url(r'^admin/', admin.site.urls),
# ]
