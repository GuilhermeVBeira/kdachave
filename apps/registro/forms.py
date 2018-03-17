from django import forms
from apps.registro.models import Registro


class RegistroForm(forms.ModelForm):

	class Meta:
		model = Registro
		fields = ['dataEntrega',
				  'dataPrevisaoRetorno',
				  'dataRetorno',
				  'responsavel',
				  'propriedade',
				  'molhos',
				  ]


class RegistroSaidaForm(forms.ModelForm):

	class Meta:
		model = Registro
		fields = [
				  'responsavel',
				  'dataEntrega',
				  'dataPrevisaoRetorno',
				  'propriedade',
				  'molhos',
				  ]


class RegistroDevolucaoForm(forms.ModelForm):

	class Meta:
		model = Registro
		fields = ['molhos', 'dataEntrega']
