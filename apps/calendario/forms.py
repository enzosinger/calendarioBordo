from django import forms

class CalendarioForms(forms.Form):
    nome=forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Evento de integração de calouros."
            }
        )
    )
    descricao=forms.CharField(
        label="Descrição",
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Descreva o evento."
            }
        )
    )
    disciplina=forms.CharField(
        label="Disciplina",
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Matemática."
            }
        )
    )
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))