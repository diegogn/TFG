from django.contrib.auth.decorators import login_required
from apiclient.discovery import build
from django.http import HttpResponseRedirect
from django.shortcuts import render
from api.models import CredentialsModel
from Test import settings
from oauth2client.django_orm import Storage
import httplib2
from api.forms import CreateForm
from oauth2client.client import flow_from_clientsecrets
import os

CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), '..', 'client_secrets.json')

FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/calendar',
    redirect_uri='http://localhost:8000/api/oauth2callback')


# Create your views here.
@login_required
def create(request):
    storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()
    if credential is None or credential.invalid == True:
        authorize_url = settings.FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)
    else:
        http = httplib2.Http()
        http = credential.authorize(http)
        service = build(serviceName='calendar', version='v3', http=http)
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            calendar = {
                        'summary': form.cleaned_data['nombre'],
                        'timeZone': form.cleaned_data['zona_horaria'],
            }
            
            created_calendar = service.calendars().insert(body=calendar).execute()
            return render(request, 'welcome2.html', {'created_calendar': created_calendar})         
    else:
        form = CreateForm()

    return render(request, 'create_calendar.html', {'form': form})

@login_required
def auth_return(request):
    credential = FLOW.step2_exchange(request.REQUEST['code'])
    storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    storage.put(credential)
    return HttpResponseRedirect("/api/create")