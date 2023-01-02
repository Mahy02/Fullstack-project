// function test() {
//     alert("Hello from a static file!");
//   };
// const container = document.querySelector('.containerr');
// const seats = document.querySelectorAll('.row .seat:not(.occupied)');
// const count = document.getElementById('count');
// const total = document.getElementById('total');
// const movieSelect = document.getElementById('movie');
// print("hhhhhhhhhhhhhhhhhhhhhhh")
// let ticketPrice = +500;

// //Update total and count
// function updateSelectedCount() {
//     const selectedSeats = document.querySelectorAll('.row .seat.selected');
//     const selectedSeatsCount = selectedSeats.length;
//     count.innerText = selectedSeatsCount;
//     total.innerText = selectedSeatsCount * ticketPrice;
//     print("first")
// }

// //Movie Select Event
// movieSelect.addEventListener('change', e => {
//     ticketPrice = +e.target.value;
//     updateSelectedCount();
//     print("sec")
// });

// //Seat click event
// container.addEventListener('click', e => {
//     if (e.target.classList.contains('seat') &&
//         !e.target.classList.contains('occupied')) {
//         e.target.classList.toggle('selected');
//         console.log("hi");
//     }
//     updateSelectedCount();
//     print("third")
// });
