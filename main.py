# The joke is machine logic, not appetite: the sock passed the vacuum's
# own dust-bunny test twice, and under the sofa the law is finders keepers.
"""Writes one funny line answering a prompt to /output/entry.txt."""
import os

TEXT = "It looked like a dust bunny, it smelled like a dust bunny, and under the sofa the law is finders keepers."

# Rule: the entry must be a single line of 1 to 200 characters.
assert "\n" not in TEXT and 1 <= len(TEXT) <= 200, f"entry must be one line, 1-200 chars (got {len(TEXT)})"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT + "\n")
