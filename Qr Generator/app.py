from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML form

@app.route('/generate_qr', methods=["POST"])
def generate_qr():
    # Get the URL entered by the user
    url = request.form.get('url')

    if not url:
        return "Please enter a URL."

    # Create the QR code
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create the QR code image
    image = qr.make_image(fill='black', back_color='white')

    # Define a folder path for saving the image
    save_path = os.path.join(os.getcwd(), 'static')  # Save inside the static folder

    # Ensure the static folder exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Generate a filename for the image
    file_name = "qrcode.png"  # You can use a dynamic name based on the URL
    image_path = os.path.join(save_path, file_name)

    # Save the image to the folder
    image.save(image_path)

    # Check if the image is saved correctly by checking the file size
    if os.path.getsize(image_path) == 0:
        return "Error: Image is not generated properly. Please try again."

    # Send the image as an attachment for download
    return send_file(image_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
