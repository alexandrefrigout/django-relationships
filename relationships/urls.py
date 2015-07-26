from .compat import patterns, url


urlpatterns = patterns('relationships.views',
    url(r'^$', 'relationship_redirect', name='relationship_list_base'),
    url(r'^(?P<username>[\w.@+-]+)/(?:(?P<status_slug>[\w-]+)/)?$', 'relationship_list', {'accepted': True}, name='relationship_list'),
    url(r'^(?P<username>[\w.@+-]+)/(?P<status_slug>[\w-]+)/awaiting', 'relationship_list', {'accepted': False}, name='relationship_list'),
    url(r'^add/(?P<username>[\w.@+-]+)/(?P<status_slug>[\w-]+)/$', 'relationship_handler', {'add': True}, name='relationship_add'),
    url(r'^remove/(?P<username>[\w.@+-]+)/(?P<status_slug>[\w-]+)/$', 'relationship_handler', {'add': False}, name='relationship_remove'),
    #Ajout Alex
    url(r'^accept/(?P<username>[\w.@+-]+)/(?P<status_slug>[\w-]+)/$', 'relationship_manage', {'accept' : True, 'reject' : False}, name='relationship_accept'),

    url(r'^reject/(?P<username>[\w.@+-]+)/(?P<status_slug>[\w-]+)/$', 'relationship_manage', {'accept': False, 'reject' : True}, name='relationship_reject'),
    #Fin ajout
)
