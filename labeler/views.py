from django.shortcuts import render
from projects.utils import allTags_project
from projects.models import Project, Value
from django.contrib.auth.decorators import login_required

# Create your views here.

labelimages = [
    {
    "url": "https://www.wonderplugin.com/wp-content/uploads/2013/12/Evening_1024.jpg",
    "uploaded": "15-Jun-20",
    "uploader": "theRealLabeler",
    "lastedit": "07-Jul-20",
    "lastlabeler": "belerla"
    },    {
    "url": "https://tse1.mm.bing.net/th?id=OIP.otIPf0nD6Sxy3HcAhQJnGAHaE8&pid=Api",
    },    {
    'url': "https://i.ytimg.com/vi/7WCbIjqjHM4/maxresdefault.jpg",
    },    {
    'url': "https://www.wonderplugin.com/wp-content/uploads/2013/12/Evening_1024.jpg",
    },    {
    'url': "https://www.wonderplugin.com/wp-content/uploads/2013/12/Evening_1024.jpg",
    },    {
    'url': "https://i.ytimg.com/vi/7WCbIjqjHM4/maxresdefault.jpg",
    }
]
tags = [
    {'title': "Band", 'type': 'bool'},
    {'title': "Queen", 'type': 'bool'},
    {'title': "Age", 'type': 'int'},
    {'title': "Color", 'type': 'string'},
]


@login_required
def project_labeler(request, pk):    
    labelimages = []
    project = Project.objects.get(id=pk)
    labelimages = project.images.all()    
    
    if request.method == 'POST':
        tagIds = list(request.POST.getlist('tagId'))
        tagVals = (request.POST.getlist('tagVal'))

        for i in range(len(tagIds)):
            obj = Value.objects.get(id=tagIds[i])
            obj.val = tagVals[i]
            obj.save()
        
        

    context = {
        'labelimages': labelimages,       
        'pk': pk,
    }

    return render(request, 'project_labeler.html', context)
