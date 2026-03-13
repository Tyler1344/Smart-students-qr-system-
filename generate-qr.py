
import qrcode

students = ["1001","1002"]

for s in students:
    img = qrcode.make(s)
    img.save(f"{s}.png")