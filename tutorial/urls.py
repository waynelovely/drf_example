from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views
from django.contrib.staticfiles import views as staticfiles_views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^static/(?P<path>.*)$', staticfiles_views.serve),
    url(r'^servers/$', views.server_list),
    url(r'^servers/(?P<pk>[0-9]+)$', views.server_detail),

]
