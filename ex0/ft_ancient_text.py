print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print()
try:
    print("Accessing Storage Vault: ancient_fragment.txt")
    fichier = open('ancient_fragment.txt', 'r')
    print("Connection established...")
    print()
    contenue = fichier.read()
    print(contenue)
    fichier.close()
    print()
    print("Data recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("ERROR: Storage vault not found.")
