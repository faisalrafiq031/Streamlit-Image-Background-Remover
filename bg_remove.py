# Made with 💛 By Faisal Rafiq


# pip install streamlit rembg pillow 

import streamlit as st
from rembg import remove
from PIL import Image
import io

# Title of the app
st.title("Remove Background from Image")

# Upload image file
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpeg", "jpg"])

if uploaded_file:
    # Open image using PIL
    image = Image.open(uploaded_file)

    # Display uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Color Picker for background color
    bg_color = st.color_picker("Pick a Background Color", "#ffffff")

    # Button to process the image
    if st.button("Upload & Process"):
        # Remove background
        output = remove(image)

        # Create a new background image with the selected color
        bg_image = Image.new("RGB", output.size, bg_color)
        
        # Paste the foreground onto the new background
        bg_image.paste(output, (0, 0), output)

        # Save and display the result
        output_path = "output_with_bg_color.png"
        bg_image.save(output_path)

        # Show the final image
        st.image(bg_image, caption="Processed Image", use_column_width=True)

        # Provide a download button for the result
        with open(output_path, "rb") as file:
            st.download_button(label="Download Image", data=file, file_name="output_with_bg_color.png")
