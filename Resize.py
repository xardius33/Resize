from PIL import Image

# Open the image file
image_path = "image.jpg"  # Replace with your image file path
image = Image.open(image_path)

# Display the original image size
print("Original Image Size:", image.size)

# Specify the desired width and height for the resized image
new_width = 800
new_height = 600

# Resize the image
resized_image = image.resize((new_width, new_height))

# Display the resized image size
print("Resized Image Size:", resized_image.size)

# Save the resized image
output_path = "resized_image.jpg"  # Replace with your desired output path
resized_image.save(output_path)

print("Resized image saved successfully.")
