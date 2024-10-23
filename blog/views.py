# mvioydosepipkomc
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Portfolio
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib import messages

def index(request):
    blog = Blog.objects.all()
    portfolio = Portfolio.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        sender_email = email 
        sender_password = 'mvioydosepipkomc'
        receiver_email = 'd08980476@gmail.com'  

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"{sender_email} Message"


        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(receiver_email, sender_password)

            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()

            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, "There was an error sending your message. Please try again.")

        return redirect('index')

    context = {
        "blogs": blog,
        "portfolios": portfolio
    }

    return render(request, 'index.html', context)

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog.html', {'blog': blog})

def portfolio_detail(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio})

def two(request):
    return render(request, '404.html')
