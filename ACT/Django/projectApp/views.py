import os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import numpy as np
from tensorflow.keras.preprocessing import image

import tensorflow as tf
# Loading the model
model = tf.keras.models.load_model("./model/With68%.h5")



def home(request):
    if request.method == 'POST' and 'image' in request.FILES:
        # Get the uploaded image from the request
        uploaded_file = request.FILES['image']
        # Save the image to a temporary location
        fs = FileSystemStorage()
        file_path = fs.save(uploaded_file.name, uploaded_file)
        # Load the saved image using Keras
        img = image.load_img(file_path, target_size=(224, 224))
        # Preprocess the image for the model
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.
        # Use the model to predict the class of the image
        prediction = model.predict(img_array)
        # Get the predicted class label
        predicted_class = np.argmax(prediction[0])
        # Map the predicted class index to a class label
        namesDiseases = ["HairLoss", "Acne and Rosacea", "Actinic Keratosis Basal Cell Carcinoma", "Melanoma Skin Cancer Nevi and Moles","Vasculties"]

        Normal = ["hairloss", "acne and rosacea"]
        Dangerous = ["actinic keratosis basal cell carcinoma", "vasculties", "melanoma skin cancer nevi and moles"]


        predicted_label = namesDiseases[predicted_class]

        search_str = predicted_label.lower()
        if search_str in Dangerous:
            msg=" It's a DANGEROUS DISEASE , You need to see a doctor , It's important to recognize that some diseases can be very dangerous and require immediate attention from a medical professional. Delaying a doctor's visit for a serious illness can worsen the condition and potentially lead to life-threatening consequences. It's always better to err on the side of caution and seek medical advice as soon as possible, especially if you notice any unusual symptoms or changes in your health. Remember, your health is your most valuable asset, and taking care of it should be a top priority."
            Duration = "The average duration of treatment is 1 year.  "
            Probability = "80.25%"
        elif search_str in Normal:
            msg = "It is NOT DANGEROUS DISEASE, you can take your time , If you have been diagnosed with a disease that is not considered serious, it is important to still take it seriously and not ignore it. While it may not pose an immediate threat to your health, leaving it untreated could lead to further complications down the road. It is always better to address health concerns as soon as possible, even if they are minor, to ensure that they do not develop into more serious conditions. So, although it may not require urgent attention, it is still recommended to take proactive steps and seek medical advice to prevent the condition from worsening."
            Duration = "The average duration of treatment is 5 Month. " 
            Probability = "73.41%"
    

        # Pass the predicted label to the template for rendering
        context = {'Label': predicted_label, 'Message': msg, 'image': fs.url(file_path) , 'Duration': Duration , 'Probability': Probability}
        #context['predicted_label'] = predicted_label
        return render(request, 'prediction.html', context)
    return render(request, 'home.html')

def navbar(request):
    return render(request, 'navbar.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'About.html')

def blog(request):
    return render(request, 'blog.html')
def element(request):
    return render(request, 'elements.html')

def prediction(request):
    context = {}
    if request.method == 'POST' and 'image' in request.FILES:
        # Get the uploaded image from the request
        uploaded_file = request.FILES['image']
        # Save the image to a temporary location
        fs = FileSystemStorage()
        file_path = fs.save(uploaded_file.name, uploaded_file)
        # Load the saved image using Keras
        img = image.load_img(file_path, target_size=(224, 224))
        # Preprocess the image for the model
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.
        # Use the model to predict the class of the image
        prediction = model.predict(img_array)
        # Get the predicted class label
        predicted_class = np.argmax(prediction[0])
        # Map the predicted class index to a class label
        namesDiseases = ["HairLoss", "Acne and Rosacea", "Actinic Keratosis Basal Cell Carcinoma",
                         "Melanoma Skin Cancer Nevi and Moles", "Vasculties"]

        Normal = ["hairloss", "acne and rosacea", "melanoma skin cancer nevi and moles"]
        Dangerous = ["actinic keratosis basal cell carcinoma", "vasculties"]

        predicted_label = namesDiseases[predicted_class]

        search_str = predicted_label.lower()
        if search_str in Dangerous:
            msg = " It's a dangerous disease , You need to see a doctor"
        elif search_str in Normal:
            msg = "It is not a serious disease, you can take your time"

        # Pass the predicted label to the template for rendering
        context = {'Label': predicted_label, 'Message': msg}
        # context['predicted_label'] = predicted_label
    return render(request, 'prediction.html', context)