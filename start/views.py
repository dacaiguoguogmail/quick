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
        # auserdata = UserDataModel2()
        # auserdata.av = 'av'
        # auserdata.an = 'an'
        # auserdata.ec = 'ec'
        # auserdata.rsd = 'rsd'
        # auserdata.scsd = 'scsd'
        # auserdata.ecd = 'ecd'
        # auserdata.nt = 'nt'
        # auserdata.rft = 'rft'
        # auserdata.i10 = 'i10'
        # auserdata.sced = 'sced'
        # auserdata.iuf = 'iuf'
        # auserdata.red = 'red'
        # auserdata.fsd = 'fsd'
        # auserdata.spsd = 'spsd'
        # auserdata.dlsd = 'dlsd'
        # auserdata.sped = 'sped'
        # auserdata.dz = 'dz'
        # auserdata.pi = 'pi'
        # auserdata.rt = 'rt'
        # auserdata.rc = 'rc'
        # auserdata.dled = 'dled'
        # auserdata.csd = 'csd'
        # auserdata.re = 're'
        # auserdata.at = 'at'
        # auserdata.npn = 'npn'
        # auserdata.pc = 'pc'
        # auserdata.ced = 'ced'
        # auserdata.cp = 'cp'
        # auserdata2 = UserDataModel2.objects.get(pk=1)
        ause2 = UserModel2.objects.get(pk=1)
        ause2.userdatamodel2_set.create(av = 'av',an = 'an',ec = 'ec',rsd = 'rsd',scsd = 'scsd',ecd = 'ecd',nt = 'nt',rft = 'rft',i10 = 'i10',sced = 'sced',iuf = 'iuf',red = 'red',fsd = 'fsd',spsd = 'spsd',dlsd = 'dlsd',sped = 'sped',dz = 'dz',pi = 'pi',rt = 'rt',rc = 'rc',dled = 'dled',csd = 'csd',re = 're',at = 'at',npn = 'npn',pc = 'pc',ced = 'ced',cp = 'cp')
        # auserdata.save()
        ause2.save()
    
    return Response(json.dumps(result), content_type='application/json')

