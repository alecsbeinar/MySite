from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView

from autos.forms import MakeForm
from autos.models import Make, Auto


class MainView(LoginRequiredMixin, View):
    def get(self, request):
        makes_count = Make.objects.count()
        autos = Auto.objects.all()
        context = {
            "makes_count": makes_count,
            "autos": autos
        }
        return render(request, "autos/main.html", context)

class MakeAll(View):
    def get(self, request):
        makes = Make.objects.all()
        context = {'makes': makes}
        return render(request, "autos/make_list.html", context)

class MakeCreate(View):
    success_url = reverse_lazy('autos:main')
    def get(self, request):
        form = MakeForm()
        context = {
            "form": form
        }
        return render(request, "autos/make_form.html", context)

    def post(self, request: HttpRequest):
        form = MakeForm(request.POST)
        if not form.is_valid():
            context = {
                "form": form
            }
            return render(request, "autos/make_form.html", context)
        form.save()
        return redirect(self.success_url)


class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:main')
    template = 'autos/make_form.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request: HttpRequest, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)
        form.save()
        return redirect(self.success_url)


class MakeDelete(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:main')
    template = 'autos/make_confirm_delete.html'
    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        context = {"make": make}
        return render(request, self.template, context)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy("autos:main")


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy("autos:main")


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy("autos:main")
