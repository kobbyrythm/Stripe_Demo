from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from .models import Event,Company,Buyer,Seller

def index(request):
    return render(request, 'index.html')

def sucess(request):
    return render (request, 'sucess.html')


stripe.api_key = settings.STRIPE_PRIVATE_KEY

model = Event
template_name = 'index.html'
# pk_url_kwarg = 'id'


# def get_context_data(self, **kwargs):
#         context = super(checkout, self).get_context_data(**kwargs)
#         context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
#         return context 

# Creating a checkout session
def checkout (request):
   
    checkout_session = stripe.checkout.Session.create(
        line_items=[
                {
                    'price': 'price_1LLkdqGf400FY8MowjKqRYj0',
                    'quantity': 1,
                },
            ],
        mode='payment',
        success_url='http://127.0.0.1:8000/',
        cancel_url='http://127.0.0.1:8000/',
        
        )
    stripe.Account.create(
        type ='express',
        country = 'GB',
        
    )

    return redirect(checkout_session.url, code=303)


def payment (request,id):
    stripe.AccountLink.create(
    account="acct_1LMAerGg57F7dHyY",
    type="account_onboarding",
)


# Payout to seller
# def transfer (request,id):
#     transfer = stripe.Transfer.create(
#     amount= (stripe.Price/100)* 10
#     destination={{'acct_1LMAerGg57F7dHyY'}}"
# )
