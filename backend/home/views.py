from django.shortcuts import render
from .models import HeroContent, Service, ProcessStep, CtaBanner, PricingPlan, Stat, ShowcaseItem
from blog.models import Post

def index(request):
    context = {
        'hero': HeroContent.load(),
        'services': Service.objects.filter(is_active=True),
        'process_steps': ProcessStep.objects.filter(is_active=True),
        'pricing_plans': PricingPlan.objects.filter(is_active=True),
        'stats': Stat.objects.filter(is_active=True),
        'showcase_items': ShowcaseItem.objects.filter(is_active=True),
        'latest_posts': Post.objects.all()[:3],
        'cta': CtaBanner.load()
    }
    return render(request, 'home/home.html', context)

def privacy_policy(request):
    return render(request, 'home/privacy_policy.html')


