from PiQR import PiQR

# define the input string for the qr code
qr_string = 'Example Text'

# generate qr binary for the input string
qr_output = PiQR.generate_qr(qr_string, correction_level='Medium')

# save qr binary as png
PiQR.show_png(qr_output, 'test.png')
