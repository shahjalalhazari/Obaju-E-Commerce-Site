from django.db import models

# CONTACT MODEL
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {}".format(self.email, self.name)


# FAQ MODEL
class Faq(models.Model):
    question = models.CharField(max_length=120)
    answere = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}".format(self.question)