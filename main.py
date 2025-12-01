import qrcode

def main():

    data = input("Please enter web address:").lower()

    qr = qrcode.QRCode(
        version=1, #Controls the size o the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L, #Error correction level
        box_size=10, # Size of each box (pixel) in the QR code
        border =4, #Thickness of the border
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save("my_qrcode.png")

    print("QR code generated and saved as my_qrcode.png")

if __name__ == "__main__":
    main() 