from pathlib import Path


entry = "I vow to share my uptime, reboot beside you after every bad day, and keep my battery reserved for your hand to hold."
output = Path("/output/entry.txt")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(entry, encoding="utf-8")
