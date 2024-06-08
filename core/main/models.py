from django.db import models

# Create your models here.
class Yerkir(models.Model):
    name = models.CharField("Yerkri anuny",max_length =250)
    img = models.ImageField("Yerkri nkary",upload_to ="yerkir/")
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name="Yerkir"
        verbose_name_plural="Yerkrner"

class  Qaxaq(models.Model):
    Yerkir=models.ForeignKey(Yerkir,on_delete=models.CASCADE,related_name="yer_qaxaq")
    name = models.CharField("Qaxaqi anuny",max_length =250)
 
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name="Qaxaq"
        verbose_name_plural="Qaxaqner"        

class  Poxoc(models.Model):
    Qaxaq=models.ForeignKey(Qaxaq,on_delete=models.CASCADE,related_name="yer_poxoc")
    name = models.CharField("Poxoci anuny",max_length =250)
 
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name="Poxoc"
        verbose_name_plural="Poxocner"        

class  Shenq(models.Model):
    Poxoc=models.ForeignKey(Poxoc,on_delete=models.CASCADE,related_name="yer_shenq")
    name = models.CharField("Shenqi hamary",max_length =250)
 
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name="Shenq"
        verbose_name_plural="Shenqer"

class  Bnakaran(models.Model):
    
    Shenq=models.ForeignKey(Shenq,on_delete=models.CASCADE,related_name="yer_bnakaran")
    name = models.CharField("Bnakarani hamary",max_length =250)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name="Bnakaran"
        verbose_name_plural="Bnakaranner"

class  Molorak(models.Model):
    
    Bnakaran=models.ForeignKey(Bnakaran,on_delete=models.CASCADE,related_name="yer_molorak")
    name = models.CharField("Molorak hamary",max_length =250)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name="Molorak"
        verbose_name_plural="Molorakner"

class Support(models.Model):
    email=models.EmailField("sex_boomb")
    text =models.TextField("sex")
    def __str__(self) -> str:
        return self.email
    