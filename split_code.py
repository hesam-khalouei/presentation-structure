import re
from pathlib import Path

content = Path("project_code.txt").read_text(encoding="utf-8")

# فرض: هر بخش با خطی مثل === path/to/file.py === شروع می‌شه
parts = re.split(r"^===\s*(.+?)\s*===\s*$", content, flags=re.M)
# parts = ['', 'file1.py', 'code1...', 'file2.py', 'code2...', ...]

for i in range(1, len(parts), 2):
    name = parts[i].strip().replace("/", "_")
    Path(f"out_{name}").write_text(parts[i+1], encoding="utf-8")

print("done!")