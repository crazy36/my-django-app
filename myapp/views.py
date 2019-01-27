
# import csv
# from myapp.models import Employee
from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# from myapp.functions.functions import handle_uploaded_file
from myapp.form import StudentForm


# Create your views here.

#from django.http import HttpResponse
#from django.views.decorators.http import require_http_methods

#def hello(request):
    #return HttpResponse("<h2>Hello! Welcome to Django!</h2>")

# def index(request):
#     student=StudentForm()
#     template=loader.get_template('index.html') #getting our template
#     name={
#         'student':'Abdull'
#     }
#     return render(request,'index.html',{'form':student}) #rendering the template in HttpResponse

def index(request):
    if request.method=="POST":
        student=StudentForm(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File Uploaded Succesfully")
    else:
        student=StudentForm()
        return render(request,'index.html',{'form':student})
# def methodinfo(request):
#     return HttpResponse("Http Request is: "+request.method)

# def setcookie(request):
#     response=HttpResponse('Cookie Set')
#     response.set_cookie('java-tutorial','javatpoint.com')
#     return response
# def getcookie(request):
#     tutorial=request.COOKIES['java-tutorial']
#     return HttpResponse("java tutorials @: "+ tutorial);
# def getfile(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="file.csv"'
#     employees = Employee.objects.all()
#     writer = csv.writer(response)
#     for employee in employees:
#         writer.writerow([employee.eid,employee.ename,employee.econtact])
#     return response

def getpdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment;"file.pdf"'
    p=canvas.Canvas(response)
    p.setFont("Times-Roman",55)
    p.drawString(100,700,"Hello,Javatpoint.")
    p.showPage()
    p.save()
    return response









