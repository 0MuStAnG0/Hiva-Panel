import subprocess
from celery import shared_task
from utils.sync_notifier import notify_sync

@shared_task
def sync_all_servers():
    try:
        result = subprocess.run(
            ["python3", "scripts/pg_multi_sync.py"],
            capture_output=True,
            text=True,
            check=True
        )
        notify_sync(success=True)
        return "Sync completed"
    except subprocess.CalledProcessError as e:
        notify_sync(success=False, message=e.stderr)
        return f"Sync failed: {e.stderr}"
