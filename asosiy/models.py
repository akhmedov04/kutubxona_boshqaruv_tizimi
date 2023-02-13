from django.db import models

class Muallif(models.Model):
    j=[("erkak","erkak"),("ayol","ayol")]
    a=[("ha","ha"),("yo'q","yo'q")]
    ism=models.CharField(max_length=50)
    yosh=models.SmallIntegerField()
    tirik=models.CharField(max_length=50,choices=a)
    kitob_soni=models.PositiveIntegerField()
    jinsi=models.CharField(max_length=50,choices=j)
    tugulgan_sana=models.DateField()
    def __str__(self):
        return self.ism
    class Meta:
        ordering = ("ism",)

class Talaba(models.Model):
    b=[(True, True), (False, False)]
    ism=models.CharField(max_length=50)
    bitiruvchi=models.BooleanField(choices=b, default=False)
    kitoblar_soni=models.PositiveIntegerField(default=0)
    kurs=models.PositiveIntegerField()
    def __str__(self):
        return self.ism
    class Meta:
        ordering = ("ism",)

class Admin(models.Model):
    ism=models.CharField(max_length=50)
    ish_vaqti=models.TimeField()
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom=models.CharField(max_length=100)
    sahifa=models.PositiveIntegerField()
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)
    janr=models.CharField(max_length=100,)
    def __str__(self):
        return self.nom

class Record(models.Model):
    s=[(True, True), (False, False)]
    talaba=models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob=models.ForeignKey(Kitob,on_delete=models.CASCADE)
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    olingan_sana=models.DateField()
    qaytarish_sanasi = models.DateField()
    qaytardi = models.CharField(max_length=50, choices=s)

class Nashriyot(models.Model):
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Kitobs(models.Model):
    nom = models.CharField(max_length=50)
    narx = models.BigIntegerField()
    kelgan_sana = models.DateField()
    nashriyot = models.ForeignKey(Nashriyot, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Sotuvchi(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=13)
    def __str__(self):
        return self.ism

class Sotuv(models.Model):
    kitob = models.ForeignKey(Kitobs, on_delete=models.CASCADE)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.CASCADE)
    sana = models.DateField()