import os
from PIL import Image
import zpl

l = zpl.Label(20,45)
height = 2
l.origin(0,2)
l.write_text("Problem?", char_height=2, char_width=2, line_width=45, justification='C')
l.endorigin()

height += 2
image_width = 5
l.origin((l.width-image_width)/2, height)
image_height = l.write_graphic(
    Image.open(os.path.join(os.path.dirname(zpl.__file__), 'trollface-large.png')),
    image_width)
l.endorigin()

height += image_height + 2
l.origin(15, height)
l.write_barcode(height=10, barcode_type='U', check_digit='Y')
l.write_text('07000002198')
l.endorigin()

height += 5
l.origin(0, height)
l.write_text('Happy Troloween!', char_height=1, char_width=1, line_width=45,
             justification='C')
l.endorigin()

print(l.dumpZPL())
l.preview()

zpl_text = l.dumpZPL()

with open('file_to_print.txt', 'w') as file:
    file.write(zpl_text)


# os.system('lpr -P ZTC-GK420t-2 file_to_print.txt')
# zpl.FilePrinter("usb://Zebra%20Technologies/ZTC%20GK420t?serial=29J154800547")
