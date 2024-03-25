

// adds Cloudinary widget to cosplay submission page

function launchCloudinaryWidget() {
    const uploadWidget = cloudinary.openUploadWidget(
        {
            cloud_name: 'demo',
            upload_preset: 'xbunpobt'
        },
        (error, result) => {
            console.log(error, result);
        });

    document.getElementById("cloudinary-upload").addEventListener("click");
    uploadWidget.open();
};



// looking for any message being appended to the DOM with the class of "message"
const alertRemove = document.querySelectorAll(".message");

// timeout for alerts to go away after 5 seconds

alertRemove.forEach(function (message) {
    setTimeout(function () {
        message.remove();
    }, 4000);
});