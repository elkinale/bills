from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from bills.models import Events, People, Bills, Relations
from bills.forms import BillForm, UpdateForm
from dal import autocomplete
# from django.db.models import Q

class MainView(View, LoginRequiredMixin):
    def get(self, request):
        ev_list = Events.objects.all()
        
        strval = request.GET.get("search", False)
        if strval:
            # ev_list = Events.objects.filter(Q(name__icontains=strval) | 
            #                                 Q(text__icontains=strval)) #In case to have more filters
            ev_list = Events.objects.filter(name__icontains=strval).select_related().distinct()[:10]
        else :
            ev_list = Events.objects.all()[:10]
        
        ctx = {'ev_list': ev_list}
        return render(request, 'bills/main.html', ctx)
    
class AddBillView(View):
    model = Events
    template_name = 'bills/create.html'
    def get(self, request):
        form = BillForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = BillForm(request.POST)
        ctx = {'form': form}

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('bills:main'))
        
        return render(request, self.template_name, ctx)
    
class EventAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Events.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
    
    def get_results(self, context):
        return [
            {
                'id': event.id,
                'text': event.name,
            }
            for event in context['object_list']
        ]

    
class DetailBillView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/main.html', context)
    
class UpdateBillView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/main.html', context)
    
class DeleteBillView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
        }
        return render(request, 'home/main.html', context)
    
    

