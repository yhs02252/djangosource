from django.shortcuts import render, redirect
from .models import Photo


def photo_list(request):

    photos = Photo.objects.all()
    return render(request, "photo/list.html", {"photos": photos})


def photo_post(request):
    if request.method == "POST":

        title = request.POST.get("title")
        auther = request.POST.get("auther")
        image = request.POST.get("image")
        description = request.POST.get("description")
        price = request.POST.get("price")

        photo = Photo(
            title=title,
            auther=auther,
            image=image,
            description=description,
            price=price,
        )
        photo.save()

        return redirect("photo_detail", id=photo.id)

    else:
        return render(request, "photo/create.html")


def photo_detail(request, id):
    photo = Photo.objects.get(id=id)
    return render(request, "photo/detail.html", {"photo": photo})


def photo_edit(request, id):
    photo = Photo.objects.get(id=id)

    if request.method == "POST":
        # 수정할 요소 가져오기
        image = request.POST.get("image")
        description = request.POST.get("description")
        price = request.POST.get("price")

        if image:
            photo.image = image

        if description:
            photo.description = description

        if price:
            photo.price = price

        photo.save()
        return redirect("photo_detail", id=id)
    else:
        return render(request, "photo/edit.html", {"photo": photo})


def photo_remove(request, id):
    photo = Photo.objects.get(id=id)
    photo.delete()
    return redirect("photo_list")
