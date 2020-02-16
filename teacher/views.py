from django.shortcuts import render,redirect
from .models import TeacherInfo
from .forms import TeacherForm



from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import Context
from django.template.loader import get_template
from django.utils.html import escape
from xhtml2pdf import pisa
from io import StringIO, BytesIO
from django.contrib.auth.decorators import login_required


@login_required
def t_list(request):
    count =TeacherInfo.objects.all().count()
    lists = TeacherInfo.objects.all()
    context = {'lists':lists,'count':count}
    return render(request,'teacher/list.html',context)

@login_required
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


def getPdfPage(request):
    lists=TeacherInfo.objects.all()
    data={'lists':lists}
    template=get_template("newpdf.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    if not pdfPage.err:
        return HttpResponse(response.getvalue(),content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")