from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.utils import simplejson
from django.core.mail import send_mail
from cross.models import Event, MailingList
from datetime import datetime



def home(request):
    return render_to_response('index.html',{'tabHome':True,}, context_instance=RequestContext(request))


def moreinfo(request):
    return render_to_response('moreinfo.html',{'tabMoreInfo':True}, context_instance=RequestContext(request))


def contact(request):
    if request.method == 'POST':
        try:
            data = simplejson.loads(request.POST['data'])
            message = "New message from crossing39th.com. \n\n"
            message += "From: " + data['email'] + '\n'
            message += "Subject: " + data['subject'] + '\n'
            message += "Body: " + data['body'] + '\n'

            send_mail('MESSAGE FROM crossing39th.COM', message, 'crossing39th@gmail.com',
                ['crossing39th@gmail.com'], fail_silently=False)

            mimetype = 'application/javascript'
            data = simplejson.dumps({'suc':True})
            return HttpResponse(data,mimetype)
        except Exception as e:
            mimetype = 'application/javascript'
            data = simplejson.dumps({'suc':False})
            return HttpResponse(data,mimetype)
    else:
        return render_to_response('contact.html',{'tabContact':True}, context_instance=RequestContext(request))


def mailingadd(request):
    if request.method == 'POST':
        try:
            data = simplejson.loads(request.POST['data'])

            MailingList.objects.create(email_address=data['email'])

            mimetype = 'application/javascript'
            data = simplejson.dumps({'suc':True})
            return HttpResponse(data,mimetype)
        except Exception as e:
            mimetype = 'application/javascript'
            data = simplejson.dumps({'suc':False})
            return HttpResponse(data,mimetype)
    else:
        return render_to_response('contact.html',{'tabContact':True}, context_instance=RequestContext(request))

def getinvolved(request):
    return render_to_response('getinvolved.html',{'tabGetInvolved':True}, context_instance=RequestContext(request))

