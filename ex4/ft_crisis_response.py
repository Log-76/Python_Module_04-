print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
try:
    with open('lost_archive.txt', 'r') as fichier:
        print(fichier.read())
except FileNotFoundError:
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")
try:
    with open('classified_vault.txt', 'r') as fichier:
        fichier.write("fdd")
except Exception:
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")
try:
    with open('standard_archive.txt', 'r') as fichier:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        print("SUCCESS: Archive recovered - ''", fichier.read(), "''")
        print("STATUS: Normal operations resumed")
except FileNotFoundError:
    print("ERROR: Storage vault not found.")
