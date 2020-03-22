from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def shop(request):
    return render(request, 'shop/shop.html')

