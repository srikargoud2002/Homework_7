import qrcode
import os
import argparse

def generate_qr(url, output_dir="qr_codes", filename="qrcode.png", fill_color="black", back_color="white"):
    """
    Generate a QR code with the given URL and save it to a file.
    
    Args:
        url (str): The URL to encode in the QR code
        output_dir (str): Directory to save the QR code
        filename (str): Filename for the QR code image
        fill_color (str): Color of the QR code
        back_color (str): Background color
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR Code
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    # Save the image
    file_path = os.path.join(output_dir, filename)
    img.save(file_path)
    print(f"QR code generated successfully!")
    print(f"QR code saved to: {file_path}")
    print(f"QR code links to: {url}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate a QR code for a URL')
    parser.add_argument('--url', type=str, help='URL to encode in the QR code')
    parser.add_argument('--output-dir', type=str, help='Directory to save QR code')
    parser.add_argument('--filename', type=str, help='Filename for the QR code')
    parser.add_argument('--fill-color', type=str, help='QR code color')
    parser.add_argument('--back-color', type=str, help='Background color')
    
    args = parser.parse_args()
    
    # Get values from arguments or environment variables or default values
    url = args.url or os.environ.get('QR_DATA_URL', 'https://github.com/srikargoud2002')
    output_dir = args.output_dir or os.environ.get('QR_CODE_DIR', 'qr_codes')
    filename = args.filename or os.environ.get('QR_CODE_FILENAME', 'qrcode.png')
    fill_color = args.fill_color or os.environ.get('FILL_COLOR', 'black')
    back_color = args.back_color or os.environ.get('BACK_COLOR', 'white')
    
    # Generate the QR code
    generate_qr(url, output_dir, filename, fill_color, back_color)