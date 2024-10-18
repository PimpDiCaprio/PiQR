from pyqr import PyQR

# define the input string for the qr code
qr_string = 'Example Text'

# Create a QReader instance
pqr = PyQR.QR()

# generate qr binary for the input string
qr_output = pqr.generate_qr(qr_string, correction_level='Medium')

# save qr binary as png
PyQR.show_png(qr_output, 'test.png')
