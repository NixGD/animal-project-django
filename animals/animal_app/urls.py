from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^animal/(?P<animal_id>[0-9]+)/$', views.animal, name='animal'),
    url(r'^animal/(?P<animal_id>[0-9]+)/delete$', views.delete_animal, name='delete_animal'),
    url(r'^animal/(?P<animal_id>[0-9]+)/part/(?P<part_id>[0-9]+)/$', \
        views.edit_part, name='edit_part'),
    # url(r'^animal/(?P<animal_id>[0-9]+)/part/new/(?P<shape_id>[0-9]+)/$', \
    #     views.new_part, name='new_part'),
    url(r'^user', views.user_home, name='user'),
    url('', include('social_django.urls', namespace='social')),
    url(r'^login', views.login, name='')
]
