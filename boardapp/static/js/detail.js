const deletebtn = document.querySelectorAll(".delete");

deletebtn.forEach((element) => {
  element.addEventListener("click", (e) => {
    e.preventDefault();

    if (confirm("정말로 삭제하시겠습니까?")) {
      location.href = e.target.dataset.url;
    }
  });
});
