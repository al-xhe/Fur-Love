from django.shortcuts import render,redirect ,get_object_or_404
from .models import Pet
from .forms import ContactForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import LearnMoreClick
from .models import Donation
from .forms import DonationForm
from .models import  Adoption
from .forms import AdoptionForm



def homePage(request):
    return render(request, 'home.html')

def adoption_process(request):
    learn_more_clicks = LearnMoreClick.objects.all()  
    return render(request, 'adoption_process.html', {'learn_more_clicks': learn_more_clicks})

def veterinary_services(request):
    return render(request, 'veterinary_services.html')

def volunteer(request):
    return render(request, 'volunteer.html')

def pet_rehabilitation(request):
    return render(request, 'pet_rehabilitation.html')

def donate_view(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})


def thank_you_view(request):
    return render(request, 'thank_you.html')


def post_adoption_support(request):
    return render(request, 'post_adoption_support.html')


def save_info(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            info = data.get('info')
            LearnMoreClick.objects.create(info=info)  # Save to the database
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'error': str(e)})
    return JsonResponse({'status': 'error', 'error': 'Invalid request method'})

def aboutPage(request):
    return render(request, 'about.html')

def adoptionPage(request):
    pets = Pet.objects.all()
    return render(request, 'adoption.html', {'pets': pets})
   
def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet-detail.html', {'pet': pet})

def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'adopt_pet.html', {'pet': pet})

def informationsPage(request):
    return render(request, 'informations.html')

def volunteerPage(request):
    return render(request, 'volunteer.html')

def contactPage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the form data to the database
            return redirect('successPage')  # Redirect to a success page after saving
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def registerUser(request):
    if request.method == 'POST':
        pass
    return render(request, 'register.html')

def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            adoption = Adoption(
                pet=pet,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            adoption.save()
            
            return redirect('adoption_success', pet_id=pet.id)
    else:
        form = AdoptionForm()

    return render(request, 'adopt_pet.html', {'pet': pet, 'form': form})

def adoption_success(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'adoption_success.html', {'pet': pet})

def care_for_your_friend(request):
    return render(request, 'care_for_your_friend.html')

def success_stories(request):
    return render(request, 'success_stories.html')