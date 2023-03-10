# -*- coding: utf-8 -*-
"""QR_Code_Generator

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SgXaSNkDntcWwn2aY1RbFT8_GTQL0fF6
"""

!pip install segno

text = input("Text to Encode: ")
file_name = "qrcode"

import segno
qrcode = segno.make(text)

for format in ["svg", "png", "pdf"]:
  qrcode.save(
      f"{file_name}.{format}",
      scale=10,
      border = 1
  )