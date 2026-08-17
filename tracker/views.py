from django.shortcuts import render, redirect
from .forms import EntryForm, VrajLocationForm
from .models import CategoryOption, VrajLocation, Entry

def landing_view(request):
    return render(request, 'tracker/landing.html')

def home_view(request):
    all_entries = Entry.objects.all().order_by('-time_start')

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            typed_option = form.cleaned_data.get('new_option')
            
            if typed_option:
                new_cat, created = CategoryOption.objects.get_or_create(name=typed_option)
                entry.category = new_cat
            elif not entry.category:
                form.add_error('category', 'Select an option or type a new one.')
                return render(request, 'tracker/index.html', {'form': form, 'entries': all_entries})

            entry.save()
            
            # 1. Sends you straight to the "Vraj kha h" page after hitting submit
            return redirect('vraj_kha_h') 
    else:
        form = EntryForm()

    return render(request, 'tracker/index.html', {'form': form, 'entries': all_entries})

def vraj_kha_h_view(request):
    # Sorts by the start time, newest dates first
    all_entries = Entry.objects.all().order_by('-time_start')

    return render(request, 'tracker/vraj_kha_h.html', {'records': all_entries})