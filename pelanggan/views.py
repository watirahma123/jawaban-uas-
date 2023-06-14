from django.shortcuts import render

def pelanggan(request):
    about = ["No Identitas", "Nama", "Alamat"]
    pemilik = "__laundry saya__"

    konteks = {
        'title': about,
        'pemilik': pemilik,
    }


    return render(request, 'pelanggan.html', konteks)