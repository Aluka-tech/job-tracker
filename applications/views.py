from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import JobApplication
from django.db.models import Count
from .forms import JobApplicationForm



# Create your views here.
def home(request):
    return render(request, 'applications/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')  # send user to login page after signup

    else:
        form = UserCreationForm()

    return render(request, 'applications/register.html', {'form': form})


@login_required
def dashboard(request):
    applications = JobApplication.objects.filter(user=request.user)

    total = applications.count()

    status_counts = applications.values('status').annotate(count=Count('status'))
    status_dict = {item['status']: item['count'] for item in status_counts}

    recent_applications = applications.order_by('-date_applied')[:5]

    context = {
        'total': total,
        'applied': status_dict.get('Applied', 0),
        'interview': status_dict.get('Interview', 0),
        'offer': status_dict.get('Offer', 0),
        'rejected': status_dict.get('Rejected', 0),
        'recent_applications': recent_applications,
    }

    return render(request, 'dashboard.html', context)

@login_required
def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)   # don't save yet
            app.user = request.user         # attach logged-in user
            app.save()
            return redirect(f"/dashboard/?saved=true") 
    else:
        form = JobApplicationForm()         # empty form for GET

    return render(request, "applications/add_application.html", {
        "form": form
    })    


@login_required
def application_list(request):
    applications = JobApplication.objects.filter(
        user=request.user
    ).order_by("-date_applied")  # most recent first

    return render(request, "applications/application_list.html", {
        "applications": applications
    })    

@login_required
def application_detail(request, id):
    application = get_object_or_404(
        JobApplication,
        id=id,
        user=request.user   # 🔒 critical for security
    )

    return render(request, "applications/application_detail.html", {
        "application": application
    })   


@login_required
def edit_application(request, id):
    application = get_object_or_404(
        JobApplication,
        id=id,
        user=request.user
    )

    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=application)

        if form.is_valid():
            updated_app = form.save(commit=False)
            updated_app.user = request.user  # keep ownership safe
            updated_app.save()

            return redirect(f"/applications/{application.id}/?saved=true") 
    else:
        form = JobApplicationForm(instance=application)

    return render(request, "applications/edit_application.html", {
        "form": form,
        "application": application
    })  

@login_required
def delete_application(request, id):
    application = get_object_or_404(
        JobApplication,
        id=id,
        user=request.user
    )

    if request.method == "POST":
        application.delete()
        return redirect("application_list")

    return render(request, "applications/confirm_delete.html", {
        "application": application
    })       