from django.db import models

# Create your models here.

class curso(models.Model):
    
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    creditos = models.IntegerField()
    
    class Meta:
        
        verbose_name_plural = "Curos"
    
    def __str__(self):
        return self.nombre  
        
