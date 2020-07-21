from django.shortcuts import render
from projects.utils import allTags_project
from projects.models import Project, Value, Label, Photo
from django.contrib.auth.decorators import login_required

@login_required
def project_labeler(request, pk):
    labelimages = []
    tagLists = []
    project = Project.objects.get(id=pk)
    labelimages = project.images.all()
    tagLists = Label.objects.all()

    if request.method == 'POST':
        tagIds = list(request.POST.getlist('tagId'))
        tagVals = request.POST.getlist('tagVal')
        addId = request.POST['addTag']
        imgId = request.POST['imgId']

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
