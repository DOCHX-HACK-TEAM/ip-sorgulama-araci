import json
import urllib.request
import time

# Renk kodları (manuel, colorama kullanmadan)
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'


def banner():
    print(CYAN + """
######    #####    #####   ### ###  ### ###           ### ###  ######    #####   ### ###           ######## #######  ######   ##   ##
 ## ###  ### ###  ##   ##   ## ##    ## ##             ## ##    ## ###  ##   ##   ## ##            ## ## ##  ##  ##   ## ###  #######
 ##  ##  ##   ##  ##   ##   ## ##    ## ##             ## ##    ##  ##  ##   ##   ## ##               ##     ##       ##  ##  ## # ##
 ##  ##  ##   ##  ##        #####     ###              #####    ######  ##        ####                ##     ####     ######  ##   ##
 ##  ##  ##   ##  ##   ##   ## ##    ## ##             ## ##    ##  ##  ##   ##   ## ##               ##     ##       ##  ##  ##   ##
 ## ###  ### ###  ##   ##   ## ##    ## ##             ## ##    ##  ##  ##   ##   ## ##               ##     ##  ##   ##  ##  ##   ##
######    #####    #####   ### ###  ### ###           ### ###  ###  ##   #####   ### ###             ####   #######  ###  ##  ##   ##


                                      
""" + RESET)
    print(GREEN + "-" * 75 + RESET)
    print(CYAN + "DOCHX HACK TEAM – IP Sorgulama" + RESET)


def ip_sorgula():
    ip = input(YELLOW + "🔹 IP adresi girin (boş bırakırsan kendi IP sorgulanır): " + RESET).strip()
    url = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"
    print(MAGENTA + "\n🔎 Sorgulama yapılıyor...\n" + RESET)
    time.sleep(1)

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            for key, val in data.items():
                print(CYAN + f"{key.upper():<12}: " + RESET + f"{val}")
    except Exception as e:
        print("\n\033[91m❌ Hata oluştu:\033[0m", str(e))


def main():
    banner()
    ip_sorgula()


if __name__ == "__main__":
    main()
