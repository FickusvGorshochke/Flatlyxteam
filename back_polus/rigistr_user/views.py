from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.shortcuts import render


class Register(View):
    template_name = 'registartion/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
