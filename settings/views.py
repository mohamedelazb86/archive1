from django.shortcuts import render,redirect
from settings.models import Sector,Document_Type
from django.contrib import messages

def sector(request):
    sector=Sector.objects.all()

    context={
        'sector':sector
    }
    return render(request,'settings/sector.html',context)


def add_sector(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        Sector.objects.create(
            code=code,
            name=name,
            notes=notes
        )

        messages.success(request,'مبرووووك تم إضافة قطاع بنجاح')

        return redirect('/settings/sector')
    
def delete_sector(request):
    if request.method=='POST':
        sector_id=request.POST['id']
        sector=Sector.objects.get(id=sector_id)
        sector.delete()
        messages.success(request,'تم الحذف بنجاح')
        return redirect('/settings/sector')
    
def edit_sector(request):
    if request.method=='POST':
        sector_id=request.POST['id']
        sector=Sector.objects.get(id=sector_id)
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        sector.code=code
        sector.name=name
        sector.notes=notes

        sector.save()
        messages.success(request,'مبرررك تم التعديل بنجاح')
        return redirect('/settings/sector')

    
# Document  Type


def document_type(request):
    document_type=Document_Type.objects.all()

    context={
        'document_type':document_type
    }
    return render(request,'settings/document_type.html',context)

def add_document_type(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        Document_Type.objects.create(
            code=code,
            name=name,
            notes=notes
        )

        messages.success(request,'مبرووووك تم إضافة نوع مستند بنجاح')

        return redirect('/settings/document-type')
    
def delete_document_type(request):
    if request.method=='POST':
        document_type_id=request.POST['id']
        document_type=Document_Type.objects.get(id=document_type_id)
        document_type.delete()
        messages.success(request,'تم الحذف بنجاح')
        return redirect('/settings/document-type')
    
def edit_document_type(request):
    if request.method=='POST':
        document_type_id=request.POST['id']
        document_type=Document_Type.objects.get(id=document_type_id)
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        document_type.code=code
        document_type.name=name
        document_type.notes=notes

        document_type.save()
        messages.success(request,'مبرررك تم التعديل بنجاح')
        return redirect('/settings/document-type')
def dashbord(request):
    return render(request,'settings/dashbord.html',{})