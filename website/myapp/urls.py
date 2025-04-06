from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .forms import CustomSetPasswordForm



urlpatterns = [
    path('', views.Home , name='homepage'),
    path('about', views.About , name='aboutpage'),
    path('service/', views.ServiceProvided , name='servicepage'),
    path('service/<int:id>/',views.service_detail, name='service_detail'),
    path('account', views.Account , name='accountpage'),
    path('ac-repair', views.AcService , name='ac-servicepage'),
    path('fridge-repair', views.FridgeService , name='fridge-servicepage'),
    path('signin', views.SignIn , name='signinpage'),
    path('signup', views.SignUp , name='signuppage'),
    path('welcome', views.Welcome , name='welcomepage'),
    path('signout/', views.SignOut, name='signoutpage'),
    path('edit-profile/',views.EditProfile, name='editprofilepage'),
    path('booking/', views.BookService, name='bookingpage'),
    path('confirm/<int:booking_id>/', views.BookingConfirmation, name='booking_confirmation'),
    path('thank-you/',views.ThankYou, name='thank_you'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="myapp/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="myapp/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="myapp/password_reset_confirm.html",form_class = CustomSetPasswordForm),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="myapp/password_reset_complete.html"), name="password_reset_complete"),
    path('login_or_signup/', views.LoginOrSignup, name='login_or_signup'),
]
