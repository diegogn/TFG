from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from Audits.foms import UploadForm, QuestionForm
from Audits.models import Document, Question
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission

# Create your views here.

def index(request):
    return render(request, 'welcome.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(filename = request.POST['filename'],docfile = request.FILES['docfile'])
            newdoc.save(form)
            return redirect("uploads")
    else:
        form = UploadForm()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'upload.html', {'form': form})

@login_required()
def questions(request):
    preguntas = Question.objects.all()
    
    return render(request, 'question_list.html', {'preguntas': preguntas})

def details(request, question_id):
    pregunta = get_object_or_404(Question,pk=question_id)
    if not request.user.id is pregunta.user.id:
        return HttpResponse("No eres el creador de la pregunta.")
    return render(request, 'questions_details.html', {'pregunta': pregunta})

def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    else:
        form = UserCreationForm
    return render(request,'sigin.html',{'form': form})

@login_required()
@permission_required('Audits.add_question')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return HttpResponseRedirect('/audits/questions')
    else:
        form = QuestionForm
    return render(request,'question_create.html',{'form':form})

def documents(request):
    documents = Document.objects.all()
    
    return render(request, 'documents_list.html', {'documents': documents})

def callback(request):
    
    return HttpResponse("Hecho")

    