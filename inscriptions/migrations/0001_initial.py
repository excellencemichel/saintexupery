# Generated by Django 2.0.3 on 2018-06-02 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('prenom', models.CharField(max_length=250)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=250)),
                ('niveau', models.CharField(choices=[('maternelle', 'Maternelle'), ('cp1', '1ère Année ou CP1'), ('cp2', '2ème Année ou CP2'), ('ce1', '3ème Année ou CE1'), ('ce2', '4ème Année ou CE2'), ('cm1', '5ème Année ou CM1'), ('cm2', '1ère Année ou CM2'), ('sixieme', 'Classe de 6ème'), ('cinquième', 'Classe de 5ème'), ('quatrieme', 'Classe de 4ème'), ('troisiem', 'Classe de 3ème'), ('deuxieme', 'Classe de 2ème'), ('premiere', 'class de 1ère lycée'), ('terminale', 'Classe de terminale')], max_length=250)),
                ('frequence', models.CharField(choices=[('premiere', '1ère inscription'), ('renouvellment', 'Renouvellement')], max_length=250)),
                ('sexe', models.CharField(choices=[('masculin', 'Masculin'), ('feminin', 'Féminin')], max_length=250)),
                ('nationalite', models.CharField(max_length=250)),
                ('telephone', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('representant_parent_un', models.CharField(choices=[('pere', 'Père'), ('personne_morale', 'Personne morale ')], max_length=250)),
                ('nom_parent_un', models.CharField(max_length=250)),
                ('prenom_parent_un', models.CharField(max_length=250)),
                ('date_naissance_parent_un', models.CharField(max_length=250)),
                ('lieu_naissance_parent_un', models.CharField(max_length=250)),
                ('code_postal_naissance_parent_un', models.CharField(max_length=250)),
                ('nationalite_parent_un', models.CharField(max_length=250)),
                ('adresse_domicile_parent_un', models.CharField(max_length=250)),
                ('ville_parent_un', models.CharField(max_length=250)),
                ('telephone_domicile_parent_un', models.CharField(max_length=250)),
                ('telephone_personnel_parent_un', models.CharField(max_length=250)),
                ('telephone_professionnel_parent_un', models.CharField(max_length=250)),
                ('email_parent_un', models.EmailField(max_length=254)),
                ('profession_parent_un', models.CharField(max_length=250)),
                ('representant_parent_deux', models.CharField(choices=[('mere', 'Mère'), ('personne_morale', 'Personne morale ')], max_length=250)),
                ('nom_jeune_fille_parent_deux', models.CharField(blank=True, max_length=250, null=True)),
                ('nom_marial_parent_deux', models.CharField(max_length=250)),
                ('prenom_parent_deux', models.CharField(max_length=250)),
                ('date_naissance_parent_deux', models.CharField(max_length=250)),
                ('lieu_naissance_parent_deux', models.CharField(max_length=250)),
                ('code_postal_naissance_parent_deux', models.CharField(max_length=250)),
                ('nationalite_parent_deux', models.CharField(max_length=250)),
                ('telephone_domicile_parent_deux', models.CharField(max_length=250)),
                ('telephone_personnel_parent_deux', models.CharField(max_length=250)),
                ('telephone_professionnel_parent_deux', models.CharField(max_length=250)),
                ('email_parent_deux', models.EmailField(max_length=254)),
                ('profession_parent_deux', models.CharField(max_length=250)),
                ('adresse_domicile_parent_deux', models.CharField(blank=True, max_length=250, null=True)),
                ('situation_familiale', models.CharField(choices=[('marie', 'Marié'), ('vie_mariale_ou_PACS', 'Vie Mariale ou PACS'), ('divorce_ou_separe', 'Divorcé(e) ou séparé(e)'), ('celibataire', 'Célibataire'), ('veuf', 'Veuf(ve)')], max_length=250, null=True)),
                ('pdf_inscription', models.FileField(blank=True, null=True, upload_to='pdfs')),
                ('matricule', models.CharField(max_length=255)),
                ('image_enfant', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
