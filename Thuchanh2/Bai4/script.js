document.querySelectorAll(".product").forEach(p =>
  p.addEventListener("click", function () {
    this.querySelector("h3").style.color =
      this.querySelector("h3").style.color === "red" ? "black" : "red";
  })
);