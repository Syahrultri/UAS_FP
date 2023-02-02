from django.shortcuts import render, redirect
from Dashboard.forms import FormBarang
from Dashboard.models import Barang
from Dashboard.forms import FormMember
from Dashboard.models import Member
from django.contrib import messages

# Create your views here.

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

def Member_View(request):
    members=Member.objects.all()

    konteks={
        'members':members,
    }
    return render(request,'tampil_mbr.html',konteks)

def tambah_barang(request):
    if request.POST:
        form= FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormBarang()
            konteks = {
                'form': form,
            }
            return redirect(request,'tambah_barang.html',konteks)

    else:
        form=FormBarang()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_barang.html',konteks)

def tambah_member(request):
    if request.POST: 
        form= FormMember(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormMember()
            konteks = {
                'form': form,
            }
            return redirect(request,'tambah_member.html',konteks)

    else:
        form=FormMember()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_member.html',konteks)

def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form= FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubah_brg',id_barang=id_barang)

    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs':barangs
        }
    return render(request,'ubah_brg.html',konteks)

def ubah_mbr(request,id_member):
    members=Member.objects.get(id=id_member)
    if request.POST:
        form= FormMember(request.POST,instance=members)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubah_mbr',id_member=id_member)

    else:
        form=FormMember(instance=members)
        konteks = {
            'form':form,
            'members':members
        }
    return render(request,'ubah_mbr.html',konteks)

# def tambah_barang(request):
#     titelnya="Barang"
#     form=FormBarang()
#     konteks={
#         'form':form,
#         'titel':titelnya,
#     }
#     return render(request,'tambah_barang.html',konteks)


def tampil_barang(request):
    titelnya="Tampilan_Barang"
    form=FormBarang()
    konteks={
        'form':form,
        'titel':titelnya,
    }
    return render(request,'tampil_brg.html',konteks)

def tampil_member(request):
    titelnya="Tampilan_Member"
    form=FormMember()
    konteks={
        'form':form,
        'titel':titelnya,
    }
    return render(request,'tampil_mbr.html',konteks)

def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html',konteks)

def laptop(request):
    titelnya="Laptop"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk1.html',konteks)

def kontak(request):
    titelnya="Kontak"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'kontak.html',konteks)

def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data Terhapus")
    return redirect('Vbrg')

def hapus_mbr(request,id_member):
    members=Member.objects.filter(id=id_member)
    members.delete()
    messages.success(request,"Data Terhapus")
    return redirect('Vmbr')