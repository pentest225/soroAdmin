from django.contrib import admin
from .import models
from django.utils.safestring import mark_safe
# Register your models here.

#register inline
class SousCategorieInline(admin.TabularInline):
    model = models.SousCategorie 
    extra = 0

    
@admin.register(models.Categorie)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('view_image','nom','status','date_add','date_upd') 
    list_filter = ('status','date_add','date_upd')#les standard ou les foreignKey
    search_fields = ('nom',)#dois etre dans liste display; ne pas metres de stadard; prend le charField ou les relations 
    list_display_links = ('view_image','nom')# tous les elements squf les standards
    list_per_page = 3
    ordering = ['nom']
    date_hierarchy = 'date_add'
    inlines = [SousCategorieInline]
    readonly_fields=['detaile_image']
    
    actions = ('active','deactive')
    
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selections a été active avec seccès')

    active.short_description = 'active les categorie sélectionée '
    
        
        
        
    def deactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,'la selections a ete désactive avec seccès')

    deactive.short_description = 'deactivé les categorie sélectionée '
    
    def view_image(self,obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.image.url))
    
    def detaile_image(self,obj):
        return mark_safe('<img src="{url}" width="300px" height="300px" />'.format(url=obj.image.url))
    
@admin.register(models.SousCategorie)
class SousCategorieAdmin(admin.ModelAdmin):
    list_display = ('categorie','nom','status','date_add','date_upd','view_image') 
    list_filter = ('categorie','status','date_add','date_upd')#les standard ou les foreignKey
    search_fields = ('nom',)#dois etre dans liste display ne pas metres de stadard prend le charField ou les relations 
    list_display_links = ('view_image','nom')# tous les elements squf les standards
    list_per_page = 3
    ordering = ['nom']
    date_hierarchy = 'date_add'
        
    actions = ('active','deactive')
        
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selections a été active avec seccès')

    active.short_description = 'active les sous categorie sélectionée '
        
            
            
            
    def deactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,'la selections a ete désactive avec seccès')

    deactive.short_description = 'deactivé les categorie sélectionée '
        
    def view_image(self,obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.image.url))
        
        
        
@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin):

    list_display = ('titre','status','date_add','date_upd','view_image') 
    list_filter = ('status','date_add','date_upd')#les standard ou les foreignKey
    search_fields = ('titre',)#dois etre dans liste display ne pas metres de stadard prend le charField ou les relations 
    list_display_links = ('view_image','titre')# tous les elements squf les standards
    list_per_page = 3
    ordering = ['titre']
    date_hierarchy = 'date_add'
    fieldsets=[
        ('Titre et Visibibilité',{'fields':['titre','status']}),
        ('Descriptions et Image',{'fields':['description','image']}),
        ('Tag et Souscategorie',{'fields':['tag','sous_categorie']}),
    ]
    filter_horizontal =('tag','sous_categorie')
            
    actions = ('active','deactive')
            
    def active(self,request,queryset):
        queryset.update(status=True)
        self.message_user(request,'la selections a été active avec seccès')

    active.short_description = 'active les sous categorie sélectionée '
            
                
                
                
    def deactive(self,request,queryset):
        queryset.update(status=False)
        self.message_user(request,'la selections a ete désactive avec seccès')

    deactive.short_description = 'deactivé les categorie sélectionée '
            
    def view_image(self,obj):
        return mark_safe('<img src="{url}" width="100px" height="50px" />'.format(url=obj.image.url))
    
    def detaile_image(self,obj):
        return mark_safe('<img src="{url}" width="300px" height="300px" />'.format(url=obj.image.url))
            
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("nom","status")
    list_filter = ('status',)#les standard ou les foreignKey
    search_fields = ('nom',)#dois etre dans liste display ne pas metres de stadard prend le charField ou les relations 
    list_display_links = ('nom',)# tous les elements squf les standards
    