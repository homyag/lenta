from django import forms


# форма, которая будет отображать кнопку для загрузки файла
class UploadFileForm(forms.Form):
    file = forms.FileField()
