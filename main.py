# Import necessary libraries
import qrcode  # Library for generating QR codes
from PIL import Image  # Python Imaging Library for image processing
import os  # Operating system module for file path operations
import uuid  # Universally Unique Identifier module for generating unique identifiers

# Get user input for the data to be encoded in the QR code
string = input("Please enter a string: ")

# Create a QR code instance with specified settings
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(string)

# Generate the QR code
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="black")

# Get the current working directory
current_directory = os.getcwd()

# Specify the base filename for the QR code image
base_filename = "myqrcode.png"

# Use the first 8 characters of a UUID for uniqueness
unique_identifier = str(uuid.uuid4())[:8]
qr_code_filename = f"{base_filename[:-4]}_{unique_identifier}.png"
full_path = os.path.join(current_directory, qr_code_filename)

# Save the QR code image in the current directory
img.save(full_path)

# Print the path where the QR code image is saved
print(f"QR code saved as {full_path}")

# Pause execution with an input prompt to keep the console window open
input('Good Bye.')
