from django.shortcuts import render
from django.core.paginator import Paginator
from .models import EmailSubscription

# Create your views here.
def home(request):
    subscriptions_list = EmailSubscription.objects.all().order_by('-created_at')  # Order by most recent first
    paginator = Paginator(subscriptions_list, 10)  # Show 10 subscriptions per page

    page_number = request.GET.get('page')
    subscriptions = paginator.get_page(page_number)
    return render(request, 'home.html', {'subscriptions': subscriptions})
