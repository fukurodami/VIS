from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import MaterialForm

class MainView(View):
    def get(self, request):
        return render(request, "main.html")

class Entry(View):
    def get(self, request):
        return render(request, "entry.html")

    def post(self, request):
        if request.method == 'POST':
            form = MaterialForm(request.POST)
            print('1')
            if form.is_valid:
                try:
                    instance = form.save(commit=False)
                    print('3')
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
                    print('4')
                    return HttpResponseRedirect('/')
                    print('5')
                except:
                    form.add_error(None, 'Ошибка добавления')
        else:
            form = MaterialForm()
        return render(request, 'entry.html', {'form': form})


