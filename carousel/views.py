from django.shortcuts import render

# Create your views here.

labelimages = [
    {
    "url": "https://www.wonderplugin.com/wp-content/uploads/2013/12/Evening_1024.jpg",
    "Band": "false",
    "Queen": "true",
    "Age":  "130",
    },
    {
    "url": "https://www.wonderplugin.com/wp-content/uploads/2013/12/Evening_1024.jpg",
    "Band": "false",
    "Queen": "true",
    "Age":  "n/d",
    },

    {
    'url': "https://www.wonderplugin.com/wp-content/uploads/2013/12/Evening_1024.jpg",
    "Band": "true",
    "Queen": "false",
    "Age":  90,
    },
]
tags = [
    "Band",
    "Queen",
    "Age",
]


def project_carousel(request):
    context = {
        'labelimages': labelimages,
        'tags': tags
    }
    return render(request, 'project_carousel.html', context)
