from django.conf.urls import url
from django.contrib import admin
from regist import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^join/$', views.signup, name='join'),
    url(r'^login/$', views.signin, name='login'),
]
