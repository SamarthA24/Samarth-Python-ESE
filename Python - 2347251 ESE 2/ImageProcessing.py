import streamlit as st
from PIL import Image
import numpy as np

def process_image(image, operations):

    img_array = np.array(image)
    if 'Resize' in operations:
        img_array = resize_image(img_array)
    if 'Grayscale' in operations:
        img_array = grayscale_image(img_array)
    if 'Crop' in operations:
        img_array = crop_image(img_array)
    if 'Rotate' in operations:
        img_array = rotate_image(img_array)
    processed_img = Image.fromarray(img_array)
    return processed_img

def resize_image(img_array, width=300, height=300):
    img = Image.fromarray(img_array)
    resized_img = img.resize((width, height))
    return np.array(resized_img)

def grayscale_image(img_array):
    img = Image.fromarray(img_array)
    grayscale_img = img.convert('L')
    return np.array(grayscale_img)

def crop_image(img_array, crop_box=(100, 100, 400, 400)):
    img = Image.fromarray(img_array)
    cropped_img = img.crop(crop_box)
    return np.array(cropped_img)

def rotate_image(img_array, angle=45):
    img = Image.fromarray(img_array)
    rotated_img = img.rotate(angle)
    return np.array(rotated_img)

def main():
    st.title("Python ESE Image Processing")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        original_image = Image.open(uploaded_file)
        st.image(original_image, caption="Original Image", use_column_width=True)
        operations = st.multiselect(
            "Select Image Processing Techniques",
            ["Resize", "Grayscale", "Crop", "Rotate"]
        )

        if st.button("Submit"):
            processed_image = process_image(original_image, operations)
            st.image(processed_image, caption="Processed Image", use_column_width=True)

if __name__ == "__main__":
    main()
