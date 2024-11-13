from django.shortcuts import render
from django.http import HttpResponse


projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

# Create your views here.
def projects(request):
    # name = 'Saroj Baniya'
    # context = {'name': name}

    context = {'projects': projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObject = None

    for i in projectsList:
        if i['id'] == str(pk):
            projectObject = i
    return render(request, 'projects/single-projects.html', {'project':projectObject})