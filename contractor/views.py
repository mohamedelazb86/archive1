from django.shortcuts import render,redirect
from contractor.models import Contractor
from settings.models import Sector
from django.contrib import messages

def contractor(request):

    contractor=Contractor.objects.all()
    sector=Sector.objects.all()

    context={
        'contractor':contractor,
        'sector':sector
    }
    return render(request,'contractor/contractor.html',context)

def add_contractor(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        sector=request.POST['sector']
        project=request.POST['project']
        item=request.POST['item']
        notes=request.POST['notes']

        Contractor.objects.create(
            code=code,
            name=name,
            sector_id=sector,
            project=project,
            item=item,
            notes=notes
        )

        messages.success(request,'مبررروك تم إضافة مقاول بنجاح')
        return redirect('/contractor/contractor')
    
def delete_contractor(request):
    if request.method=='POST':
        contractor_id=request.POST['id']
        contractor=Contractor.objects.get(id=contractor_id)
        contractor.delete()
        messages.success(request,'تم الحذف بنجاح ')
        return redirect('/contractor/contractor')
def edit_contractor(request):
    if request.method=='POST':
        contractor_id=request.POST['id']
        contractor=Contractor.objects.get(id=contractor_id)
        code=request.POST['code']
        name=request.POST['name']
        sector=request.POST['sector']
        item=request.POST['item']
        project=request.POST['project']
        notes=request.POST['notes']

        contractor.code=code
        contractor.name=name
        contractor.sector_id=sector
        contractor.project=project
        contractor.item=item
        contractor.notes=notes

        contractor.save()

        messages.success(request,'تم التعديل بنجاح')
        return redirect('/contractor/contractor')

        
