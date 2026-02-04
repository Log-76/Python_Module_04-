import sys


id_arch = input("id_archive")
report = sys.stdin.readline()
print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
print("Input Stream active. Enter archivist ID:", id_arch)
print("Input Stream active. Enter status report: ", report)

sys.stdout.write(f"[STANDARD] Archive status from {id_arch}: {report}")
sys.stderr.write("[ALERT] System diagnostic: Communication"
                 "channels verified\n")
sys.stdout.write("[STANDARD] Data transmission complete\n")
