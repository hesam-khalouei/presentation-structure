import re
from pathlib import Path

SOURCE = "project_code.txt"
OUT_DIR = Path("llm_parts")
MAX_CHARS = 180_000  # ~180KB هر بخش (امن برای Gemini)

OUT_DIR.mkdir(exist_ok=True)

text = Path(SOURCE).read_text(encoding="utf-8", errors="replace")

# الگوی درست بر اساس فایل شما:
#   =========================================
#   FILE: ./index2.html
#   =========================================
pattern = r"^=+\s*\nFILE:\s*(.+?)\s*\n=+\s*$"
parts = re.split(pattern, text, flags=re.M)
# parts[0] = مقدمه، بعدش جفت (نام, کد)

files = []
for i in range(1, len(parts), 2):
    name = parts[i].strip()
    code = parts[i+1].strip("\n")
    files.append((name, code))

print(f"تعداد فایل پیدا شد: {len(files)}")

# --- پاک‌سازی base64 (فونت/تصویر) ---
def strip_base64(s: str) -> str:
    # data:font/... base64,XXXX  یا  data:image/... base64,XXXX
    s = re.sub(
        r"data:(?:font|image)/[a-zA-Z0-9.+-]+;base64,[A-Za-z0-9+/=\s]+",
        "data:...(base64 حذف شد برای صرفه‌جویی توکن)...",
        s,
    )
    return s

files = [(n, strip_base64(c)) for n, c in files]

# --- تشخیص زبون از پسوند ---
LANG = {
    ".py": "python", ".js": "javascript", ".ts": "typescript",
    ".jsx": "jsx", ".tsx": "tsx", ".java": "java", ".kt": "kotlin",
    ".go": "go", ".rs": "rust", ".rb": "ruby", ".php": "php",
    ".c": "c", ".h": "c", ".cpp": "cpp", ".hpp": "cpp", ".cc": "cpp",
    ".cs": "csharp", ".swift": "swift", ".html": "html", ".css": "css",
    ".scss": "scss", ".json": "json", ".yaml": "yaml", ".yml": "yaml",
    ".xml": "xml", ".sql": "sql", ".sh": "bash", ".md": "markdown",
    ".toml": "toml",
}
def lang_of(name: str) -> str:
    return LANG.get(Path(name.lower()).suffix, "")

# --- ساخت بخش‌های مارک‌داون، با تقسیم فایل‌های بزرگ ---
header = (
    "# Project Source Code (Part {idx})\n\n"
    "این فایل شامل کد پروژه است. هر فایل با `=== path ===` مشخص شده "
    "و کد داخل بلوک ```lang``` است. base64 فونت/تصویر حذف شده.\n\n---\n"
)

def render(name, code):
    return f"\n=== {name} ===\n\n```{lang_of(name)}\n{code}\n```\n"

chunk_idx = 1
buf = [header.format(idx=chunk_idx)]
buf_len = len(buf[0])

def flush():
    global chunk_idx, buf, buf_len
    out = OUT_DIR / f"part_{chunk_idx:02d}.md"
    out.write_text("".join(buf), encoding="utf-8")
    print(f"✔ {out}  ({out.stat().st_size//1024} KB)")
    chunk_idx += 1
    buf = [header.format(idx=chunk_idx)]
    buf_len = len(buf[0])

for name, code in files:
    block = render(name, code)

    # اگه خود بلوک از MAX_CHARS بزرگ‌تره، تکه‌تکه کن
    if len(block) > MAX_CHARS:
        if buf_len > len(buf[0]):
            flush()
        for i in range(0, len(code), MAX_CHARS // 2):
            piece = code[i : i + MAX_CHARS // 2]
            b = render(f"{name} (ادامه {i//(MAX_CHARS//2)+1})", piece)
            buf.append(b); buf_len += len(b)
            if buf_len >= MAX_CHARS:
                flush()
        continue

    if buf_len + len(block) > MAX_CHARS:
        flush()

    buf.append(block)
    buf_len += len(block)

if buf_len > len(buf[0]):
    flush()

print(f"\n✅ تمام شد. {chunk_idx-1} فایل در پوشه {OUT_DIR}/")