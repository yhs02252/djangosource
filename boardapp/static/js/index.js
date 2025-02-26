const actionForm = document.querySelector("#actionForm");
const searchbtn = document.querySelector("#searchbtn");

// .page-link 클릭 시 a 태그 기능 중지
// page 번호 가져온 후 actionForm 안의 페이지 값 변경
// actionForm 보내기
document.querySelector(".pagination").addEventListener("clicl", (e) => {
  e.preventDefault();
  actionForm.page.value = e.target.getAttribute("href");
  actionForm.action = "/board";
  actionForm.submit();
});

// 제목 클릭 시 a 태그 중지
// actionForm
document.querySelector("tbody a").addEventListener("click", (e) => {
  e.preventDefault();

  actionForm.action = e.target.getAttribute("href");
  actionForm.submit();
});

// 정렬기준 change 일어나면
document.querySelector(".so").addEventListener("change", (e) => {
  // 사용자가 선택한 value 가져온 후 actionForm so 필드 값 변경
  actionForm.so.value = e.target.value;
  // actionForm 보내기
  actionForm.submit();
});

// 찾기 버튼 클릭 시(검색)
searchbtn.addEventListener("click", () => {
  // actionForm 보내기 - 사용자가 입력한 keyword를 actionForm 의 keyword 값으로 변경
  // page - 1 변경
  actionForm.keyword.value = document.querySelector("[name='keyword']").value;
  actionForm.page.value = 1;
  actionForm.action = "/board";
  actionForm.submit();
});
