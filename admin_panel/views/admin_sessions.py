from django.shortcuts import render
from consult_panel.models import *
from django.contrib.auth.decorators import permission_required
from admin_panel.forms.forms import SessionForm


def sessions_index(request):
    return render(request, 'admin_sessions_index.html', context={
        'page_title'        : 'Gestion des sessions',
        'sessions_list'     : Session.objects.all()
        });
        
def sessions_add(request):
    return render(request, 'admin_sessions_add.html', {
        'page_title'        : 'Ajouter une session',
        'form'              : SessionForm()
    });
    
def sessions_edit(request, id):
    return render(request, 'admin_sessions_edit.html', {
        'page_title'        : 'Editer une session',
        'form'              : SessionForm(instance=Session.objects.get(pk=id))
    });
    