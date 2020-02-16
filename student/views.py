from django.shortcuts import render,redirect
from .models import StudentDetailsInfo
from .forms import StudentInfoForm,StudentDetailForm,StudentSearchForm
from django.contrib.auth.decorators import login_required



from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import Context
from django.template.loader import get_template
from django.utils.html import escape
from xhtml2pdf import pisa
from io import StringIO, BytesIO

from django.contrib.auth.decorators import login_required

def getPdfPage(request,roll_no):
    lists = StudentDetailsInfo.objects.get(id=roll_no)
    data={'lists':lists}
    template=get_template("pdf.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(),content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")




@login_required
def s_search(request):
    forms = StudentSearchForm()
    std_class = request.GET.get('student_class',None)
    std_roll = request.GET.get('roll',None)
    session = request.GET.get('session',None)

    if std_class:
       students = StudentDetailsInfo.objects.filter(std_class__id=std_class)
       if std_roll:
            students = students.filter(roll_no=std_roll)
       if session:
            students = students.filter(std_session=session)
            context = {'forms': forms,'students':students}
            return render(request, 'student/search.html', context)


    context = {'forms': forms}
    return render(request,'student/search.html',context)

@login_required
def s_list(request):
    lists = StudentDetailsInfo.objects.all()
    context = {'lists':lists}
    return render(request,'student/list.html',context)


def s_detail(request,roll_no):
    student_obj = StudentDetailsInfo.objects.get(id=roll_no)
    context = {'student': student_obj}
    return render(request,'student/detail.html',context)

@login_required
def s_create(request):
    form1 = StudentInfoForm()
    form2 = StudentDetailForm()
    if request.method == 'POST':
        form1 = StudentInfoForm(request.POST or None,request.FILES)
        form2 = StudentDetailForm(request.POST or None,request.FILES)
        if form1.is_valid() & form2.is_valid():
            std_obj = form1.save()
            std_detail = form2.save(commit=False)
            std_detail.student =  std_obj
            std_detail.save()
            return redirect('s_search')


    context = { 'form1':form1,'form2':form2 }
    return render(request,'student/create.html',context)


def s_edit(request,roll_no):
    std_detail = StudentDetailsInfo.objects.get(id=roll_no)
    std_info = std_detail.student

    form1 = StudentInfoForm(request.POST or None,instance=std_info)
    form2 = StudentDetailForm(request.POST or None,instance=std_detail)

    if request.method == 'POST':
        if form1.is_valid() & form2.is_valid():
            std_obj = form1.save()
            std_detail = form2.save(commit=False)
            std_detail.student =  std_obj
            std_detail.save()
#this is ok =>  return HttpResponseRedirect("/student/detail/{id}/".format(id=std_detail.id))
            return redirect('s_detail' ,roll_no = std_detail.id )

    context = { 'form1':form1,'form2':form2 }
    return render(request,'student/edit.html',context)


def s_delete(request,s_id):
    s_obj = StudentDetailsInfo.objects.get(id=s_id)
    if request.method == 'POST':
        s_obj.delete()
        return redirect('s_search')

    context ={'s_obj':s_obj}
    return render(request, 'student/delete_conf.html', context)
