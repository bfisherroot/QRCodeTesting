#REQUIRED 
# pip install pyqrcode
# pip install pypng

import pyqrcode

NAMES = ["Emily","Ella","Chloey","Owen"]


for i in range(len(NAMES)):
    QRCode = pyqrcode.create("To: %s\nLove: Mommy and Daddy" % NAMES[i])
    QRCode.svg("./images/%s" % NAMES[i], scale=8)
