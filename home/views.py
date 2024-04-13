from django.shortcuts import render
from .forms import ContactForm
from .models import PortfolioItem, Category, Post


# def home(request):
#     return render(request, 'home/home.html')

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can add a success message here
            return render(request, 'home/home.html')  # Replace 'success_url' with the URL name of your success page
    else:
        form = ContactForm()

    portfolio_items = PortfolioItem.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    return render(request, 'home/home.html',
                  {'form': form, 'portfolio_items': portfolio_items, 'categories': categories, 'posts': posts})

