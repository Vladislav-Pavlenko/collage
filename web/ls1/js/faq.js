const summaryBtnArrEl = document.querySelectorAll("#summary-btn-js");
const summaryDetailsArrEl = document.querySelectorAll("#details-js");

summaryBtnArrEl.forEach((item, index) => {
  item.addEventListener("click", () => {
    summaryDetailsArrEl[index].classList.toggle("active");
  });
});
