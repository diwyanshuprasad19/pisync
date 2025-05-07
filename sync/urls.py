from django.urls import path
from .views import SyncEventCreateView, DeviceSyncHistoryView, RepeatedFailuresView

urlpatterns = [
    path('sync-event/', SyncEventCreateView.as_view(), name='sync-event'),
    path('device/<str:id>/sync-history/', DeviceSyncHistoryView.as_view(), name='sync-history'),
    path('devices/repeated-failures/', RepeatedFailuresView.as_view(), name='repeated-failures'),
]
