from PIL import Image, ImageFilter

def upscale_image(input_path, output_path, scale_factor):
    # Open the image
    original_image = Image.open(input_path)

    # Get the original width and height
    original_width, original_height = original_image.size

    # Calculate the new width and height after scaling
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    # Use the resize function to upscale the image
    upscaled_image = original_image.resize((new_width, new_height))

    # Save the upscaled image
    upscaled_image.save(output_path)

# Example usage:
input_image_path = r"C:\Users\diyan\Downloads\sympop__1_-removebg-preview (1).png"
output_image_path = r"C:\Users\diyan\Downloads\sympop_1.png"
scale_factor = 2  # Adjust the scale factor as needed

upscale_image(input_image_path, output_image_path, scale_factor)
