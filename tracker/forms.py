from django import forms
from .models import Entry, CategoryOption, VrajLocation

class EntryForm(forms.ModelForm):
    # This field isn't in the database; it just catches the user's typed input
    new_option = forms.CharField(
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Or type a new option...'})
    )

    class Meta:
        model = Entry
        fields = ['some_text', 'category', 'time_start', 'time_stop', 'comments']
        widgets = {
            'time_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'time_stop': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the category dropdown optional so the form doesn't block if they type a new option
        self.fields['category'].required = False

class VrajLocationForm(forms.ModelForm):
    class Meta:
        model = VrajLocation
        fields = ['kha_paya_gya_tha', 'kis_jagah', 'time_kya_tha']
        widgets = {
            # Forces the datetime field to render as a visual calendar/time picker
            'time_kya_tha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }