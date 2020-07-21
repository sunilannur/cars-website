from .models import *
from django.shortcuts import render, redirect, reverse


def user_check(request):
    try:
        check_user = Car.objects.get(user=request.user)
        print("222222222222",check_user)

    except Exception as e:
        print("==============", e)
        return redirect(reverse('website:dashboard'))
