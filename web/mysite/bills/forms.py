# forms.py
from django import forms
from .models import People, Events, Bills, Relations
from dal import autocomplete

class UpdateForm(forms.Form):
    # People fields
    person_name = forms.CharField(
        label="Person Name",
        max_length=100,
        help_text="Enter the name of the person."
    )

    # Relations fields
    amount_paid = forms.DecimalField(
        label="Amount Paid",
        max_digits=10,
        decimal_places=2,
        help_text="Enter the amount paid by the person for this bill."
    )

    def save(self):
        # Create or get Person
        person, _ = People.objects.get_or_create(
            name=self.cleaned_data['person_name']
        )

        # Create or get Event
        event, _ = Events.objects.get_or_create(
            name=self.cleaned_data['event_name']
        )

        # Create Bill
        bill = Bills.objects.create(
            total=self.cleaned_data['total'],
            event=event,
            place=self.cleaned_data.get('place'),
            date=self.cleaned_data.get('date'),
        )

        # Create Relation
        relation = Relations.objects.create(
            person=person,
            bill=bill,
            amount_paid=self.cleaned_data['amount_paid'],
        )

        return bill  # Return the created bill (optional)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class BillForm(forms.Form):
    # Bills fields
    total = forms.DecimalField(
        label="Total Amount",
        max_digits=10,
        decimal_places=2,
        help_text="Enter the total amount for the bill."
    )
    place = forms.CharField(
        label="Place (Optional)",
        max_length=100,
        required=False,
        help_text="Enter the place where the bill occurred."
    )
    date = forms.DateField(
        label="Date (Optional)",
        required=False,
        help_text="Enter the date of the bill (YYYY-MM-DD).",
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    # Events fields
    event_name = forms.CharField(
        label="Event Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control select2-enable',  # Custom class for JavaScript
            'placeholder': 'Search or create an event...',
            'tags': True, 
            'allowClear': True, 
        })
    )

    def save(self):
        # Create or get Event
        event, _ = Events.objects.get_or_create(
            name=self.cleaned_data['event_name']
        )

        # Create Bill
        bill = Bills.objects.create(
            total=self.cleaned_data['total'],
            event=event,
            place=self.cleaned_data.get('place'),
            date=self.cleaned_data.get('date'),
        )

        return bill  # Return the created bill (optional)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'event_name' : continue
            self.fields[field].widget.attrs.update({'class': 'form-control'})

