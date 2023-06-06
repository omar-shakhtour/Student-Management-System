from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect("home")
            else:
                messages.success(
                    request, "Incorrect username/password, please try again."
                )
        # else if user is already logged in, do the following:
        else:
            messages.error(request, "Username and password are required.")
    return render(request, "home.html", {"records": records})


def student_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        student_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"student_record": student_record})
    else:
        messages.success(request, "You must be logged in to view that page.")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "The record has been successfully deleted.")
        return redirect("home")
    else:
        messages.success(request, "You must be logged in to perform this function.")
        return redirect("home")


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record successfully added")
                return redirect("home")
        else:
            return render(request, "add_record.html", {"form": form})
    else:
        messages.success(request, "You must be logged in.")
        return redirect("home")


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record successfully updated.")
            return redirect("home")
        return render(request, "update_record.html", {"form": form})
    else:
        messages.success(request, "You must be logged in.")
        return redirect("home")


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home")
