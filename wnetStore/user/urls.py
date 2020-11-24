from django.conf.urls import url
from .views import UserList, UserDetail

# Se definen los endpoints los cuales van a ser accesibles desde el navegador web.
urlpatterns = [
    url(r'^user/$', UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]
