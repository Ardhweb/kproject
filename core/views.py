from django.shortcuts import render,redirect,get_object_or_404,HttpResponse

# Create your views here.
from .forms import UploadFileForm,ShareForm
from django.contrib.auth.decorators import login_required
from .models import UploadFile,SharedFiles
from account.models import UserProfile
from django.db.models import Q
from django.contrib.auth import get_user_model

# from django.contrib.auth.models import Group, Permission, User



def core_engine(request):
    # permissions = Permission.objects.all()
    # print(permissions)

    if not request.user.is_authenticated:
        # Get all objects
       files_list = f"No File Yet"
       shared_file = f"ss"
    else:
        # Get objects related to the currently logged-in user
       files_list = UploadFile.objects.filter(user=request.user)
       shared_file = SharedFiles.objects.all().filter(shared_with=request.user.id)
    return render(request, "core/home.html",{'files_list':files_list, 'shared_file': shared_file,})


@login_required
def upload_file(request):
    if request.method == 'POST':
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save(commit=False)
            upload_form.cleaned_data['uploading_file']
            upload_form.save()
            return redirect('core:home')
    else:
        upload_form = UploadFileForm(initial={'user':request.user.id})
    return render(request, "core/upload_file.html", {'upload_form':upload_form})


@login_required
def search_user(request):
    if request.method == "POST":
        query =  request.POST['searched']
        search_results = UserProfile.objects.filter(
                    Q(full_name__icontains=query))
        context = {'search_results':search_results}
        return render(request,"core/search_rspg.html",context)
    else:
        user_profiles = UserProfile.objects.all()
    return render(request, 'core/search_rspg.html', {})


@login_required
def share_file(request,file_id):
    file_ids = get_object_or_404(UploadFile, file_id=file_id)
    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            # form['sharefiles'] = file_ids
            form.cleaned_data
            form.save()
            return redirect('core:home')
        else:
            return HttpResponse("Invalid Request!")
    else:
        form = ShareForm(initial={'sharefiles':file_ids})
    return render(request, "core/share-file.html", {'form':form})







