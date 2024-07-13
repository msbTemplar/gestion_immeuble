from django.db import models

# Create your models here.

class Charge(models.Model):
        nome_charge = models.CharField('Une Charge', max_length=120)
        
        def __str__(self) -> str:
            return self.nome_charge

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # Obtener la extensión del archivo
    valid_extensions = ['.pdf', '.xls', '.xlsx', '.doc', '.docx','.jpg','.png']  # Extensiones permitidas
    if not ext.lower() in valid_extensions:
        raise ValidationError('Tipo de archivo no soportado. Sube archivos PDF, XLS, XLSX, DOC o DOCX.')  

class FormulaireCharge(models.Model):
    date=models.DateTimeField('Date')
    charge=models.ForeignKey(Charge, blank=True, null=True, on_delete=models.CASCADE)
    du=models.DateField('Du')
    au=models.DateField('Au')
    montant = models.DecimalField('Montant', max_digits=10, decimal_places=2)  # Agregar max_digits y decimal_places
    #image_charge = models.ImageField(null=True, blank=True, upload_to="images/")
    image_charge = models.FileField('Fichier de charge', null=True, blank=True, upload_to="uploads/",
                                    validators=[validate_file_extension])
    
    def __str__(self) -> str:  # Agregar un método __str__ para esta clase también
        return f"FormulaireCharge Charge {self.charge} du {self.du} au {self.au} avec le montant {self.montant} "
    

  

class FormulaireListeDesProprietaires(models.Model):
    proprietaire_locataire_choices = [
        ('Proprietaire', 'Proprietaire'),
        ('Locataire', 'Locataire')
    ]
    nom=models.CharField('Nom', max_length=120)
    prenom=models.CharField('Prenom', max_length=120)
    aptNum = models.IntegerField('Nº Apt',blank=True, null=True)
    tel=models.CharField('Tel', max_length=120)
    email=models.CharField('Email', max_length=120)
    proprietaire_locataire= models.CharField('Proprietaire/Locataire', max_length=120, choices=proprietaire_locataire_choices)
    
    def __str__(self) -> str:  # Agregar un método __str__ para esta clase también
        return f"FormulaireListeDesProprietaires Nom {self.nom} Prenom {self.prenom} Email {self.email} Proprietaire/Locataire {self.proprietaire_locataire} "
    

class FormulaireCotization(models.Model):
    proprietaire_locataire_choices = [
        ('Proprietaire', 'Proprietaire'),
        ('Locataire', 'Locataire')
    ]
    
    mois_choices = [
        ('Janvier', 'Janvier'),
        ('Février', 'Février'),
        ('Mars', 'Mars'),
        ('Avril', 'Avril'),
        ('Mai', 'Mai'),
        ('Juin', 'Juin'),
        ('Juillet', 'Juillet'),
        ('Août', 'Août'),
        ('Septembre', 'Septembre'),
        ('Octobre', 'Octobre'),
        ('Novembre', 'Novembre'),
        ('Décembre', 'Décembre'),
    ]

    annee_choices = [(str(year), str(year)) for year in range(2000, 2100)]
    
    frais_sindic_choices = [
        ('', ''),
        ('----', '----'),  # Opción vacía
        ('Frais Sindic', 'Frais Sindic')
    ]
    codeFormCotiz = models.IntegerField('Code', blank=True, null=True)
    date = models.DateTimeField('Date')
    liste_proprietaire = models.ForeignKey(FormulaireListeDesProprietaires, blank=True, null=True, on_delete=models.CASCADE)
    
    
    
    nom = models.CharField('Nom', max_length=120)
    prenom = models.CharField('Prenom', max_length=120)
    aptNum = models.IntegerField('Nº Apt', blank=True, null=True)
    
    montant = models.DecimalField('Montant', max_digits=10, decimal_places=2)  # Agregar max_digits y decimal_places
    
    regle = models.BooleanField('Reglé?', default=False)
    
    motif_mois = models.CharField('Mois', max_length=120, choices=mois_choices)
    motif_annee = models.CharField('Année', max_length=4, choices=annee_choices)
    frais_sindic = models.CharField('Frais Sindic', max_length=120, choices=frais_sindic_choices, blank=True, null=True)
    frais_sindic_manual = models.CharField('Frais Sindic Manual', max_length=120, blank=True, null=True)
    
    
    def __str__(self) -> str:
        return f"FormulaireCotization Nom {self.nom} Prenom {self.prenom} Nº Apt {self.aptNum} Proprietaire/Locataire {self.liste_proprietaire}"
    

class FormulairePConcierge(models.Model):
    
    mois_choices = [
        ('Janvier', 'Janvier'),
        ('Février', 'Février'),
        ('Mars', 'Mars'),
        ('Avril', 'Avril'),
        ('Mai', 'Mai'),
        ('Juin', 'Juin'),
        ('Juillet', 'Juillet'),
        ('Août', 'Août'),
        ('Septembre', 'Septembre'),
        ('Octobre', 'Octobre'),
        ('Novembre', 'Novembre'),
        ('Décembre', 'Décembre'),
    ]

    annee_choices = [(str(year), str(year)) for year in range(2000, 2100)]
    date = models.DateTimeField('Date')
        
    nom = models.CharField('Nom', max_length=120)
    prenom = models.CharField('Prenom', max_length=120)
        
    montant = models.DecimalField('Montant', max_digits=10, decimal_places=2)  # Agregar max_digits y decimal_places
            
    mois = models.CharField('Mois', max_length=120, choices=mois_choices)
    annee = models.CharField('Année', max_length=4, choices=annee_choices)
        
    def __str__(self) -> str:
        return f"FormulairePConcierge Nom {self.nom} Prenom {self.prenom} Montant {self.montant} Mois {self.mois} Année {self.annee}"