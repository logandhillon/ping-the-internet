"""
Legacy IP Address Storage Conversion Agent
(c) 2024 Logan Dhillon. All rights reserved.
"""
import os
import ipsa


def main() -> None:
    from base64 import b64decode
    print(b64decode("TGVnYWN5IElQIEFkZHJlc3MgU3RvcmFnZSBDb252ZXJzaW9uIEFnZW50CihjKSAyMDI0IExvZ2FuIERoaWxsb24K").decode())
    store_dir = input(f"Where is the legacy store located? [out] ") or "out"
    print(f"Found {len(os.listdir(store_dir))} item(s)")

    files = [entry for entry in os.listdir(
        store_dir) if os.path.isfile(os.path.join(store_dir, entry))]

    for file in files:
        path = os.path.join(store_dir, file)
        with open(path, 'r') as f:
            contents = f.read()
            print(f"Found {contents} at {path}, writing now")
            ipsa.add_ip(contents)


if __name__ == "__main__":
    main()
