import re
from pathlib import Path

content = Path("project_code.txt").read_text(encoding="utf-8")

# جدا کردن بخش‌ها با همون الگوی قبلی
parts = re.split(r"^===\s*(.+?)\s*===\s*$", content, flags=re.M)

# پسوند فایل → اسم زبون برای نمایش
LANG_MAP = {
    ".py": "python", ".js": "javascript", ".ts": "typescript",
    ".jsx": "jsx", ".tsx": "tsx", ".java": "java", ".kt": "kotlin",
    ".go": "go", ".rs": "rust", ".rb": "ruby", ".php": "php",
    ".c": "c", ".h": "c", ".cpp": "cpp", ".hpp": "cpp", ".cc": "cpp",
    ".cs": "csharp", ".swift": "swift", ".m": "objectivec",
    ".html": "html", ".css": "css", ".scss": "scss",
    ".json": "json", ".yaml": "yaml", ".yml": "yaml",
    ".xml": "xml", ".sql": "sql", ".sh": "bash",
    ".md": "markdown", ".txt": "text", ".toml": "toml",
    ".env": "bash", ".dockerfile": "dockerfile",
}

def lang_of(name: str) -> str:
    p = name.lower()
    if p.endswith("dockerfile") or p == "dockerfile":
        return "dockerfile"
    if p.endswith("makefile") or p == "makefile":
        return "makefile"
    suffix = Path(p).suffix
    return LANG_MAP.get(suffix, "")

output = []
output.append("# Project Source Code\n")
output.append("این فایل شامل کد کامل پروژه است. هر فایل با هدر `=== path/to/file ===` مشخص شده.\n")
output.append(f"تعداد فایل‌ها: {len(parts)//2}\n")
output.append("\n---\n")

for i in range(1, len(parts), 2):
    name = parts[i].strip()
    code = parts[i+1].strip("\n")
    lang = lang_of(name)

    output.append(f"\n=== {name} ===\n")
    output.append(f"```{lang}\n{code}\n```\n")

Path("project_for_llm.md").write_text("".join(output), encoding="utf-8")
print(f"ساخته شد: project_for_llm.md ({len(parts)//2} فایل)")