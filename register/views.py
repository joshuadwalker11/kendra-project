from django.views.generic.edit import FormView
from .forms import RegForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


def index(request):
    return HttpResponse("View: registration index")


def reg_view(request):
    context = {}
    context['form'] = RegForm
    return render(request, "reg.html", context)


class RegFormView(FormView):
    template_name = "reg.html"
    form_class = RegForm
    success_url = 'reg_complete'

    def form_valid(self, form):
        print(form.data)
        return super().form_valid(form)


def reg_complete(request):
    return HttpResponse("Registration complete!")
