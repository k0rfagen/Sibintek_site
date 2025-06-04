const images = document.querySelectorAll('img');
let currentIndex = 0;

function showImage(index) {
  images[currentIndex].classList.remove('active');
  images[index].classList.add('active');
  currentIndex = index;
}

document.querySelector('.prev').addEventListener('click', () => {
  if (currentIndex > 0) {
    showImage(currentIndex - 1);
  }
})

document.querySelector('.next').addEventListener('click', () => {
  if (currentIndex < images.length - 1) {
    showImage(currentIndex + 1);
  }
})

showImage(currentIndex);