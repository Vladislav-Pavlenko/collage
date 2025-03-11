const reviewsArrEl = document.querySelectorAll("#slide-js");
const prevBtnEl = document.querySelector("#prev-btn-js");
const nextBtnEl = document.querySelector("#next-btn-js");

const checkButton = () => {
  const lastIndex = reviewsArrEl.length - 1;
  const activeIndex = [...reviewsArrEl].findIndex((item) =>
    item.classList.contains("active")
  );

  prevBtnEl.classList.toggle("disable", activeIndex === 0);
  nextBtnEl.classList.toggle("disable", activeIndex === lastIndex);
};

nextBtnEl.addEventListener("click", () => {
  let idxActiveElement = [...reviewsArrEl].findIndex((item) =>
    item.classList.contains("active")
  );

  if (idxActiveElement < reviewsArrEl.length - 1) {
    reviewsArrEl[idxActiveElement].classList.remove("active");
    reviewsArrEl[idxActiveElement + 1].classList.add("active");
    checkButton();
  }
});

prevBtnEl.addEventListener("click", () => {
  let idxActiveElement = [...reviewsArrEl].findIndex((item) =>
    item.classList.contains("active")
  );

  if (idxActiveElement > 0) {
    reviewsArrEl[idxActiveElement].classList.remove("active");
    reviewsArrEl[idxActiveElement - 1].classList.add("active");
    checkButton();
  }
});

checkButton();
