from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import SyncEventSerializer
from .services import SyncService
from .exceptions import DeviceNotFoundError
from .constants import MESSAGES


class SyncEventCreateView(generics.CreateAPIView):
    """
    POST /api/sync-event/
    Creates a sync event and triggers failure check.
    """
    serializer_class = SyncEventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event = SyncService.create_sync_event(serializer.validated_data)
        return Response({
            "message": MESSAGES["SUCCESS"],
            "data": SyncEventSerializer(event).data
        })


class DeviceSyncHistoryView(generics.ListAPIView):
    """
    GET /api/device/<id>/sync-history/
    Retrieves sync history for a specific device.
    """
    serializer_class = SyncEventSerializer

    def get(self, request, id):
        try:
            events = SyncService.get_sync_history(id)
            data = SyncEventSerializer(events, many=True).data
            return Response(data)
        except DeviceNotFoundError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)


class RepeatedFailuresView(generics.ListAPIView):
    """
    GET /api/devices/repeated-failures/
    Lists devices with more than 3 total failures.
    """
    serializer_class = SyncEventSerializer

    def get(self, request):
        events = SyncService.get_devices_with_repeated_failures()
        data = SyncEventSerializer(events, many=True).data
        return Response(data)
