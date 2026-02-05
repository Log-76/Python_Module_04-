print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
print()
try:
    print("Initiating secure vault access...")
    with open('classified_data.txt', 'r') as fichier:
        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION:")
        print(fichier.read(), '\n')
    with open('security_protocols.txt', 'r') as fichier:
        print("SECURE PRESERVATION:")
        print(fichier.read())
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security")
except FileNotFoundError:
    print("ERROR: Storage vault not found.")
