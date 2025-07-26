# adminpanel/finance_views.py

from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.db.models import Sum, Count
from subscriptions.models import Plan, Order
from django.utils.timezone import now, timedelta
from .forms import PlanForm

@staff_member_required
def finance_dashboard(request):
    today = now().date()
    last_30 = today - timedelta(days=30)

    daily_orders = (
        Order.objects.filter(date__gte=last_30)
        .extra(select={'day': 'date(date)'})
        .values('day')
        .annotate(revenue=Sum('amount'), count=Count('id'))
        .order_by('day')
    )

    total_revenue = Order.objects.aggregate(total=Sum('amount'))['total'] or 0

    return render(request, "finance_dashboard.html", {
        "orders": daily_orders,
        "total_revenue": total_revenue,
    })

@staff_member_required
def manage_plans(request):
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage-plans')
    else:
        form = PlanForm()

    plans = Plan.objects.all()
    return render(request, "manage_plans.html", {"plans": plans, "form": form})
