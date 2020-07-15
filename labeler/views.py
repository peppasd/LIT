from django.shortcuts import render

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


def project_labeler(request):
    context = {
        'labelimages': labelimages,
        'tags': tags
    }

    return render(request, 'project_labeler.html', context)
