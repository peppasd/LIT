from django.shortcuts import render
from django.http import HttpResponseRedirect
from projects.utils import allTags_project
from projects.models import Project, Value, Label, Photo
from django.contrib.auth.decorators import login_required





def removeValue(pk):
    elm = Value.objects.get(pk=pk)      
    elm.delete()    

@login_required
def project_labeler(request, pk):    
    labelimages = []
    tagLists = []
    project = Project.objects.get(id=pk)

    for img in project.images.all():
        labelimages.append(img)
     
    tagLists = Label.objects.all()
    loopId = 0    
    labelimages = list(labelimages)    

    if request.method == 'POST':
        tagIds = list(request.POST.getlist('tagId'))
        delValues = list(request.POST.getlist('del'))                
        tagVals = request.POST.getlist('tagVal')
        addId = request.POST['addTag']
        imgId = request.POST['imgId']
        loopId = request.POST['loopId']
        loopId = int(loopId)
        if len(delValues) > 0:
            for delId in delValues:
                if delId in tagIds:
                    tagIds.remove(delId)
                valId = int(delId)
                removeValue(valId)
        if loopId != 0:
            indexImg = 0
            for i,j in enumerate(labelimages):               
                if str(j.uuid) == imgId:
                    indexImg = i
                    break
            labelimages[0], labelimages[indexImg] = labelimages[indexImg], labelimages[0]

        if addId:
            photo = Photo.objects.get(uuid=imgId)
            getLabel = Label.objects.get(id=addId)
            labels = []
            for tag in photo.values.all():
                labels.append(tag.label.first())
            if getLabel not in labels:
                valObj = Value(val=' ')
                valObj.save()
                valObj.label.add(getLabel)
                valObj.save()
                valObj.photo = photo
                valObj.save()        

        for i in range(len(tagIds)):
            obj = Value.objects.get(id=tagIds[i])
            obj.val = tagVals[i]
            obj.save()

    context = {
        'labelimages': labelimages,
        'pk': pk,
        'tagLists': tagLists,
        'project': project,
    }

    return render(request, 'project_labeler.html', context)
