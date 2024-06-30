import os

# Basic color printer
def log(hex_str, msg):
    hex_str = hex_str[1:]
    print("\033[38;2;"
          + str(int(hex_str[0] + hex_str[1], 16)) + ";"
          + str(int(hex_str[2] + hex_str[3], 16)) + ";"
          + str(int(hex_str[4] + hex_str[5], 16)) + "m" + msg)


proxies = [
    "PROXY",
    "SOCKS",
    "SOCKS4",
    "SOCKS5",
    "HTTPS"
]


def main():
    # Filepath
    log("#3cc743", "Specify path and file e.g: /home/daunita/Downloads/socks5.txt" + "\033[0m")
    path = str(input())

    # Opening file
    try:
        f = open(path, "r")
    except FileNotFoundError:
        log("#ff0000", "File not found" + "\033[0m")
        exit()
    else:
        log("#0be616", "Successfully opened file" + "\033[0m")

    # Choosing proxy type
    log("#3cc743", "Specify proxy type e.g: 4 "
                   "\n1) PROXY"
                   "\n2) SOCKS"
                   "\n3) SOCKS4"
                   "\n4) SOCKS5"
                   "\n5) HTTPS" + "\033[0m"
        )
    i = int(input())
    try:
        proxy = proxies[i - 1]
    except IndexError:
        log("#ff0000", "Bad number" + "\033[0m")
        exit()
    else:
        log("#0be616", "Proxy: " + proxy + "\033[0m")

    new = path.replace(".txt", "") + "_patched.txt"

    # Formatting and writing into file
    out = open(new, "w")
    for x in f:
        line = proxy + " " + x.strip() + ";" + "\n"
        out.write(line)
    out.close()
    f.close()

    # Remove last ; character
    b = open(new, "ab")
    b.seek(-2, 2)
    b.truncate()


main()
