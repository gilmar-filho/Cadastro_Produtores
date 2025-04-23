'''
from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'celular1', 'celular2', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'celular1': forms.TextInput(attrs={'class': 'form-control'}),
            'celular2': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
'''
from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [
            'nome', 'cpf', 'endereco', 'numero_casa', 'zona_rural',
            'telefone1', 'telefone2', 'cartao_produtor',
            'checkbox_1', 'checkbox_2', 'checkbox_3', 'checkbox_4',
            'relatorio'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_casa': forms.TextInput(attrs={'class': 'form-control'}),
            'zona_rural': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'telefone1': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone2': forms.TextInput(attrs={'class': 'form-control'}),
            'cartao_produtor': forms.TextInput(attrs={'class': 'form-control'}),
            'checkbox_1': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'checkbox_2': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'checkbox_3': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'checkbox_4': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'relatorio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get("nome")
        cpf = cleaned_data.get("cpf")
        telefone1 = cleaned_data.get("telefone1")
        endereco = cleaned_data.get("endereco")

        if not all([nome, cpf, telefone1, endereco]):
            raise forms.ValidationError("Os campos Nome, CPF, Telefone 1 e Endereço são obrigatórios.")
