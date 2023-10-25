from django.contrib.humanize.templatetags.humanize import naturaltime
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.utils import timezone
from datetime import timedelta
from django.utils.html import escape

from chat.models import Message


class Main(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'chat/main.html')

    def post(self, request: HttpRequest):
        mes = Message(text=request.POST['message'], owner=request.user)
        mes.save()
        return redirect(reverse('chat:main'))


class TalkMessages(LoginRequiredMixin, View):
    def get(self, request):
        Message.objects.filter(created_at__lt=timezone.now() - timedelta(minutes=20)).delete()
        messages = Message.objects.all().order_by("-created_at")[:10]
        results = []
        for message in messages:
            result = [escape(message.text), naturaltime(message.created_at)]
            results.append(result)

        return JsonResponse(results, safe=False)