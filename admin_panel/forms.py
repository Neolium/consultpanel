# coding: utf-8

from consult_panel.models import *
from documents.models import *
from django.forms import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.models import User


class InscriptionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-6'
        self.helper.add_input(Submit('submit', 'Envoyer'))
        super(InscriptionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Inscription
        fields = ['nom', 'prenom', 'client']
        labels = {'nom': 'Nom : ', 'prenom': 'Prénom : ',
                  'client': 'Client associé : '}


class LocalisationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-6'
        self.helper.add_input(Submit('submit', 'Envoyer'))
        super(LocalisationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Localisation
        fields = ['nom', 'latitude', 'longitude']
        labels = {'label': 'Nom : ', 'latitude': 'Latitude : ',
                  'longitude': 'Longitude : '}


class ClientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-6'
        self.helper.add_input(Submit('submit', 'Envoyer'))
        super(ClientForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Client
        fields = ['nom', 'catalogue', 'entreprise']
        labels = {'label': 'Nom : ', 'catalogue': 'Catalogue associé : ',
                  'entreprise': 'Entreprise associée : '}


class FileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-6'
        self.helper.add_input(Submit('submit', 'Envoyer'))
        super(FileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Template
        fields = ['label', 'document', 'type']
        labels = {'label': 'Titre : ', 'document': 'Fichier : '}


class CoursForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-6'
        self.helper.add_input(Submit('submit', 'Ajouter'))
        super(CoursForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Cours
        fields = ['date_cours_debut', 'date_cours_fin',
                  'localisation']
        labels = {
            'date_cours_debut': 'Début : ',
            'date_cours_fin': 'Fin : ',
            'localisation': 'Localisation',
            'session': 'Session de formation'
        }


class FormationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Sauvegarder'))
        super(FormationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Formation
        fields = ['nom', 'description', 'prix_ht', 'prix_ttc']
        labels = {
            'nom': 'Nom : ',
            'description': 'Description : ',
            'prix_ht': 'Prix H.T (€) : ',
            'prix_ttc': 'Prix T.T.C (€) : '
        }


class CatalogueForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Sauvegarder'))
        super(CatalogueForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Catalogue
        fields = ['nom', 'liste_formations']
        labels = {
            'nom': 'Nom : ',
            'liste_formations': 'Liste des formations : ',
        }


class SessionForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Ajouter'))
        super(SessionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Session
        fields = ['formation']


class EntrepriseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Sauvegarder'))
        super(EntrepriseForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Entreprise
        fields = ['nom']

class CentreFormationForm(ModelForm):

    nom = CharField(required=True, label="Nom de l'entreprise :")
    siret = CharField(required=True, label="Numéro de siret :")
    adresse = CharField(required=True, label="Adresse :")
    ville = CharField(required=True, label="Ville :")
    code_postal = CharField(required=True, label="Code Postal :")
    telephone =  CharField(required=True, label="Téléphone :")

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-9'
        self.helper.add_input(Submit('submit', 'Sauvegarder'))
        super(CentreFormationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CentreFormation
        fields = ['nom', 'siret', 'adresse', 'ville',
                  'code_postal', 'telephone']

