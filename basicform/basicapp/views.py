from django.shortcuts import render
from basicapp.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def users(request):
    form = NewUserForm()

    if request.method =='POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else :
            print('Error form invalid')

    return render(request, 'basicapp/users.html', {'form':form})


def otherone(request):
    dict ={'text':'Hello World', 'number': 100}
    return render (request,'basicapp/otherone.html',dict)

def othertwo(request):
    return render(request,'basicapp/othertwo.html')
