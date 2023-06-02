from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenge = {
    'january': 'Eat',
    'february': 'Sleep',
    'march': 'Concqour',
    'april': 'Repeat',
    'may':'Eat',
    'june':'Sleep',
    'july':'Concqour',
    'august':'Repeat',
    'september':'Eat', 
    'october':'Sleep',
    'november':'Concqour',
    'december':None
}

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())
    if(month < 1 or month > 12):
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)
    redirect_month = months[month-1]
    redirect_url = reverse("monthly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)

def monthly_challenges(request,month):
    try:
        challenge_text = monthly_challenge[month]
        response_data = f"<h1>{challenge_text}</h1>"
        response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
        return render(request, 'challenges/challenge.html',{
            'text': challenge_text,
            'month': month
        })
    except:
        response_data = render_to_string('404.html')
        return HttpResponseNotFound(response_data)
    
def home(request):
    months = list(monthly_challenge.keys())
    
    return render(request, 'challenges/index.html',{
        'months': months
    })
