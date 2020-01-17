import re

# myenc = "utf-16BE"

with open(path) as f:
    ifc_text = f.read()

# ddd = aaa.decode(myenc)
# a = "0\xd30\xeb0\xc70\xa30\xf30\xb00\xde0\xc60\xea0\xa20\xeb"
# # b'0\xd30\xeb0\xc70\xa30\xf30\xb00\xde0\xc60\xea0\xa20\xeb'

ppp = re.findall(r'30..', s)

# print(hex(ord("ビ")))
# print(0x30d3)
# print(0x30eb)

# reg \\x2\\.*?\\X0\\

for i in ppp:
    print(chr(int(i, 16)))