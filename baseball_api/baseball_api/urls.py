from django.conf.urls import url
from django.contrib import admin

from baseball_api_app.views import MasterListCreateAPIView, MasterDetailUpdateDestroyAPIView, \
                                   BattingListCreateAPIView, BattingDetailUpdateDestroyAPIView, \
                                   PitchingListCreateAPIView, PitchingDetailUpdateDestroyAPIView, \
                                   FieldingListCreateAPIView, FieldingDetailUpdateDestroyAPIView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/masters/$', MasterListCreateAPIView.as_view(), name="master_list_create_api_view"),
    url(r'^api/masters/(?P<pk>\d+)/$', MasterDetailUpdateDestroyAPIView.as_view(), name="master_detail_update_destroy_api_view"),
    url(r'^api/battings/$', BattingListCreateAPIView.as_view(), name="batting_list_create_api_view"),
    url(r'^api/battings/(?P<pk>\d+)/$', BattingDetailUpdateDestroyAPIView.as_view(), name="batting_detail_update_destroy_api_view"),
    url(r'^api/pitchings/$', PitchingListCreateAPIView.as_view(), name="pitching_list_create_api_view"),
    url(r'^api/pitchings/(?P<pk>\d+)/$', PitchingDetailUpdateDestroyAPIView.as_view(), name="pitching_detail_update_destroy_api_view"),
    url(r'^api/fieldings/$', FieldingListCreateAPIView.as_view(), name="fielding_list_create_api_view"),
    url(r'^api/fieldings/(?P<pk>\d+)/$', FieldingDetailUpdateDestroyAPIView.as_view(), name="fielding_detail_update_destroy_api_view"),
]
