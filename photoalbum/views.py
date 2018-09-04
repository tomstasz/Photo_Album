from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View


class IndexView(View):

    def get(self, request):
        return TemplateResponse(request, 'photoalbum/index.html', {'message': 'Witaj świecie'})
