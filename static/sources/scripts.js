
// looking for any message being appended to the DOM with the class of "message"
const alertRemove = document.querySelectorAll(".message");

// timeout for alerts to go away after 5 seconds

alertRemove.forEach(function (message) {
    setTimeout(function () {
        message.remove();
    }, 4000);
});