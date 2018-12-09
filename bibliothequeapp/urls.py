from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'', include('django.contrib.auth.urls'), name='login'),
    url(r'^app',views.app,name='app' ),
    url(r'liste',views.liste,name='liste')
]