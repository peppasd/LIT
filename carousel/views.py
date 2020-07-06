from django.shortcuts import render

# Create your views here.

labelimages = [
    {
    "url": "https://www.wonderplugin.com/wp-content/uploads/2013/12/Evening_1024.jpg",
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
    },    {
    'url': "https://www.wallpapers13.com/wp-content/uploads/2016/01/Cool-and-Beautiful-Nature-desktop-wallpaper-image-2560X1600-1600x1200.jpg",
    },    {
    'url': "https://tse1.mm.bing.net/th?id=OIP.otIPf0nD6Sxy3HcAhQJnGAHaE8&pid=Api",
    },    {
    'url': "https://i.ytimg.com/vi/co1yhzb9fu0/maxresdefault.jpg",
    },    {
    "url": "https://www.wonderplugin.com/wp-content/uploads/2013/12/Evening_1024.jpg",
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
    },    {
    'url': "https://www.wallpapers13.com/wp-content/uploads/2016/01/Cool-and-Beautiful-Nature-desktop-wallpaper-image-2560X1600-1600x1200.jpg",
    },    {
    'url': "https://tse1.mm.bing.net/th?id=OIP.otIPf0nD6Sxy3HcAhQJnGAHaE8&pid=Api",
    },    {
    'url': "https://i.ytimg.com/vi/co1yhzb9fu0/maxresdefault.jpg",
    },
]
tags = [
    {'title': "Band", 'type': 'bool'},
    {'title': "Queen", 'type': 'bool'},
    {'title': "Age", 'type': 'int'},
    {'title': "Color", 'type': 'string'},
]


def project_carousel(request):
    context = {
        'labelimages': labelimages,
        'tags': tags
    }

    return render(request, 'project_carousel.html', context)
