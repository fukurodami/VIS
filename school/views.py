from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import MaterialForm, SerialForm
from .models import Material, SerialModel


class Entry(View):
    def get(self, request):
        form = MaterialForm(request.POST)
        return render(request, 'entry.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = MaterialForm(request.POST)
            if form.is_valid:
                try:
                    instance = form.save(commit=False)
                    instance.title = form.cleaned_data['title']
                    instance.category = form.cleaned_data['category']
                    instance.amount = form.cleaned_data['amount']
                    instance.document = form.cleaned_data['document']
                    instance.organization = form.cleaned_data['organization']
                    instance.price = form.cleaned_data['price']
                    instance.size = form.cleaned_data['size']
                    instance.width = form.cleaned_data['width']
                    instance.length = form.cleaned_data['length']
                    instance.height = form.cleaned_data['height']
                    instance.serial = form.cleaned_data['serial']
                    instance.note = form.cleaned_data['note']
                    instance.save()
                    return HttpResponseRedirect('/')
                except:
                    form.add_error(None, 'Ошибка добавления')
        else:
            form = MaterialForm()
        return render(request, 'entry.html', {'form': form})

class SerialView(View):
    def get(self, request, pk):
        serial = Material.objects.get(serial=pk)
        if SerialModel.objects.get(material=serial) != None:
            form = SerialModel.objects.get(material=serial)
        else:
            form = SerialForm(request.POST)

        return render(request, "serial.html", {'serial': serial, 'form': form})

    def post(self, request, pk):
        if request.method == 'POST':
            serial = Material.objects.get(serial=pk)
            form = SerialForm(request.POST)
            if form.is_valid:
                try:
                    print(1)
                    instance = form.save(commit=False)
                    print(serial.id)
                    instance.material = serial
                    print(3)
                    instance.view_material = form.cleaned_data['view_material']
                    print(4)
                    instance.numb_seral = form.cleaned_data['numb_seral']
                    instance.face = form.cleaned_data['face']
                    instance.lifetime = form.cleaned_data['lifetime']
                    instance.details = form.cleaned_data['details']
                    instance.transfer = form.cleaned_data['transfer']
                    instance.work = form.cleaned_data['work']
                    print(412)
                    instance.save()
                    print(3)
                    return HttpResponseRedirect('/')
                except:
                    form.add_error(None, 'Ошибка добавления')
        else:
            form = SerialForm()
        return render(request, "serial.html", {'serial': serial, 'form': form})

class MainView(View):
    def get(self, request):
        materials = Material.objects.all()
        return render(request, "main.html", {'materials': materials})


