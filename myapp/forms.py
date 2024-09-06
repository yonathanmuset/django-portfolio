from django import forms


class createnewtask(forms.Form):
    title = forms.CharField(
        label="titulo de tarea",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "input"}),
    )
    description = forms.CharField(
        label="descripcion de la tarea", widget=forms.Textarea(attrs={"class": "input"})
    )


class createnewproject(forms.Form):
    name = forms.CharField(
        label="nombre del proyecto",
        max_length=200,
        widget=forms.TextInput(attrs={"class": "input"}),
    )
