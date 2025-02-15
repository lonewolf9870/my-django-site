from django.db import models

class Registration(models.Model):
    event = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.EmailField(default="abc@gmail.com")
    phone = models.CharField(max_length=15)
    teamname = models.CharField(max_length=100)
    teammates = models.TextField()
    collegename = models.CharField(max_length=100)
    transactionid = models.CharField(max_length=100)
    image = models.ImageField(upload_to='registration_images/')

    def __str__(self):
        return f"{self.name} - {self.event} - {self.transactionid}"


