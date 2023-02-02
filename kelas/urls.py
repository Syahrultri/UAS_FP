
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from Dashboard.views import produk, laptop, kontak, tambah_barang, Barang_View, ubah_brg, ubah_mbr, tambah_member, Member_View, hapus_brg, hapus_mbr


def coba1(request):
    return HttpResponse('Selamat Datang')

def coba2(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'index.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',coba2),
    path('produk/',produk),
    path('produk1/',laptop),
    path('kontak/',kontak),
    path('addbrg/',tambah_barang),
    path('Vbrg/',Barang_View, name='Vbrg'),
    path('addmbr/',tambah_member),
    path('Vmbr/',Member_View, name='Vmbr'),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
    path('ubah1/<int:id_member>',ubah_mbr,name='ubah_mbr'),
    path('hapus/<int:id_barang>',hapus_brg,name='hapus_brg'),
    path('hapus1/<int:id_member>',hapus_mbr,name='hapus_mbr'),
]
