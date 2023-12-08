from django import forms
from .models import UploadFile,SharedFiles
from django.contrib.auth.models import User

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('uploading_file','user')
        widgets ={
                'user':forms.TextInput(attrs={'style':'display:none; '}),
                
                  
        }


from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255,)



class ShareForm(forms.ModelForm):
    class Meta:
        model = SharedFiles
        fields = ('sharefiles','shared_with','access_level')
        widgets ={
                'sharefiles':forms.TextInput(attrs={'style':'display:none;'}),
                'shared_with':forms.SelectMultiple(attrs={'class':'form-control text-center'}),
                'access_level':forms.Select(attrs={'class':'form-control w-100 '}),
                
            }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Exclude admin users from the related_users field
            self.fields['related_users'].queryset = User.objects.exclude(is_superuser=True)