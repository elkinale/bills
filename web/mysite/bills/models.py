# models.py
from django.db import models

class People(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Bills(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    event = models.ForeignKey(Events, on_delete=models.CASCADE, default=None)
    place = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Bill for {self.event.name} (Total: ${self.total})"

class Relations(models.Model):
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    bill = models.ForeignKey(Bills, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = [('person', 'bill')]  # Prevent duplicate entries

    def __str__(self):
        return f"{self.person.name} paid ${self.amount_paid} for {self.bill}"