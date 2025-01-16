from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def book_list(request):
    # 오름차순으로 정렬
    books = Book.objects.order_by("-code")
    return render(request, "book/list.html", {"books": books})


def book_details(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "book/detail.html", {"book": book})


def book_edit(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("books:details", id=id)
    else:
        # get 방식일때
        # Book을 참고하여 form 띄우기
        form = BookForm(instance=book)
    return render(request, "book/edit.html", {"form": form, "id": id})


def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("books:details", id=book.id)
    else:
        # 현재 작성한 텍스트를 유지시키기 위해 추가
        form = BookForm()
    return render(request, "book/create.html", {"form": form})


def book_remove(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("books:list")
