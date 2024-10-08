from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Charge,FormulaireCharge,FormulaireListeDesProprietaires,FormulaireCotization,FormulairePConcierge #, Genero
from django.core.validators import MinValueValidator, MaxValueValidator



class RegisterUserForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
    
    def __init__(self, *args, **kwargs) :
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
        


class EnregistrerChargeForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = '__all__'
        widgets = {'nome_charge': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introduire la charge','name':'nome_charge'}),}


class EnregistrerFormulaireChargeForm(forms.ModelForm):
    class Meta:
        model = FormulaireCharge
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date', 'type': 'date'}),
            'charge': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Charge'}),
            'du': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Du', 'type': 'date'}),
            'au': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Au', 'type': 'date'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montant', 'id': 'id_montant', 'min': '0', 'step': '0.01'}),
            'image_charge': forms.ClearableFileInput(attrs={'class': 'form-control', 'name': 'files', 'id': 'formFile'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Obtener las opciones dinámicamente desde el modelo Charge
        self.fields['charge'].queryset = Charge.objects.all()  # Puedes ajustar esto según tus necesidades de filtrado

class EnregistrerFormulaireListeProprietaireForm(forms.ModelForm):
    class Meta:
        model = FormulaireListeDesProprietaires
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom','name':'nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom','name':'prenom'}),
            'aptNum': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nº Apt', 'min': '0', 'max': '2100', 'id':'id_aptNum'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tel','name':'tel'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email','name':'email'}),
            'proprietaire_locataire': forms.Select(attrs={'class': 'form-control'}, choices=FormulaireListeDesProprietaires.proprietaire_locataire_choices),
        }
        
class EnregistrerFormulaireCotizationForm(forms.ModelForm):
    class Meta:
        model = FormulaireCotization
        fields = '__all__'
        widgets = {
            'codeFormCotiz': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_codeFormCotiz', 'readonly':'readonly'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'liste_proprietaire': forms.Select(attrs={'class': 'form-control', 'id': 'id_liste_proprietaire'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_prenom'}),
            'aptNum': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_aptNum'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_montant'}),
            'regle': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'motif_mois': forms.Select(attrs={'class': 'form-control'}),
            'motif_annee': forms.Select(attrs={'class': 'form-control'}),
            'frais_sindic': forms.Select(attrs={'class': 'form-control','id': 'id_frais_sindic'}),
            #'frais_sindic': forms.Select(choices=FormulaireCotization.frais_sindic_choices, attrs={'class': 'form-control', 'id': 'id_frais_sindic'}),
            'frais_sindic_manual': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_frais_sindic_manual', 'placeholder': 'Frais Syndic Manual (opcion de escribir o seleccionar)', 'value' :'----'}),
            'image_signer': forms.ClearableFileInput(attrs={'class': 'form-control', 'name': 'files', 'id': 'formFile'}),
        
        
        }
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        super(EnregistrerFormulaireCotizationForm, self).__init__(*args, **kwargs)
        # Obtener el último valor de codeFormCotiz de la base de datos
        last_code = FormulaireCotization.objects.order_by('-codeFormCotiz').first()
        if last_code and last_code.codeFormCotiz is not None:
            next_code = last_code.codeFormCotiz + 1
        else:
            next_code = 2205
        self.fields['codeFormCotiz'].initial = next_code
        if self.instance and self.instance.frais_sindic:
            self.fields['frais_sindic'].initial = self.instance.frais_sindic
            print(list(self.fields['frais_sindic'].choices))


class EnregistrerFormulairePConciergeForm(forms.ModelForm):
    class Meta:
        model = FormulairePConcierge
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
            'nom': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_prenom'}),
            
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_montant'}),
            
            'mois': forms.Select(attrs={'class': 'form-control'}),
            'annee': forms.Select(attrs={'class': 'form-control'}),
            
        
        
        }
    def __init__(self, *args, **kwargs):
        super(EnregistrerFormulairePConciergeForm, self).__init__(*args, **kwargs)
        self.fields['nom'].initial = "AABANE"
        self.fields['prenom'].initial = "BRAHIM"
