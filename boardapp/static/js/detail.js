const deletebtn = document.querySelectorAll(".delete");
const actionForm = document.querySelector("#actionForm");

// 목록으로 클릭시 actionForm 보내기
document.querySelector(".btn-success").addEventListener("click", (e) => {
  actionForm.submit();
});

deletebtn.forEach((element) => {
  element.addEventListener("click", (e) => {
    e.preventDefault();

    if (confirm("정말로 삭제하시겠습니까?")) {
      location.href = e.target.dataset.url;
    }
  });
});
