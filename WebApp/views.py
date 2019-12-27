from django.http import HttpResponse
import csv
from reportlab.pdfgen import canvas

def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="BigData.csv"'
    writer = csv.writer(response)
    writer.writerow(['1001', 'Subba', 'Thomson', 'Networking', '"Testing"'])
    writer.writerow(['1003', 'Smith', 'John', 'H/W'])
    return response

def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="BigData.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100, 700, "Hei, DJANGO.")
    p.showPage()
    p.save()
    return response
