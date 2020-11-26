from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db import transaction

from .forms import *
from .models import Schema, SchemaColumn


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('data_schemas')
                else:
                    return HttpResponse("disable account")
            else:
                return HttpResponse("invalid login")
    else:
        if request.user.is_authenticated:
            return redirect('data_schemas')

        form = LoginForm()
    return render(request, 'generator/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return render(request, 'generator/logout.html')


@login_required()
def data_schemas(request):
    schemas = Schema.objects.filter(owner=request.user)
    return render(request, 'generator/data_schemas.html', {'schemas': schemas})


# @login_required()
class SchemaCreate(CreateView):
    model = Schema
    template_name = 'generator/add_schema.html'
    form_class = SchemaForm
    seccess_url = None

    def get_context_data(self, **kwargs):
        data = super(SchemaCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['columns'] = SchemaColumnFormSet(self.request.POST)
        else:
            data['columns'] = SchemaColumnFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        columns = context['columns']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if columns.in_valid():
                columns.instance = self.object
                columns.save()
        return super(SchemaCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('generator:schemas')


# @login_required()
class SchemaUpdate(UpdateView):
    model = Schema
    template_name = 'generator/add_schema.html'
    form_class = SchemaForm
    seccess_url = None

    def get_context_data(self, **kwargs):
        data = super(SchemaUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['titles'] = SchemaColumnFormSet(self.request.POST, instance=self.object)
        else:
            data['titles'] = SchemaColumnFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        columns = context['columns']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if columns.in_valid():
                columns.instance = self.object
                columns.save()
        return super(SchemaUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('generator:schemas')
    


