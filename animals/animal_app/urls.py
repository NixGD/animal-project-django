from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.user_home, name='index'),
    url(r'^animal/(?P<animal_id>[0-9]+)/$', views.animal, name='animal'),
    url(r'^animal/(?P<animal_id>[0-9]+)/(?P<part_id>[0-9]+)/$', views.animal, name='animal'),
    url(r'^animal/(?P<animal_id>[0-9]+)/delete$', views.delete_animal, name='delete_animal'),
    url(r'^part/(?P<part_id>[0-9]+)/delete$', views.delete_part, name='delete_part'),
    # url(r'^animal/(?P<animal_id>[0-9]+)/part/new/(?P<shape_id>[0-9]+)/$', \
    #     views.new_part, name='new_part'),
    url(r'^collection/(?P<collection_id>[0-9]+)/$', views.collection, name='collection'),
    url(r'^user', views.user_home, name='user'),

    url('', include('social_django.urls', namespace='social')),
    url(r'^login', views.login_view, name='login'),
    url(r'^logout', views.logout_view, name='logout')
]
