from django.shortcuts import render, redirect
from .models import Square
from django.contrib import messages
import math
# Create your views here.
def index(request):
    list_1 = []
    if not Square.objects.get(id=1):
        for i in range(1,82):
            new_square =Square.objects.create(value=0)


    context = {
        "listhelper" : Square.objects.all()
    }
    return render (request,'sudoku/index.html', context)
def change(request,id):
    request.session['this_id']=id
    return render(request,'sudoku/change.html')
def clear(request):
    all_square = Square.objects.all()
    for i in all_square:
        i.value = 0
        i.save()
    return redirect('/')
def changeval(request,id):
    print id
    response = Square.objects.changeval(request.POST)
    if not response['status']:
        for error in response['error']:
            messages.error(request, error)

        return redirect('/')
    change_square = Square.objects.get(id=id)
    change_square.value = request.POST['new_val']
    change_square.save()
    return redirect('/')
def solve(request):
    all_square = Square.objects.all()
    value_list = []
    for i in all_square:
        value_list.append(i.value)

    testcount = 0
    for i in range(0,len(value_list)):
        if value_list[i] == 0:
            testcount += 1
    print testcount
    solve_dict = {}
    for i in range(0,len(value_list)):
        mini_list = []
        for x in range(0,len(value_list)):
            if i%9 == x%9 and value_list[x] != 0:
                mini_list.append(value_list[x])
        solve_dict[i]=mini_list

    for i in range(0,len(value_list)):
        mini_list_1 = []
        if i<9:
            for x in range(0,9):
                if value_list[x]!= 0:
                    mini_list_1.append(value_list[x])
        elif i<18:
            for x in range(9,18):
                if value_list[x]!= 0:
                    mini_list_1.append(value_list[x])
        elif i<27:
            for x in range(18,27):
                if value_list[x]!= 0:
                    mini_list_1.append(value_list[x])
        elif i<36:
            for x in range(27,36):
                if value_list[x]!= 0:
                    mini_list_1.append(value_list[x])
        elif i<45:
            for x in range(36,45):
                if value_list[x]!= 0:
                    mini_list_1.append(value_list[x])
        elif i<54:
            for x in range(45,54):
                if value_list[x]!= 0:
                    mini_list_1.append(value_list[x])
        elif i<63:
            for x in range(54,63):
                if value_list[x]!= 0:
                    mini_list_1.append(value_list[x])
        elif i <72:
            for x in range(63,72):
                if value_list[x]!=0:
                    mini_list_1.append(value_list[x])
        else:
            for x in range(72,81):
                if value_list[x]!=0:
                    mini_list_1.append(value_list[x])
        solve_dict[i] = solve_dict[i]+mini_list_1
    for x in range(0,len(value_list)):
        j = 0
        k=0
        if x%9<3:
            j = 3
        elif x%9<6:
            j = 6
        else:
            j = 9
        if int(math.floor(x/9)) < 3:
            k = 3
        elif int(math.floor(x/9)) < 6:
            k = 6
        else:
            k = 9

        mini_list2= []
        for i in range(k-3,k):

            for y in range(i*9+j-3,i*9+j):
                if solve_dict[y]!=0:
                    mini_list2.append(value_list[y])
        solve_dict[x] = solve_dict[x]+mini_list2
    for key in solve_dict:
        dup_list= []
        for x in solve_dict[key]:
            if x not in dup_list:
                if x !=0:
                    dup_list.append(x)
        solve_dict[key] = dup_list

    for i in range(0,len(value_list)):
        if value_list[i]==0:
            if len(solve_dict[i]) == 8:
                for x in (range(1,10)):
                    if x not in solve_dict[i]:
                        value_list[i]=x

    testcount2 = 0
    for i in range(0,len(value_list)):
        if value_list[i]==0:
            testcount2 +=1
    if testcount2 == testcount:
        errors = []
        errors.append("Sudoku solve unsuccessful. Please confirm that you entered the puzzle correctly and that the puzzle is designated as 'easy'")
        for error in errors:
            messages.error(request, error)
            return redirect('/')
    for i in range(0,len(value_list)):
        thing = i+1
        this_square = Square.objects.get(id = thing)
        this_square.value = value_list[i]
        this_square.save()
    all_square=Square.objects.all()
    for square in all_square:
        if square.value == 0:
            return redirect('/solve')
    return redirect('/')
