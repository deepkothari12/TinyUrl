import qrcode
import os
import qrcode.constants
import io
import base64


class QRGENRATOR:
    def QRgenrator(self , Short_url):

        file_path = "D:/Vs.code/.vscode/tignyUrl/qrcode.png"

        # Ensure directory exists if saving in a folder (Optional)
        #os.makedirs("static/qrcodes", exist_ok=True)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,  # Adjust for better visibility
            border=2,
        )

        qr.add_data(Short_url)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")

        buffer = io.BytesIO()
        img.save(buffer, format= 'png') # type: ignore
        qr_code_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        # img.save(file_path)  # type: ignore

        # print(f"QR Code saved successfully at {file_path} ")
        return qr_code_base64