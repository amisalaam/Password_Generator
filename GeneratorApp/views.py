from django.shortcuts import render,redirect
import random
import string

# Create your views here.

def home(request):
   return render(request,'home.html')


def generator(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.POST.get('length', 12))  # Default length is 12

    if request.POST.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.POST.get('specialcharacter'):
        special_characters = string.punctuation
        characters.extend(list(special_characters))
    if request.POST.get('number'):
        characters.extend(list('1234567890'))

    if request.method == 'POST' and 'generate' in request.POST:
        random_password = ''.join(random.choice(characters) for _ in range(length))
        context = {'password': random_password}
        return render(request, 'generator.html', context)

    return render(request, 'generator.html')


