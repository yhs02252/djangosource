from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# 자바에서 controller와 같은 개념
def todo_list(request):

    # Todo 전체 조회
    # todos = Todo.objects.all()

    # 완료되지 않은 할 일 목록 추출
    todos = Todo.objects.filter(completed=False)

    return render(
        request, "todo/list.html", {"todos": todos}
    )  # key : value 형태로 담기


def todo_detail(request, id):
    # todo 상세 조회
    todo = Todo.objects.get(id=id)
    return render(request, "todo/detail.html", {"todo": todo})


def todo_register(request):
    if request.method == "POST":

        # 폼안의 내용 개별로 가져오기 (ModelForm을 사용하지 않았을 때)
        # title = request.POST.get("title")
        # description = request.POST.get("description")
        # important = request.POST.get("important")
        # completed = request.POST.get("completed")

        # print(f"post {title}, {description}, {important}, {completed}")

        # if important:
        #     todo = Todo(title=title, description=description, important=True)
        # else:
        #     todo = Todo(title=title, description=description)

        # todo.save()

        # ModelForm 이용 시
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo_list")
    else:
        form = TodoForm()

    return render(request, "todo/create.html", {"form": form})


def todo_edit(request, id):

    todo = Todo.objects.get(id=id)

    if request.method == "POST":
        # 폼안의 내용 개별로 가져오기
        # title = request.POST.get("title")
        # description = request.POST.get("description")
        # important = request.POST.get("important")
        # completed = request.POST.get("completed")

        # print(f"post {title}, {description}, {important}, {completed}")

        # todo.title = title
        # todo.description = description

        # if important:
        #     todo.important = True
        # else:
        #     todo.important = False

        # if completed:
        #     todo.completed = True
        # else:
        #     todo.completed = False

        # todo.save()

        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_detail", id=todo.id)

    else:
        form = TodoForm(instance=todo)

    return render(request, "todo/edit.html", {"form": form})


def todo_done(request):
    # Todo 완료 목록 조회
    todos = Todo.objects.filter(completed=True)

    return render(request, "todo/done.html", {"todos": todos})
