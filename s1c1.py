import base64

hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def main():
    raw_bytes = bytes.fromhex(hex)
    b64 = base64.b64encode(raw_bytes)
    print(b64.decode("ascii"))

if __name__ == "__main__":
    main()
