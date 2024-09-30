from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404, render
from pregunkane.autoforms import FraseForm
import random
from django.shortcuts import redirect


def index(request):
    ultimasfrases = Frase.objects.order_by('-data')[:5]
    context = {'ultimasfrases': ultimasfrases}
    return render(request, 'pregunkane/index.html', context)

def fraseRandom(request):
    frases = list(Frase.objects.all())
    frase = random.choice(frases)
    return render(request,'pregunkane/frase.html',{'frase': frase})

def fraseRandomSFW(request):
    fras = []
    for frases in Frase.objects.all():
        addeable = True
        for tag in frases.Tag.all():
            if tag.NSFW is True:
                addeable = False
        if addeable is True:
            fras.append(frases)

    frase = random.choice(fras)
    return render(request,'pregunkane/frase.html',{'frase': frase})


def detail(request,frase_id):
    try:
        frase = Frase.objects.get(pk=frase_id)
    except Frase.DoesNotExist:
        raise Http404("Frase no existe")
    return render(request,'pregunkane/frase.html', {'frase':frase})

def addfrase(request):
    if request.method =='POST':
        form = FraseForm(request.POST)
        if form.is_valid():
            frase = form.save()
            return redirect('detail',frase.id)
    else:
        form = FraseForm()
        return render(request,'pregunkane/frase_create.html',{'form': form})

def home(request):
    return render(request, 'pregunkane/home.html')


def fraseNom(request,nom):
    frase = []
    name=nom.lower()
    for names in User.objects.all():
        if names.name.lower() == name:
            name = names.name

    for frases in Frase.objects.all():
        print(frases.Dicho.name == name)
        if frases.Dicho.name == name:
            frase.append(frases)

    print(frase)

    context = {'frase': frase}
    return render(request, 'pregunkane/frases.html', context)
#Por terminar tienen que tener una vista___________

def addTag(request,frase_id,nomTag):
    try:
        frase = Frase.objects.get(pk=frase_id)
        tag = Tag.objects.get(TNom = nomTag)
        print(frase)
        frase.Tag.add(tag)
        frase.save()
    except Frase.DoesNotExist:
        raise Http404("Frase no existe")
    except Tag.DoesNotExist:
        raise Http404("Tag no existe")
    return render(request,'pregunkane/frase.html', {'frase':frase})

# Solo funciones_______

def removeTag(request,frase_id,nomTag):
    try:
        frase = Frase.objects.get(pk=frase_id)
        tag = Tag.objects.get(TNom = nomTag)
        print(frase)
        frase.Tag.remove(tag)
        frase.save()
    except Frase.DoesNotExist:
        raise Http404("Frase no existe")
    except Tag.DoesNotExist:
        raise Http404("Tag no existe")
    return render(request,'pregunkane/frase.html', {'frase':frase})


