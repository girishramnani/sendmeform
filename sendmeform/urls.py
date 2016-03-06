from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from receiveform import views
from receiveform.views import Index, ClientDashBoard, ClientFormEndpoint

urlpatterns = [
    # Examples:
    # url(r'^$', 'sendmeform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^staticPage$',TemplateView.as_view(template_name="default_redirect_page.html") \
        ,name="fallbackRedirect"),
    url(r"^(?P<public_token>\w+)",ClientFormEndpoint.as_view(),name="endpoint"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Index.as_view(),name="index"),
    url(r'^user/(?P<token>\w+)',ClientDashBoard.as_view(),name="dashboard"),

]
