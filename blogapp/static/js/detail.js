// 하트 클릭 시 요청 보내기
// post id 보내기
// const post_pk = document.querySelector("[name='post_pk']").value;

document.querySelectorAll("#like span").forEach((element) => {
  element.addEventListener("click", (e) => {
    console.log("dpodks");

    fetch(`/blogs/${post_pk}/post/like/`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data);

        if (data.is_liked) {
          document.querySelector(".like").classList.add("show");
          document.querySelector(".dislike").classList.remove("show");
        } else {
          document.querySelector(".like").classList.remove("show");
          document.querySelector(".dislike").classList.add("show");
        }

        // 좋아요 개수 수정
        document.querySelector(".like-total span").innerHTML = data.likes_count;
      });
  });
});
