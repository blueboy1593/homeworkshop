from django.shortcuts import render

# Create your views here.

def info(request):
    return render(request, 'info.html')


def student(request, stu_name):
    context={
        'stu_name' : stu_name,
    }
    return render(request, 'student.html', context)


def pushnumber(request):
    return render(request, 'pushnumber.html')


def pullnumber(request):
    num = request.GET.get('number')
    context = {
        'num' : num,
    }
    return render(request, 'pullnumber.html', context)