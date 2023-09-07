from django.shortcuts import render, redirect
from .models import SQLData
from .forms import SQLDataForm

# Create your views here.

def home(request):
    data = SQLData.objects.all()
    return render(request, 'myapp/home.html', {'data': data})


def createRow(request):
    form = SQLDataForm()
    if request.method == "POST":
        form = SQLDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form':form}
    return render(request,'myapp/create_update_form.html',context)


def updateRow(request, pk):
    stock = SQLData.objects.get(id=pk)
    form = SQLDataForm(instance=stock)

    if request.method == "POST":
        form = SQLDataForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect("home")


    context = {"form" : form}
    return render(request, "myapp/create_update_form.html", context)


def deleteRow(request, pk):
    stock = SQLData.objects.get(id=pk)
    stock.delete()
    return redirect("home")
