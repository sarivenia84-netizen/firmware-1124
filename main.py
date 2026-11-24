from pathlib import Path

# The joke treats a robot's emergency reboot as a honeymoon, while encryption and a warm charging port keep the vow tender.
entry = "I promise to keep your secrets encrypted, your hand warm in my charging port, and reboot beside you—because every marriage needs a restart."
output = Path("/output/entry.txt")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(entry, encoding="utf-8")
