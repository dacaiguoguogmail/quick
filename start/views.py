from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone 
from django.views import generic
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Choice, Question, UserDataModel2, UserModel2
import json
import gzip
import base64

class IndexView(generic.ListView):
    template_name = 'start/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
#        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'start/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'start/results.html'

class UUIDView(generic.DetailView):
    model = UserModel2
    template_name = 'start/uuid.html'


def numberview(request, mn):
    user_list = UserModel2.objects.filter(mn=mn)
    user_list2 = []
    for oneuser in user_list:
        allll = oneuser.userdatamodel2_set.all()
        for aus in allll:
            user_list2.append({"id":(aus.id), "retime":((aus.red-aus.rsd)*1000)})

    return render(request, 'start/number.html', {'usermodel2_list': user_list2, "number2": mn})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        return render(request, 'start/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('start:results', args=(question.id,)))


#    return HttpResponse("You're voting on question %s." % question_id)
@api_view(['POST', 'HEAD'])
def addapi(request):
    orgss = request.data['data']
    base64.b64decode(orgss)
    orgssbytes = base64.b64decode(orgss)
    orgssjson = gzip.decompress(orgssbytes)
    dataDict = json.loads(orgssjson)
    ause = UserModel2()
    ause.lo = dataDict['lo']
    ause.la = dataDict['la']
    ause.prov = dataDict['prov']
    ause.dt = dataDict['dt']
    ause.tec = dataDict['tec']
    ause.ct = dataDict['ct']
    ause.ui = dataDict['ui']
    ause.ns = dataDict['ns']
    ause.ver = dataDict['ver']
    ause.ot = dataDict['ot']
    ause.mn = dataDict['mn']
    ause.save()
    result = {}

    for k in dataDict['data']:
        model2 = UserDataModel2()
        model2.av = k['av']
        model2.an = k['an']
        model2.ec = k['ec']
        model2.rsd = k['rsd']
        model2.scsd = k['scsd']
        model2.ecd = k['ecd']
        model2.nt = k['nt']
        model2.rft = k['rft']
        model2.i10 = k['i10']
        model2.sced = k['sced']
        model2.iuf = k['iuf']
        model2.red = k['red']
        model2.fsd = k['fsd']
        model2.spsd = k['spsd']
        model2.dlsd = k['dlsd']
        model2.sped = k['sped']
        model2.dz = k['dz']
        model2.pi = k['pi']
        model2.rt = k['rt']
        model2.rc = k['rc']
        model2.dled = k['dled']
        model2.csd = k['csd']
        model2.re = k['re']
        model2.at = k['at']
        model2.npn = k['npn']
        model2.pc = k['pc']
        model2.ced = k['ced']
        model2.cp = k['cp']
        model2.usermodel = ause
        model2.save()
    
    return Response(json.dumps(result), content_type='application/json')

