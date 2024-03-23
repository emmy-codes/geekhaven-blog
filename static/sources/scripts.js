

// adds Cloudinary widget
const uploadWidget = cloudinary.openUploadWidget(
    {
        cloud_name: 'demo',
        upload_preset: 'a5vxnzbp'
    },
    (error, result) => {
    console.log(error, result)
});