from django.contrib.auth. models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.contrib.auth import logout
from django.template.response import TemplateResponse


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/sign/login/'


def logout_view(request):
    logout(request)
    return TemplateResponse(request,'logout.html')







