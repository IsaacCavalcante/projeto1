from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'meu_blog.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       )

urlpatterns += patterns('blog.views',
                        url(r'^home/$', 'pagina_de_redirecionamento'),
                        url(r'^latest/$', 'latest_books'),
                        url(r'^logon/$', 'pagina_logon'),
                        url(r'^$', 'home_view'),
                        url(r'^accounts/login/$', 'pagina_logon'),
                        url(r'^logout/$', 'logout'),
                        url(r'^logonsucesso/$', 'logon_sucesso'),
                        url(r'^deslogado/$', 'deslogado'),
                        url(r'^autorizado/$', 'autorizado'),
                        url(r'^artigo/add/$', 'artigo_add'),
                        url(r'^artigo/del/(?P<artigo_id>\d+)/$', 'artigo_del'),
                        url(r'^artigo/redirect/(?P<artigo_id>\d+)/$', 'artigo_redirect'),
                        (r'^artigo/(?P<artigo_id>\d+)/$', 'artigo'),
                        )