import zipfile

def zip_password_cracker(zip_file, wordlist):
    with zipfile.ZipFile(zip_file, 'r') as zf:
        for word in wordlist:
            try:
                zf.extractall(pwd=word.encode())
                print(f"{RED}[CRACKED]{RESET} Password found: {word}")
                return
            except:
                print(f"{YELLOW}[FAILED]{RESET} Tried {word}")

passwords = ["123456", "password", "admin", "letmein", "1234"]
zip_password_cracker("protected.zip", passwords
