from django.shortcuts import render, redirect
from . models import Table
from .forms import TableForm

def index(request):
    return render(request,'main/index.html')

def db(request):
    database = Table.objects.all()
    return render(request, 'main/db.html', {'database': database})
def makedb(request):
    error = ''
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form False'
    form = TableForm()
    context = {
    'form' : form
    }
    return render(request, 'main/makedb.html', context)
