from django.shortcuts import get_object_or_404, render

#Dummy Project
projects = [
    {
        'id' : '001',
        'title' : 'Face Detector',
        'date_created': 'August 22, 2030'
    },
    
    {
        'id': '002',
        'title' : 'Puppy Detector',
        'date_created': 'November 02, 1894'
    }
]
members = [
    {
       'username': 'John'
    },
    {
       'username': 'Big John'
    },
    {
       'username': 'Raw John'
    }
]
tags = [
    'testing',
    'the queen',
    'old'
]
images = [
    {'url':'https://www.cheatsheet.com/wp-content/uploads/2017/12/Queen-Elizabeth-Waving.jpg',
     'isTagged': True,},
    {'url':'https://www.cheatsheet.com/wp-content/uploads/2017/10/queen-elizabeth-fur.jpg',
    'isTagged': False,},
    {'url':'http://i.dailymail.co.uk/i/newpix/2018/06/29/21/4DBC9DE400000578-0-Fans_of_the_Royal_family_grew_worried_about_Queen_Elizabeth_II_s-m-55_1530303342340.jpg',
    'isTagged': False,},
    {'url':'https://tse3.mm.bing.net/th?id=OIP.raEAx7WtuS2iOyrYhTQUdQHaE8&pid=Api',
    'isTagged':True,},
    {'url':'https://tse4.mm.bing.net/th?id=OIP.kiRqPNokgSnJ6ApWGksB2QHaJe&pid=Api',
    'isTagged':True},
    {'url':'https://tse1.mm.bing.net/th?id=OIP.HC7u7SXAjRSapw29hIQ6ZgHaFj&pid=Api',
    'isTagged':True,},
]
count_images = images.__len__
tagged_images = 4

# Create your views here.
def project_overview(request):
    context = {
        'projects': projects,
        'members': members,
        'images': [images[0],images[1]],
        'tags':tags,
        'count_images': count_images,
    }
    #project = get_object_or_404(Project, pk=project_id)
    return render(request, 'project_overview.html', context)


def project_images(request):
    context = {
        'projects': projects,
        'members': members,
        'images':images,
        'tags':tags
    }
    return render(request, 'project_images.html', context)

