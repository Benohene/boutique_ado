from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def checkout(request):
    """ A view to return the checkout page """
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse("products"))
    
    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NXaWNDdl1Qad2oJOO9CVnYKxqYmrHU6zwVFaO5I3qQ0pmk41lXReyc6l1eM8Yk28LLu7eO9oiXrwdmm00yr3af200cZiUuyEN',
        'client_secret': 'test client secret',
    }
    
    return render(request, template, context)
