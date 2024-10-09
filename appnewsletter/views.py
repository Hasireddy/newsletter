from django.shortcuts import render,HttpResponse

from django.contrib import messages

from .forms import EmailForm
from . models import NewsLetterEmail

# Create your views here.

def home(request):
    return render(request,"home.html")


# def news_letter(request):
#      form = EmailForm()
#      return render(request,"news.html",{"news_form":form})


def news_letter(request):
    if request.method == "POST":
        action = request.POST.get("action")
        email = request.POST.get("userEmail")
        
        #if 'subscribe' in request.POST:
        # add the user email in database
        if action == "subscribe":
            form = EmailForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,f"successfully subscribed {email}")
            else:
               messages.error(request,"Invalid Email address")
        #if 'unsubscribe' in request.POST:
        # remove the user email from database    
        elif action == "unsubscribe":
            try:
                subscriber = NewsLetterEmail.objects.get(userEmail = email)
                subscriber.delete()
                messages.success(request, f'Successfully unsubscribed: {email}')
                
            except NewsLetterEmail.DoesNotExist:
                 messages.error(request, 'Email not found. Please check and try again.')
                 
    form = EmailForm()
    return render(request,"news.html",{"news_form":form})
            
        
            