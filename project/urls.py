from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.views.static import serve as static_serve
from django.contrib.admin.views.decorators import staff_member_required
from house_finances import views as house_finance_view


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # This is the URL Varnish will ping to check the server health.
    url(r'^app_status/$', 'toolbox.views.app_status', name='status'),
    url(r'^$', house_finance_view.index, name='index'),
    url(r'^roommate/$', house_finance_view.roommie_detail, name='roommate-detail'),
    url(r'^shit/$', house_finance_view.item_list, name='shit-list'),
    url(r'^shit/detail/$', house_finance_view.item_detail, name='shit-detailed'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        url(r'^static/(?P<path>.*)$', 'serve', {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True,
        }),
        url(r'^media/(?P<path>.*)$', 'serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
    )

if settings.PRODUCTION:
    urlpatterns += patterns('',
        url(r'^munin/(?P<path>.*)$', staff_member_required(static_serve), {
            'document_root': settings.MUNIN_ROOT,
        })
   )
