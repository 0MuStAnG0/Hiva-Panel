# support/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm, TicketReplyForm

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, "ticket_list.html", {"tickets": tickets})

@login_required
def ticket_create(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("ticket-list")
    else:
        form = TicketForm()
    return render(request, "ticket_create.html", {"form": form})

@login_required
def ticket_reply(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == "POST":
        form = TicketReplyForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            ticket.status = "answered"
            ticket.save()
            return redirect("ticket-list")
    else:
        form = TicketReplyForm(instance=ticket)
    return render(request, "ticket_reply.html", {"form": form, "ticket": ticket})
