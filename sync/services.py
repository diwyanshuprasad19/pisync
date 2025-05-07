from .models import SyncEvent
from .exceptions import DeviceNotFoundError
from .constants import ERROR_THRESHOLD

class SyncService:

    @staticmethod
    def create_sync_event(data):
        # Create the event
        event = SyncEvent.objects.create(**data)
        
        # Bonus: Check last 3 failures for this device
        recent_failures = SyncEvent.objects.filter(
            device_id=event.device_id,
            total_errors__gt=0
        ).order_by('-timestamp')[:3]
        
        if recent_failures.count() == 3 and all(e.total_errors > 0 for e in recent_failures):
            print(f"⚠️ Device {event.device_id} has failed 3 times in a row!")

        return event

    @staticmethod
    def get_sync_history(device_id):
        events = SyncEvent.objects.filter(device_id=device_id).order_by('-timestamp')
        if not events.exists():
            raise DeviceNotFoundError(f"No sync history for device {device_id}.")
        return events

    @staticmethod
    def get_devices_with_repeated_failures():
        from django.db.models import Count
        failed_devices = (
            SyncEvent.objects.filter(total_errors__gt=0)
            .values('device_id')
            .annotate(failure_count=Count('id'))
            .filter(failure_count__gt=ERROR_THRESHOLD)
            .values_list('device_id', flat=True)
        )
        return SyncEvent.objects.filter(device_id__in=failed_devices)
