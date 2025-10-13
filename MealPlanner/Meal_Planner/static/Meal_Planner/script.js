const main_image = document.getElementById("dish_photo");
const random_btn = document.getElementById("random");
const changeImage_sect = document.getElementById("changePic_btns");
  const circles = document.querySelectorAll(".circle");
  const prevBtn = document.getElementById("previous");
  const nextBtn = document.getElementById("next");
  let currentIndex = 0;

  function updateActiveCircle() {
    circles.forEach((circle, i) => {
      circle.classList.toggle("active", i === currentIndex);
    });
  }
  
  updateActiveCircle();

  prevBtn.addEventListener("click", function() {
    currentIndex = (currentIndex - 1 + circles.length) % circles.length;
    updateActiveCircle();
  });

  nextBtn.addEventListener("click", function() {
    currentIndex = (currentIndex + 1) % circles.length;
    updateActiveCircle();
  });

random_btn.addEventListener("click", function(){
    changeImage_sect.style.display = "flex";
})


