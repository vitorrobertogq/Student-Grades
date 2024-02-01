from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
import gspread

#Initial Page
def home(request):
    return render(request,'home/home.html')

from django.http import HttpResponse

#Reading and interpreting the worksheet
def sheet_function(request):

    if request.method == 'POST':
        google_sheets_link = request.POST.get('google_sheets_link', '')

    #Part of worksheet link
    code = google_sheets_link.split('/')[5]

    #API CONFIG
    googleclient = gspread.service_account(filename='config/key.json')
    
    sheet = googleclient.open_by_key(code)

    worksheet = sheet.get_worksheet(0)

    values = worksheet.get_all_values()

    for row in values:
        #Number Of Classes
        if row[0].split()[0] == 'Total':
            number_of_classes = int(row[0].split()[5])
        #Student Data
        elif row[0].split()[0].isnumeric():
            student = Student(number_of_classes,row[0],row[1],row[2],row[3],row[4],row[5])
            worksheet.update(f'G{student.get_situation()[1]}', [[student.get_situation()[2]]])
            worksheet.update(f'H{student.get_situation()[1]}', [[student.get_situation()[4]]])

    return HttpResponse('Operation Finished !')
            
