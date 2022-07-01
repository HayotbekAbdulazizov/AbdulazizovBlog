/*!
* Start Bootstrap - Simple Sidebar v6.0.5 (https://startbootstrap.com/template/simple-sidebar)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-simple-sidebar/blob/master/LICENSE)
*/
// 
// Scripts
// 

$('#myTab a').on('click', function (e) {
    e.preventDefault()
    $(this).tab('show')
  })

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle')
    const sidebarToggle2 = document.body.querySelector('#sidebarToggle2')
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes  
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

    if (sidebarToggle2) {
      // Uncomment Below to persist sidebar toggle between refreshes  
      // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
      //     document.body.classList.toggle('sb-sidenav-toggled');
      // }
      sidebarToggle2.addEventListener('click', event => {
          event.preventDefault();
          document.body.classList.toggle('sb-sidenav-toggled');
          localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
      });
  }

});





































































// let items = document.querySelectorAll('.carousel .carousel-item')

// items.forEach((el) => {
//     const minPerSlide = 4
//     let next = el.nextElementSibling
//     for (var i=1; i<minPerSlide; i++) {
//         if (!next) {
//             // wrap carousel by using first child
//         	next = items[0]
//       	}
//         let cloneChild = next.cloneNode(true)
//         el.appendChild(cloneChild.children[0])
//         next = next.nextElementSibling
//     }
// })

















// let items = document.querySelectorAll('.carousel .carousel-item')
// console.log(items)

// items.forEach((el) => {
//   console.log(el, "Element")
//     const minPerSlide = 4
//     let next = el.nextElementSibling
//     console.log(next, "Element")

//     for (var i=1; i<minPerSlide; i++) {
//         if (!next) {
//             // wrap carousel by using first child
//         	next = items[0]
//       	}
//         let cloneChild = next.cloneNode(true)
//         // console.log(
//           // cloneChild, "Clone Child"
//         // )
//         el.appendChild(cloneChild.children[0])
//         next = next.nextElementSibling
//     }
// })





















































$(document).ready(function() {
  var owl = $('.owl-carousel');
  owl.owlCarousel({
    loop: false,
    nav: true,
    margin: 18,
    responsive: {
      0: {
        items: 2
      },
      600: {
        items: 3
      },
      960: {
        items: 4
      },
      1300: {
        items: 5
      }
    }
  });
  owl.on('mousewheel', '.owl-stage', function(e) {
    if (e.deltaY > 0) {
      owl.trigger('next.owl');
    } else {
      owl.trigger('prev.owl');
    }
    e.preventDefault();
  });
})