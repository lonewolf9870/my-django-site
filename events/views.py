from django.shortcuts import render, redirect
from .models import Registration
from django.contrib import messages

def index(request):
    return render(request, "events/index.html")

def events(request):
    return render(request, "events/events.html")


def success_page(request):
    return render(request,"events/success.html")

def register_event(request):
    if request.method == "POST":
        event_title = request.POST.get("game_name")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone_number")
        teamname = request.POST.get("team_name")
        collegename = request.POST.get("college_name")
        image = request.FILES.get("payment_image")
        teammates = request.POST.get("team_members") if event_title.lower() == "paper presentation" else ""
        transactionid = request.POST.get("transaction_id")

        errors = []
        if event_title.lower() == "paper presentation":
            num_teammates = len(teammates.split(",")) if teammates else 0
            if num_teammates < 1 or num_teammates > 3:
                errors.append("Paper Presentation requires 1 to 4 members in total.")

        # If there are errors, return to template with the modal open
        if errors:
            return render(request, "events/events.html", {
                "modal_open": True,  # Keep modal open only on errors
                "event_title": event_title,
                "name": name,
                "email": email,
                "phone": phone,
                "teamname": teamname,
                "collegename": collegename,
                "teammates": teammates,
                "transactionid": transactionid,
                "errors": errors
            })

        # Save registration
        Registration.objects.create(
            event=event_title,
            name=name,
            email=email,
            phone=phone,
            teamname=teamname,
            teammates=teammates,
            collegename=collegename,
            
            image=image
        )

        return redirect("success_page")

    return render(request, "events/events.html")
