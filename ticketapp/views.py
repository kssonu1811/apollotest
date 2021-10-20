from django.http import request
from django.shortcuts import render
from .models import Contact, status
from .forms import Ticketform

# Create your views here.
def ticket(request):
    registered = False
    if request.method == 'POST':
        ticket_form = Ticketform(data=request.POST)
        if ticket_form.is_valid():
            ticket_form.save()
            
            registered = True
        else:
            return(ticket_form.errors)
    else:
        ticket_form = Ticketform()
    data = {
        'ticket_form': ticket_form,
        'registered': registered,
    }
    return render(request, 'account/ticket.html',data)

def statuss(request):
    tickets = Contact.objects.all()
    statusss = status.objects.all()

    data ={
        "tickets" : tickets,
        "statusss" : statusss
    }
    return render(request, 'account/status.html', data)