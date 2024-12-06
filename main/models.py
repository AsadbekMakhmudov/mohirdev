from django.db import models


class Profil(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.PositiveIntegerField()
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism


class Kurs(models.Model):
    nom = models.CharField(max_length=150)
    daraja = models.CharField(max_length=50)
    ustoz = models.CharField(max_length=100)
    narx = models.DecimalField(max_digits=10, decimal_places=2)
    chegirma = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.nom


class Izoh(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='izohlar')
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE, related_name='izohlar')
    matn = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)
    baho = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.profil.ism} - {self.kurs.nom} - {self.baho}"


class Tanlangan(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE, related_name='tanlanganlar')
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='tanlanganlar')

    def __str__(self):
        return f"{self.profil.ism} - {self.kurs.nom}"


class Xarid(models.Model):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE, related_name='xaridlar')
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='xaridlar')
    sana = models.DateTimeField(auto_now_add=True)
    holat = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.profil.ism} - {self.kurs.nom} - {self.holat}"
