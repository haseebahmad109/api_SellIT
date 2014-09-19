from django.conf.urls import patterns, include, url
import xadmin
xadmin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Camera.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(xadmin.site.urls)),
)
