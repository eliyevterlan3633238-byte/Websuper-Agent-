from django.shortcuts import render
from .models import TeamMember, Value, AboutSection

def index(request):
    team = TeamMember.objects.filter(is_active=True)
    values = Value.objects.filter(is_active=True)
    about_section = AboutSection.load()
    return render(request, 'about/about.html', {
        'team': team,
        'values': values,
        'about': about_section
    })
