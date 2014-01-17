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
                        url(r'^home/$', 'home_view'),
						url(r'^latest/$', 'latest_books'),
						url(r'^$', 'pagina_de_redirecionamento'),
						)