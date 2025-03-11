const menuEl = document.querySelector("#menu-js");
const menuBtnEl = document.querySelector("#menu-btn-js");
const iconOpenEl = document.querySelector("#icon-open-js");
const iconCloseEl = document.querySelector("#icon-close-js");

menuBtnEl.addEventListener("click", () => {
  if (menuEl.classList.contains("hidden")) {
    menuEl.classList.remove("hidden");
    iconOpenEl.classList.add("hidden");
    iconCloseEl.classList.remove("hidden");
    document.body.style.overflow = "hidden";
  } else {
    menuEl.classList.add("hidden");
    iconOpenEl.classList.remove("hidden");
    iconCloseEl.classList.add("hidden");
    document.body.style.overflow = "auto";
  }
});
