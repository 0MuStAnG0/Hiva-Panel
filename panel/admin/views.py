# panel/admin/views.py
import subprocess
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from utils.sync_notifier import notify_sync

@staff_member_required
def trigger_sync(request):
    try:
        result = subprocess.run(
            ["python3", "scripts/pg_multi_sync.py"],
            capture_output=True,
            text=True,
            check=True
        )
        notify_sync(success=True)
        messages.success(request, "✅ همگام‌سازی با موفقیت انجام شد.")
    except subprocess.CalledProcessError as e:
        notify_sync(success=False, message=e.stderr)
        messages.error(request, f"❌ خطا در اجرای sync: {e.stderr}")
    return HttpResponseRedirect(reverse("admin:index"))
