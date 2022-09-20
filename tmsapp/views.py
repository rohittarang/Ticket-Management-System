from django.shortcuts import render, redirect
from .models import Ticket2
from tmsapp.forms import SaveTicket
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Index(request):
    ticketdata = Ticket2.objects.filter(ticketholder = request.user)
    if request.method == "POST":
        form = SaveTicket(request.POST,request.FILES or None) 
        if form.is_valid():
            form.save(commit=False).ticketholder = request.user
            form.save()
            messages.success(request,("Data has been added successfully !!"))
            print(form)
            return redirect('index')
    else:
        form = SaveTicket()
    return render(request, 'index.html', {'ticketdata':ticketdata})

@login_required
def Delete(request, id):
    ticketdata = Ticket2.objects.get(pk=id)
    ticketdata.delete()
    messages.success(request,("Data has been deleted successfully !!"))
    return redirect('index')

@login_required
def Edit(request, id):
    if request.method == "POST":
        ticketdata = Ticket2.objects.get(pk=id)
        form = SaveTicket(request.POST,request.FILES or None, instance=ticketdata)
        if form.is_valid():
            form.save()
            messages.success(request,("Data has been updated successfully !!"))
            print(form)
        return redirect('index')
    else:
        ticketdata = Ticket2.objects.get(pk=id)
        print(ticketdata.file)
        return render(request, 'edit.html', {'ticketdata':ticketdata})



