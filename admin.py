from django.contrib import admin
from .models import Pet, Contact,Donation, Adoption
 




class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'breed', 'sex', 'color', 'size', 'adoption_fee')
    search_fields = ('name', 'breed', 'sex', 'color', 'size')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')  
    search_fields = ('full_name', 'email') 

class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'date')
    search_fields = ('name', 'email')
    list_filter = ('date',)
    ordering = ('-date',)

class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('pet', 'name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

# Register the model with the admin site
admin.site.register(Pet, PetAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Adoption, AdoptionAdmin)






