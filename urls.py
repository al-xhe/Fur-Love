

from django.urls import path
from . import views
from .views import pet_detail
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import adopt_pet, adoption_success



urlpatterns = [
     path('', views.homePage, name='homePage'),  
    path('veterinary-services/', views.veterinary_services, name='veterinary_services'),
     path('adoption-process/', views.adoption_process, name='adoption_process'),
    path('volunteer/', views.volunteer, name='volunteer'),
      path('pet-rehabilitation/', views.pet_rehabilitation, name='pet_rehabilitation'),
    path('post-adoption-support/', views.post_adoption_support, name='post_adoption_support'),
    path('save-info/', views.save_info, name='save_info'),
    path('about/', views.aboutPage, name='aboutPage'),
     path('contact/', views.contactPage, name='contactPage'),
     path('adoption/', views.adoptionPage, name='adoptionPage'),
     path('informations/', views.informationsPage, name='informationsPage'),
     path('volunteer/', views.volunteerPage, name= 'volunteerPage' ),
      path('pet/<int:pk>/', pet_detail, name='pet_detail'),
       path('adopt/<int:pet_id>/', views.adopt_pet, name='adoptPet'),
    path('success/', TemplateView.as_view(template_name="success.html"), name='successPage'),
 path('donate/', views.donate_view, name='donate'),
 path('thank-you/', views.thank_you_view, name='thank_you'),
   path('adopt/<int:pet_id>/', adopt_pet, name='adopt_pet'),
    path('adopt-success/<int:pet_id>/', adoption_success, name='adoption_success'),
    path('care-for-your-friend/', views.care_for_your_friend, name='careForYourFriend'),
    path('success-stories/', views.success_stories, name='successStories'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

