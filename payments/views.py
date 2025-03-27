from django.shortcuts import render, redirect
from intasend import APIService
from decouple import config

def index(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        if not amount or float(amount) <= 0:
            return render(request, "index.html", {"error": "Invalid amount!"})

        # Authenticate with IntaSend
        service = APIService(
            token=config("private_key"),
            publishable_key=config("publishable_key"),
            test=True  # Use False for live mode
        )

        # Create a payment request
        response = service.payment_links.create(
            title='Donation',            
            amount=float(amount),
            currency="KES",
            email="customer@example.com",  # Optional
            description="Payment for services"
        )

        # Redirect to the IntaSend payment page
        payment_url = response.get("url")
        if payment_url:
            return redirect(payment_url)
        else:
            return render(request, "index.html", {"error": "Payment request failed."})

    return render(request, "index.html")
