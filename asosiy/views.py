from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def salomlash(request):
    return HttpResponse("Salom, Dunyo!")

def salom(request):
    data = {"ism":"Islom",
            "ismlar":["Ali", "Javlon", "Bekzod", "Bahodir"]}
    return render(request, "salom.html", data)

def main(request):
    return render(request, "bosh_sahifa.html")

def talabalar(request):
    if request.method == 'POST':
        forma = TalabaForm(request.POST)
        if forma.is_valid():
            Talaba.objects.create(
                ism= forma.cleaned_data.get('name'),
                kurs= forma.cleaned_data.get('course'),
                kitoblar_soni= forma.cleaned_data.get('books'),
                bitiruvchi= forma.cleaned_data.get('graduate')
            )
        return redirect('/talabalar/')
    soz = request.GET.get('qidirish')
    if soz is None:
        st = Talaba.objects.all()
    else:
        st =Talaba.objects.filter(ism__contains=soz)
    data = {
        "forma": TalabaForm(),
        "talabalar": st}
    return render(request, "talabalar.html", data)

def mualliflar(request):
    if request.method == 'POST':
        authors = MuallifForm(request.POST)
        if authors.is_valid():
            Muallif.objects.create(
                ism = authors.cleaned_data.get('ism'),
                yosh= authors.cleaned_data.get('yosh'),
                tirik=authors.cleaned_data.get('tirik'),
                kitob_soni=authors.cleaned_data.get('kitob_soni'),
                jinsi=authors.cleaned_data.get('jinsi'),
                tugulgan_sana= authors.cleaned_data.get('tugulgan_sana')
            )
        return redirect('/mualliflar/')
    data={"mualliflar": Muallif.objects.all(),
          "authors": MuallifForm()}
    return render(request, "mualliflar.html", data)

def kitoblar(request):
    if request.method == 'POST':
        forma = KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/kitoblar/')
    soz = request.GET.get('qidirish')
    if soz is None:
        kt = Kitob.objects.all()
    else:
        kt = Kitob.objects.filter(nom__contains=soz)
    data = {"kitoblar": kt, "mualliflar": Muallif.objects.all(),
            "forma": KitobForm}
    return render(request, "kitoblar.html", data)

def talaba(request, son):
    if request.method == "POST":
        if request.POST.get('b') == 'on':
            bitiruvchi_qiymati = True
        else:
            bitiruvchi_qiymati = False
        Talaba.objects.filter(id=son).update(
            ism = request.POST.get('i'),
            kurs = request.POST.get('k'),
            kitoblar_soni = request.POST.get('k_s'),
            bitiruvchi = bitiruvchi_qiymati
        )
        return redirect('/talabalar/')
    data = {"talaba": Talaba.objects.get(id=son)}
    return render(request, "talaba.html", data)

def talaba_ochir(request, son):
    Talaba.objects.get(id=son).delete()
    return redirect("/talabalar/")

def kitob_ochir(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect("/kitoblar/")

def muallif(request, son):
    data={'muallif':Muallif.objects.get(id=son)}
    return render(request, 'muallif.html', data)

def records(request):
    data = {'records': Record.objects.all(),
            'forma': RecordForm}
    return render(request, 'records.html', data)

def admins(request):
    if request.method == 'POST':
        forma = AdminForm(request.POST)
        if forma.is_valid():
            Admin.objects.create(
                ism = forma.cleaned_data.get('ism'),
                ish_vaqti = forma.cleaned_data.get('ish_vaqti')
            )
        return redirect('/admins/')
    data= {'adminlar': Admin.objects.all(),
           'forma': AdminForm}
    return render(request, 'admins.html', data)
