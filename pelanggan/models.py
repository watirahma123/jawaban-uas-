from django.db import models

# Create your models here.
class Jenis_Pakaian(models.Model):
    pakaian = models.CharField(max_length=40)
    keterangan = models.TextField()

    def _str_(self):
        return self.pakaian


class pelanggan (models.Model):
    Nama = models.CharField(max_length=100)
    Alamat = models.CharField(max_length=100)
    jumlah = models.IntegerField(null=True)
    Jenis_Pakaian_id = models.ForeignKey(Jenis_Pakaian, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Nama
    
