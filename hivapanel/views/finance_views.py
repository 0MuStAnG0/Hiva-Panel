from django.shortcuts import render
from utils.finance import calculate_net_profit

def finance_dashboard(request):
    data = calculate_net_profit(9000000, 3500000)
    return render(request, "finance.html", {"data": data})
