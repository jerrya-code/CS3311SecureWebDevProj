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

// ------------------- Login/Register Form Toggle ------------------ //
document.addEventListener("DOMContentLoaded", function() {
  const hideLoginForm = document.getElementById("toRegister_btn");
  const loginForm = document.getElementById("LoginForm");
  const registerForm = document.getElementById("RegistrateForm"); // fixed ID
  const hideRegisterForm = document.getElementById("AlreadyAccount");

  if (hideLoginForm && loginForm && registerForm) {
    hideLoginForm.addEventListener("click", function(e) {
      e.preventDefault();                // don’t submit LoginForm
      loginForm.style.display = "none";
      registerForm.style.display = "block"; //This is messing up the CSS layout (overridden)
    });
  }

  if (hideRegisterForm && loginForm && registerForm) {
    hideRegisterForm.addEventListener("click", function(e) {
      e.preventDefault();                // don’t navigate to "#"
      registerForm.style.display = "none";
      loginForm.style.display = "block";
    });
  }
});
