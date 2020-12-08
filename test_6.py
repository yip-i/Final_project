

import zipfile

secret_file = zipfile.ZipFile("Secret.zip")

password = "1234"

def main():
    try:
        secret_file.setpassword("1234".encode('ascii'))
        secret_file.extract("Secret.txt")


    except:
        print("Fail")




main()
