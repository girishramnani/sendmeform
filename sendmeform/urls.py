from django.conf.urls import include, url
from django.contrib import admin

from receiveform import views
from receiveform.views import Index

urlpatterns = [
    # Examples:
    # url(r'^$', 'sendmeform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',Index.as_view())
]
