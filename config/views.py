from django.shortcuts import render, redirect
from django.views import View


class TopPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class FaqList(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'faq/list.html')


class FaqDetail(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'faq/detail.html')


class ContentsList(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contents/list.html')


class ContentsDetail(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contents/detail.html')


class InformationList(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'information/list.html')


class InformationDetail(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'information/detail.html')
