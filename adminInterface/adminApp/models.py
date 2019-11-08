from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="Categorie/%Y/%m/%d/")
    date_add = models.DateTimeField( auto_now_add=True)
    date_upd = models.DateTimeField( auto_now=True)
    status = models.BooleanField(default=False)
    
    
    

    def __str__(self):
        return self.nom

class SousCategorie(models.Model):
    """Model definition for SousCategorie."""
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,related_name='categorie_sous')
    image = models.ImageField(upload_to="SousCategorie/%Y/%m/%d/")
    nom = models.CharField(max_length=250)
    date_add = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_upd = models.DateTimeField( auto_now=False, auto_now_add=True)
    status = models.BooleanField(default=True)
    

    # TODO: Define fields here

    class Meta:
        """Meta definition for SousCategorie."""

        verbose_name = 'SousCategorie'
        verbose_name_plural = 'SousCategories'

    def __str__(self):
        """Unicode representation of SousCategorie."""
        return self.nom





class Tag(models.Model):
    """Model definition for Tag."""

    # TODO: Define fields here
    nom = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Tag."""

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        """Unicode representation of Tag."""
        pass

class Produit(models.Model):
    titre=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to='Produit/')
    sous_categorie=models.ManyToManyField(SousCategorie)
    tag=models.ManyToManyField(Tag,related_name="tag_produit")
    date_add=models.DateTimeField(auto_now=True)
    date_upd=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)