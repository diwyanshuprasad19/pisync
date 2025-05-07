class SyncEventError(Exception):
    """Base class for sync event errors."""

class DeviceNotFoundError(SyncEventError):
    """Raised when a device has no sync history."""
