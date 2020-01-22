from django.shortcuts import render,redirect
from .models import TeacherInfo
from .forms import TeacherForm

def t_list(request):
    lists = TeacherInfo.objects.all()
    context = {'lists':lists}
    return render(request,'teacher/list.html',context)


def t_create(request):
    forms = TeacherForm()
    if request.method == 'POST':
        forms = TeacherForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('t_list')
    context = {'forms':forms}
    return render(request,'teacher/create.html',context)


def t_edit(request,t_id):
    t_obj = TeacherInfo.objects.get(id=t_id)
    forms = TeacherForm(instance=t_obj)
    if request.method == 'POST':
        forms = TeacherForm(request.POST,instance=t_obj)
        if forms.is_valid():
            forms.save()
            return redirect('t_list')
    context = {'forms':forms}
    return render( request,'teacher/edit.html',context )


def t_delete(request,t_id):
    t_obj = TeacherInfo.objects.get(id=t_id)
    if request.method == 'POST':
        t_obj.delete()
        return redirect('t_list')
    context ={'t_obj':t_obj}
    return render(request, 'teacher/delete_conf.html', context)


