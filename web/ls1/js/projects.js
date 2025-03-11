const listEl = document.querySelector("#projects-list-js");
const btnEl = document.querySelector("#load-more-btn-js");

function showProjects() {
  let counter = 0;
  const children = listEl.children;
  const childArray = Array.from(children);

  childArray.forEach((child) => {
    if (counter < 3 && !child.classList.contains("visible")) {
      child.classList.add("visible");
      counter++;
    }
  });
  if (childArray.every((child) => child.classList.contains("visible"))) {
    btnEl.classList.add("hidden");
    return;
  }
}

btnEl.addEventListener("click", showProjects);
