from django.shortcuts import render
from gingerit.gingerit import GingerIt 
from django.http import HttpResponse
import json
from .models import Grammercheck
from .forms import GrammerForm

def index(request):
    text = 'JavaScript engines are originaly used only the web browsers, but are now core components of some servers and a variety of aplictions. The most popular runtime system of this usage is Node.js.'
    parser = GingerIt()
    output = parser.parse(text)
    with open("/var/www/subdomain/spellchecker/grammer/media/json/test.json", "w") as outfile:
        json.dump(output, outfile)
    # Opening JSON file
    f = open('/var/www/subdomain/spellchecker/grammer/media/json/test.json')
    data = json.load(f)
    # list
    print(data['result'])
    f.close()
    return HttpResponse('hello world')
    #return render(request,{'result': text})

# def grammer(request):
#     text = 'JavaScript engines are originaly used only the web browsers, but are now core components of some servers and a variety of aplictions. The most popular runtime system of this usage is Node.js.'
#     parser = GingerIt()
#     output = parser.parse(text)
#     with open("sample.json", "w") as outfile:
#         json.dump(output, outfile)
#     # Opening JSON file
#     f = open('sample.json')
#     data = json.load(f)
#     # list
#     print(data['result'])
#     f.close()
#     return HttpResponse('hello world')


def grammerform(request):
    if request.method == 'POST':
        form = GrammerForm(request.POST, request.FILES)
        if form.is_valid():
            #func_obj = form
            #func_obj.sourceFile = form.cleaned_data['sourceFile']
            form.save()
            #print(form.Document.document)
            #form.save()
            documents = Grammercheck.objects.all()
            for obj in documents:
                grammertext = obj.description
                #info = obj.info
            #print(rank)
            #print(baseurls)
            #print(grammertext)
            parser = GingerIt()
            output = parser.parse(grammertext)
            with open("/var/www/subdomain/spellchecker/grammer/media/json/sample.json", "w") as outfile:
                json.dump(output, outfile)
            # Opening JSON file
            f = open('/var/www/subdomain/spellchecker/grammer/media/json/sample.json')
            data = json.load(f)
            # list
            print(data['result'])
            rewrtingtext = data['result']
            f.close()
            return render(request, 'grammer.html', {'rewrtingtext':rewrtingtext, 'grammertext': grammertext})
    else:
        form = GrammerForm()
        #documents = Grammercheck.objects.all().order_by('-id')
    return render(request, 'grammer.html', {
        'form': form,
    })