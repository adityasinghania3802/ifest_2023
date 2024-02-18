import re
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

#from ..iFest_2021.models import Registration
from .models import *
import datetime

# Create your views here.

@login_required(login_url='login_page')
def iohome(request, Round):
    #q = Registration.filter(event='IOHunt')
    #if q.objects.get(userProfile=request.user) is None:
    #    return redirect('$iohunteventpage$')
    if request.method == "POST":
        try:
            player = Player.objects.get(userProfile=request.user, Round=Round)
            if player.status == 'E':
                return redirect('ended', Round=Round)
            else:
                try:
                    puzzle = Puzzle.objects.get(name='start', Round=Round)
                    return redirect('puzzle', Round=Round, slug=puzzle.link)
                except:
                    return redirect('puzzle', Round=Round, slug='start')
        except:
            now = datetime.datetime.now()
            player = Player(userProfile=request.user, status='S', startTime=now, Round=Round)
            player.save()
            try:
                puzzle = Puzzle.objects.get(name='start', Round=Round)
                return redirect('puzzle', Round=Round, slug=puzzle.link)
            except:
                return redirect('puzzle', Round=Round, slug='start')
    return render(request, 'iohome.html')


@login_required(login_url='login_page')
def puzzle(request, Round, slug):
    try:
        player = Player.objects.get(userProfile=request.user, Round=Round)
    except:
        return redirect('iohome', Round=Round)

    if player.status == 'NS':
        return redirect('iohome', Round=Round)
    if player.status == 'E':
        return redirect('ended', Round=Round)

    try:
        puzzle = Puzzle.objects.get(link=slug, Round=Round)
    except:
        return render(request, 'lost.html')

    if request.method == "POST":
        if str(request.POST['ans']).upper() == str(puzzle.Data['answer']).upper():
            now = datetime.datetime.now()
            if puzzle.name == 'end':
                player.endTime = now
                player.status = 'E'
                player.save()
                return redirect('ended', Round=Round)
            else:
                messages.success(request, "Correct Answer! You may go forward.")
                 #messages.info(request, puzzle.Data['hint'])
        else:
            messages.error(request, "Incorrect Answer. Try Again!")

    return render(request, 'puzzle.html', {'puzzle':puzzle})


def ended(request, Round):
    try:
        player = Player.objects.get(userProfile=request.user, Round=Round)
        return render(request, 'ended.html', {'time':player.timeTaken, 'round':Round})
    except:
        return render(request, 'ended.html', {'round':Round})


@staff_member_required
def results(request):
    return render(request, 'results.html')