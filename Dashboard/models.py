from unittest.util import _MAX_LENGTH
from django.db import models

class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

# Create your models here.
class Barang(models.Model):
    kodebrg=models.CharField(max_length=8)
    nama=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
       return "{}. {}. {}".format(self.nama,self.kodebrg,self.harga)
    
class Member(models.Model):
    nama=models.CharField(max_length=50)
    no_hp=models.IntegerField()
    provinsi=models.CharField(max_length=20)
    kota=models.CharField(max_length=20)
    kode_pos=models.IntegerField()
    waktu_posting=models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return "{}. {}. {}".format(self.nama,self.kota, self.kode_pos)
