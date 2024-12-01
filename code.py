import qrcode

upi_Id=input("Enter your UPI ID :")


# UPI FORMAT : upi://pay?pa=upi_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE


# defining payment url based on the upi id and payment app

phonepe_url= f'upi://pay?pa={upi_Id}&pn=Recipient%20Name&mc=1234'
paytm_url= f'upi://pay?pa={upi_Id}&pn=Recipient%20Name&mc=1234'
google_pay_url= f'upi://pay?pa={upi_Id}&pn=Recipient%20Name&mc=1234'

# mc =merchent code


# Create QRCODE
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url) 
google_pay_qr=qrcode.make(google_pay_url)



# save QR code to image file
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm.png")
google_pay_qr.save("google_pay.png")



# pil or pillow use for image processing

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
