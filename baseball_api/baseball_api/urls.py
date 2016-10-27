from django.conf.urls import url
from django.contrib import admin

from baseball_api_app.views import MasterListCreateAPIView, MasterUpdateDestroyAPIView, \
                                   BattingListCreateAPIView, BattingUpdateDestroyAPIView, \
                                   PitchingListCreateAPIView, PitchingUpdateDestroyAPIView, \
                                   FieldingListCreateAPIView, FieldingUpdateDestroyAPIView, \


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/master/$', MasterListCreateAPIView.as_view(), name="master_list_create_api_view"),
    url(r'^api/master/(?P<pk>\d+)/$', MasterUpdateDestroyAPIView.as_view(), name="master_update_destroy_api_view"),
    url(r'^api/batting/$', BattingListCreateAPIView.as_view(), name="batting_list_create_api_view"),
    url(r'^api/batting/(?P<pk>\d+)/$', BattingUpdateDestroyAPIView.as_view(), name="batting_update_destroy_api_view"),
    url(r'^api/pitching/$', PitchingListCreateAPIView.as_view(), name="pitching_list_create_api_view"),
    url(r'^api/pitching/(?P<pk>\d+)/$', PitchingUpdateDestroyAPIView.as_view(), name="pitching_update_destroy_api_view"),
    url(r'^api/fielding/$', FieldingListCreateAPIView.as_view(), name="fielding_list_create_api_view"),
    url(r'^api/fielding/(?P<pk>\d+)/$', FieldingUpdateDestroyAPIView.as_view(), name="fielding_update_destroy_api_view"),
]
