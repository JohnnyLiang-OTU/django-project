document.addEventListener('DOMContentLoaded', function() {
    const brandContainer = document.querySelector('.brand_container');
    const firstCard = document.querySelector('.brand_card');
    const buttonWidth = document.querySelector('.prev_button').offsetWidth;
    brandContainer.scrollLeft = firstCard.offsetWidth - buttonWidth;
});