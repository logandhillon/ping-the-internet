"""
IP Address Storage Agent Client
(c) 2024 Logan Dhillon
"""
STORE_NAME = "ipdb.txt"


def add_ip(ip: str) -> None:
    with open(STORE_NAME, 'a') as f:
        f.write(ip+'\n')


def get_all():
    with open(STORE_NAME, 'r') as f:
        return f.readlines()


def main() -> None:
    from base64 import b64decode
    print(b64decode("SVAgQWRkcmVzcyBTdG9yYWdlIEFnZW50IENsaWVudAooYykgMjAyNCBMb2dhbiBEaGlsbG9uCg==").decode())
    ip = input(f"IP address to add to store? ")

    if ip == '':
        print("No IP address was inputted, exiting")
        exit(0)

    add_ip(ip)


if __name__ == "__main__":
    main()
