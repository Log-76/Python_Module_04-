print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
print()
"""
open('new_discovery.txt', 'w+',) creer un fichier
fichier.write('') permet d ecrire dedans
fichier.seek(0) permet de revenir au debut fichier
fichier.read() permet de lire le contenue
fichier.close() permet de fermer
"""

fichier = open('new_discovery.txt', 'w+',)
print("Initializing new storage unit:", fichier.name)
print("Storage unit created successfully...")
print()
fichier.write('[ENTRY 001] New quantum algorithm discovered\n')
fichier.write('[ENTRY 002] Efficiency increased by 347%\n')
fichier.write('[ENTRY 003] Archived by Data Archivist trainee\n')
fichier.seek(0)
print(fichier.read())
fichier.close()
print("Data inscription complete. Storage unit sealed.")
print(f"Archive '{fichier.name}' ready for long-term preservation.")
