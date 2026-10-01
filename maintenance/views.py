from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from .models import MaintenanceRequest
from .forms import RegisterForm, RequestForm


# Create your views here.

#home
def home(request):
    return render(request, 'home.html')

#Register
def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request,user)
        return redirect('home')
    return render(request, 'register.html', {'form':form})


#Login
def user_login(request):
    form = AuthenticationForm(request, data = request.POST or None)

    if form.is_valid():
        login(request,form.get_user())
        return redirect('home')
    return render(request, 'login.html', {'form':form})


#logout
@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


#SUBMIT REQUEST
@login_required
def submit_request(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.user = request.user
        obj.save()
        return redirect('my_requests')
    return render(request, 'request_Form.html', {'form':form})

#display and search
@login_required
def my_requests(request):
    requests = MaintenanceRequest.objects.filter(user=request.user)

    category = request.GET.get('category')
    priority = request.GET.get('priority')
    status = request.GET.get('status')

    if category:
        requests = requests.filter(category=category)
    if priority:
        requests = requests.filter(priority=priority)
    if status:
        requests = requests.filter(status=status)

    return render(request, 'my_requests.html', {'requests':requests})

#update
@login_required
def edit_request(request, id):
    obj = get_object_or_404(
        MaintenanceRequest, id=id, user=request.user)

    form = RequestForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('my_requests')
    return render(request, 'edit_request.html', {'form':form})

#delete
@login_required
def delete_request(request, id):
    obj = get_object_or_404(MaintenanceRequest, id=id, user=request.user)
    if request.method == 'POST':
        obj.delete()

    return redirect('my_requests')

#staff
def is_staff(user):
    return user.is_staff

#staff page
@login_required
@user_passes_test(is_staff)
def staff_requests(request):
    requests = MaintenanceRequest.objects.all()

    if request.method == 'POST':
        obj = get_object_or_404(MaintenanceRequest, id = request.POST['id'])
        obj.status = request.POST['status']
        obj.save()
        return redirect('staff_requests')
    return render(request, 'staff_requests.html',{'requests': requests})








