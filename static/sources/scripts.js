

// adds Cloudinary widget

function launchCloudinaryWidget() {
const uploadWidget = cloudinary.openUploadWidget(
    {
        cloud_name: 'demo',
        upload_preset: 'a5vxnzbp'
    },
    (error, result) => {
    console.log(error, result);
});

    document.getElementById("cloudinary-upload").addEventListener("click");
    uploadWidget.open();
};
