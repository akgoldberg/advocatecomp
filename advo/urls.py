from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

from ajax_select import urls as ajax_select_urls

from contacts.views import FilteredSingleTableView
from contacts.tables import ContactTable
from contacts.models import Contact


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'magazine.views.index'),
    url(r'^about$', 'magazine.views.masthead'),
    #url(r'^alumni$', 'contacts.views.alumnidb'),
    url(r'^alumni$', FilteredSingleTableView.as_view(
        table_class = ContactTable, 
        model = Contact, 
        template_name = 'alumni.html', 
        table_pagination = {"per_page":20}) , 
        name='filtered_single_table_view'
        ),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^updates/', 'contacts.views.updates'),
    url(r'^user/(?P<contact_id>\d+)/$', 'contacts.views.profile', name = 'profile'),
    #http://stackoverflow.com/questions/901551/how-do-i-include-image-files-in-django-templates
    #http://stackoverflow.com/questions/19132123/name-settings-is-not-defined
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^account/$', 'contacts.views.edit_user'),
)

