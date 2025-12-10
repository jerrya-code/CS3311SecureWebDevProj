const filterSelect = document.getElementById('filter');

filterSelect.addEventListener('change', function() {
    const value = this.value.toLowerCase();
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        let show = true;

        if (value === "gluten free" && card.dataset.gluten !== "True") show = false;
        if (value === "dairy free" && card.dataset.dairy !== "True") show = false;
        if (value === "nut free" && card.dataset.nut !== "True") show = false;
        if (value === "vegetarian" && card.dataset.vegetarian !== "True") show = false;
        
        card.style.display = show ? "flex" : "none";
    });
});

// ------------------ Side Bar Shopping Cart ------------------- //
function openCart() {
  document.getElementById("shopping_cart").style.width = "535px";
  document.getElementById("overlay_background").classList.add("active");
}

function closeCart() {
  document.getElementById("shopping_cart").style.width = "0";
  document.getElementById("overlay_background").classList.remove("active");
}

document.getElementById("overlay_background").addEventListener("click", closeCart);