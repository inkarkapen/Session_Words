from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    return render(request,'wordsApp/index.html')
def process(request):
    if request.session['my_list'] == None:
        request.session['my_list'] = []
        request.session['my_dict'] = {}
    my_dict = request.session['my_dict']
    my_dict['word'] = request.POST['word']
    my_dict['color'] = request.POST.get('color', 'black')
    my_dict['font'] = request.POST.get('font', 'normal')
    my_dict['time'] = "-- " +strftime("%Y-%m-%d %H:%M %p", gmtime())
    request.session['my_dict'] = my_dict
    request.session['my_list'].append(my_dict)
    return redirect("/", request)
def clear(request):
    request.session['my_list'] = None
    return redirect("/", request)