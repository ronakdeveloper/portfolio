from django.shortcuts import render
from .models import ContactMessage
from django.http import HttpResponse

def IndexPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Save the form data to the database using the ContactMessage model
        contact_message = ContactMessage.objects.create(name=name, email=email, message=message)
        
          # Render a simple thank you message
        return render(request, 'index.html', {'thank_you_message': 'Thank you for your message!'})
    else:
        return render(request, 'index.html')