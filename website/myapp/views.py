from django.shortcuts import render , redirect , reverse , get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from . forms import MyRegFrm
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking 
from django.core.mail import send_mail
from django.conf import settings
from .models import Service


# Create your views here.

def Home(request):
    services = Service.objects.all() 
    return render(request,'myapp/index.html', {'services': services})

def About(request):
    return render(request,'myapp/about.html')

def ServiceProvided(request):
    services = Service.objects.all() 
    return render(request, 'myapp/service.html', {'services': services})

def service_detail(request, id):
    service = get_object_or_404(Service, id=id)

    # Define templates based on service name
    template_map = {
        "AC Service": "myapp/ac-repair.html",
        "Fridge Service": "myapp/fridge-repair.html",
    }

    # Use specific template or fallback to default
    template_name = template_map.get(service.name, "myapp/service.html")

    return render(request, template_name, {"service": service})

def Account(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
        return render(request, 'myapp/account.html', {'bookings': bookings})
    else:
        return redirect('/welcome')

def AcService(request):
    return render(request,'myapp/ac-repair.html')

def FridgeService(request):
    return render(request,'myapp/fridge-repair.html')

def SignIn(request):
    if request.POST:
        form=AuthenticationForm(request=request , data= request.POST)
        if form.is_valid():
          uname=form.cleaned_data['username']
          upass=form.cleaned_data['password']
          user=authenticate(username = uname , password = upass)
          if user is not None:
            login(request , user)
            return redirect('/account')        
    else:
        form=AuthenticationForm()
    context = {"form": form}
    return render(request,'myapp/signin.html' , context)

def SignUp(request):
    if request.POST:
        form=MyRegFrm(data=request.POST)
        if form.is_valid:
            try:
                form.save()
                messages.success(request, 'You have Been Sucessfully Registered')   
            except Exception as e:
                messages.error(request, 'Your registration is not successfull')   
    else:
        form=MyRegFrm()
    context={'frm':form}
    return render(request, 'myapp/signup.html', context)

def Welcome(request):
    return render(request,'myapp/welcome.html')

def SignOut(request):
    logout(request)
    return redirect('/welcome')

@login_required
def EditProfile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account') 
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'myapp/edit_profile.html', {'form': form})


@login_required(login_url='/login_or_signup')
def BookService(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.full_name = request.POST.get("full_name")
            booking.email = request.POST.get("email")
            booking.phone = request.POST.get("phone")
            booking.save()
            return redirect(reverse('booking_confirmation', args=[booking.id]))
    else:
        form = BookingForm(initial={
            'full_name': f"{request.user.first_name} {request.user.last_name}",
            'email': request.user.email,
            'phone': request.user.mobile,
        })
    
    return render(request, 'myapp/booking.html', {'form': form})


@login_required
def BookingConfirmation(request, booking_id):
    booking = Booking.objects.get(id=booking_id, user=request.user )

    if request.method == "POST":
        booking.confirmed = True
        booking.save()

        subject = "Booking Confirmation"
        message = f"""
Thank you for your submission. Our service engineer will call you soon.

Name: {request.user.first_name} {request.user.last_name}
Phone: {request.user.mobile}
Email: {request.user.email}
Address: {request.user.city_town_village}, {request.user.street_name}, {request.user.pin_code}
City / Town / Village: {request.user.city_town_village}
Booking On: {booking.booking_date}
Service Type: {booking.service_type}

Best Regards,  
Mr. Cool
""".strip()

        from_email = settings.EMAIL_HOST_USER
        recipient_list = [booking.email] 

        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            print(f"Email sending failed: {e}")

        return redirect("thank_you")

    return render(request, "myapp/booking_confirmation.html", {"booking": booking})


def ThankYou(request):
    return render(request,'myapp/thanks.html')

def LoginOrSignup(request):
    return render(request, "myapp/login_or_signup.html")

