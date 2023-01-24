from django.db import models

# Create your models here.
class CPMSManager(models.Model):
    def create_cpms(self, name, url):
        
        cpms = CPMS()
        cpms.name = name
        cpms.url = url
        cpms.save(using=self._db)
        return cpms
    
    def get_cpms(self, id):
        return self.get(id=id)
    
    pass

class CPMS(models.Model):
 
    name = models.CharField(max_length=255, default=None, unique=True)
    url = models.CharField(max_length=255, default=None)
    
    objects = CPMSManager()
    

    REQUIRED_FIELDS = ['name', 'url']

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_url(self):
        return self.url