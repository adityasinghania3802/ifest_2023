from django.shortcuts import render, redirect
from .models import Question, UserAnswer
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import datetime

from django.http import HttpResponse

from django.contrib import messages


@login_required(login_url='login_page')
def base(request):
    flag = 1
    if(UserAnswer.objects.filter(user = request.user).exists()):
        p = UserAnswer.objects.get(user = request.user)
        if(p.status == 'E'):
            print(p.score)
            html = "<html><body>quiz already given</body></html>"
            messages.error(request, 'quiz already given')
            flag = 0
    context = {
        "flag":flag
    }
    return render(request , "homeganith.html" , context)


@login_required(login_url='login_page')
def start_quiz(request):
    question = Question.objects.all()[0]
    if request.method == "POST":

        player = UserAnswer.objects.filter(user=request.user).exists()
        print("in   ")
        chance = 4
        if(not player):
            now = datetime.datetime.now()
            p = UserAnswer(user=request.user, status='S', score=0 , chance = 4 , startTime = now)
            p.save()
        else:
            p = UserAnswer.objects.get(user = request.user)
            if(p.status == 'E'):
                print(p.score)
                html = "<html><body>quiz already given</body></html>"
                messages.error(request, 'quiz already given')
                return redirect('/igan/base')


        # if player.status == 'E':
        #     return render(request , '<h1> quiz ended </h1>')

    return render(request, 'question.html', {'question': question , 'chance':chance})

@login_required(login_url='login_page')
def next_question(request, question_id):
    question = Question.objects.get(question_id=question_id)
    user = request.user
    # print(user.username)

    # print(len(UserAnswer.objects.all()))

    user_answer_obj = UserAnswer.objects.get(user=user)

    if request.method == 'POST':
        chances = user_answer_obj.chance

        if user_answer_obj.status == 'E':
            html = "<html><body>quiz already over for this user</body></html>"
            messages.error(request, 'quiz already given')
            return redirect('/igan/base')

        if( chances < 0):
            now = datetime.datetime.now()
            user_answer_obj.endTime = now
            user_answer_obj.status = 'E'
            user_answer_obj.save()
            html = "<html><body>quiz over enough chances taken</body></html>"
            messages.error(request, 'quiz over enough chances taken')
            return redirect('/igan/base')

        user_answer = request.POST.get('answer')
        correct_answer = question.correct_answer
        is_correct = user_answer == correct_answer
        if(not user_answer_obj.just_answered.filter(question_id = question_id).exists()):

            if(is_correct):

                user_answer_obj.answered.add(Question.objects.get(question_id= question_id))
                user_answer_obj.just_answered.add(Question.objects.get(question_id= question_id))
                user_answer_obj.score = len(user_answer_obj.answered.all())
                print(user_answer_obj.score)
                user_answer_obj.save()

            else:
                user_answer_obj.just_answered.add(Question.objects.get(question_id= question_id))
                chances = user_answer_obj.chance
                chances -= 1
                user_answer_obj.chance = chances
                user_answer_obj.save()

                #print(chances)
                if( chances < 0):
                    now = datetime.datetime.now()
                    user_answer_obj.endTime = now
                    user_answer_obj.status = 'E';
                    user_answer_obj.save()
                    messages.error(request, 'quiz over enough chances taken')
                    return redirect('/igan/base')
                user_answer_obj.answered.add(Question.objects.get(question_id= question_id))
                user_answer_obj.just_answered.add(Question.objects.get(question_id= question_id))
                user_answer_obj.score = len(user_answer_obj.answered.all())
                print(user_answer_obj.score)
                user_answer_obj.save()


        if question_id < 40:

            next_question_id = Question.objects.filter(question_id__gt = question_id).first().question_id
            next_question = Question.objects.get( question_id = next_question_id)
            return render(request, 'question.html', {'question': next_question , "chance":chances})
        else:
            now = datetime.datetime.now()
            user_answer_obj.endTime = now
            user_answer_obj.status = 'E';
            user_answer_obj.save()
            messages.error(request, 'quiz over for this user')
            return redirect('/igan/base')

    return render(request, 'question.html', {'question': question , "chance":chances})


@staff_member_required()
def endquiz(request):
    alluser = UserAnswer.objects.all()
    for users in alluser:
        if(users.status != "E"):
            users.status = 'E'
            now = datetime.datetime.now()
            users.endTime = now
            users.save()
    return render(request , 'home.html')


