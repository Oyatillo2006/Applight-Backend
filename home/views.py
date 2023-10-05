from django.shortcuts import render, redirect
from .models import About, Features, Team, Test, Questions, Message
def home(request):
    if request.POST:
        f_name = request.POST.get("full-name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Message.objects.create(full_name = f_name, email = email, subject = subject, message = message)

        return redirect("/")

    if len(Features.objects.all()) > 1:
        data = {
            "about": About.objects.all(),
            "left": Features.objects.all()[0::2],
            "right": Features.objects.all()[1::2],
            "team": Team.objects.all(),
            "test": Test.objects.all(),
            "questions": Questions.objects.all()
        }
    else:
        data = {
            "about": About.objects.all(),
            "team": Team.objects.all(),
            "test": Test.objects.all(),
            "questions": Questions.objects.all()
        }

    return render(request, "index.html", data)

