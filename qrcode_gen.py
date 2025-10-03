#!/usr/bin/env python3
import qrcode
import sys
import os

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr.print_ascii(invert=True)
    print("\n")  # Optional separation

def main():
    if len(sys.argv) < 2:
        print("Usage: python qrcode_cli.py <text_or_file.txt>")
        sys.exit(1)

    input_arg = sys.argv[1]

    if os.path.isfile(input_arg):
        # Read entire file content as one string
        with open(input_arg, "r", encoding="utf-8") as f:
            data = f.read().strip()
        if data:
            print(f"QR for content of: {input_arg}")
            generate_qr(data)
        else:
            print("File is empty.")
    else:
        # Treat it as a single string input
        generate_qr(input_arg)

if __name__ == "__main__":
    main()
