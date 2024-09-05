from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pet_images/')
    description = models.TextField()
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    adoption_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00) 
    sex = models.CharField(max_length=10, default='Unknown')  
    color = models.CharField(max_length=30, default='Unknown')
    size = models.CharField(max_length=20, default='Unknown')

    def __str__(self):
        return self.name

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    

class LearnMoreClick(models.Model):
    info = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.info
    
class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ${self.amount}"
    

class Adoption(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
