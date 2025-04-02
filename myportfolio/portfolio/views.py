# views.py
from django.shortcuts import render
from .models import Resume, Project


def index(request):
    resumes = Resume.objects.all()  # Get all resumes
    # projects = Project.objects.all()
    projects = Project.objects.prefetch_related('images').all()
    return render(request, 'portfolio/index.html', {'resumes': resumes, "projects": projects})
# portfolio/views.py
from django.http import HttpResponse, Http404
from .models import Resume
import os

def download_cv(request, resume_id):
    try:
        # Get the resume object from the database
        resume = Resume.objects.get(id=resume_id)

        # Get the file path from the FileField
        file_path = resume.file.path

        # Check if the file exists
        if not os.path.exists(file_path):
            raise Http404("File not found.")

        # Open the file and serve it as a response
        with open(file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{resume.name}.pdf"'
            return response
    except Resume.DoesNotExist:
        raise Http404("Resume not found.")




from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Remove this if using a CSRF token
def contact_form(request):
    if request.method == "POST":
        data = json.loads(request.body)
        
        name = data.get("name")
        email = data.get("email")
        subject = data.get("subject")
        message = data.get("message")

        if not name or not email or not subject or not message:
            return JsonResponse({"status": "error", "message": "All fields are required"}, status=400)

        # Sending Email
        send_mail(
            subject=f"Contact Form: {subject}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email="your-email@gmail.com",  # Replace with your email
            recipient_list=["namandoshi459@gmail.com"],  # Your email
        )

        return JsonResponse({"status": "success", "message": "Your message has been sent!"})

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


