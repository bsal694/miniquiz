from django.core.mail import send_mail
from accounts.models import Account
from django.conf import settings
import random,time

def send_otp_via_mail(email):
    subject='Your account Verification Email'
    otp=random.randint(1000,9999)
    email_from=settings.EMAIL_HOST_USER
    message=f'your otp is {otp}'
    try:
        send_mail(subject,message,email_from,[email])
        print("hi")
        user_obj=Account.objects.get(email=email)
        user_obj.otp=otp
        user_obj.save()
        return otp
    except:
        print("errors")
