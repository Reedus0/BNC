from django.shortcuts import render
from .forms import ReviewForm

# Create your views here.

def contacts(request):
    return render(request, 'index/contacts.html')

def about(request):
    return render(request, 'index/about.html')

def work(request):
    return render(request, 'index/work.html')

def experts(request):
    return render(request, 'index/experts.html')

def services(request):
    return render(request, 'index/services.html')

def review(request):
    form = ReviewForm()
    if request.method == 'POST':
        print(request.POST)
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form}
    return render(request, 'index/review.html', context)
