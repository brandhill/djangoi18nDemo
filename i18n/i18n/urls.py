from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from views import landing

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)


urlpatterns += i18n_patterns('i18n.views',
    url(r'^', landing, name='home'),
)

# urlpatterns += i18n_patterns('',
#     url(r'^', include('i18n.urls')),
# )


# urlpatterns = patterns('i18n.views',
#     url(r'^$', landing),
# )


# urlpatterns += patterns('i18n.views',
#     url(r'^$', landing),
# )
