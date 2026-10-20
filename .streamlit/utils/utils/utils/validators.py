"""File validation: signature + MIME + size checks (used in Phase 2)."""
from __future__ import annotations

ALLOWED = {
    "application/pdf": b"%PDF",
    "image/png": b"\x89PNG",
    "image/jpeg": b"\xff\xd8\xff",
}

MAX_BYTES = 10 * 1024 * 1024
MAX_PDF_PAGES = 20

def validate_upload(filename: str, content: bytes, mime: str) -> tuple[bool, str]:
    if len(content) == 0:
        return False, "File is empty."
    if len(content) > MAX_BYTES:
        return False, "File exceeds 10 MB limit."
    sig = ALLOWED.get(mime)
    if sig is None:
        return False, f"Unsupported file type: {mime}. Use PDF, PNG, or JPG."
    if not content.startswith(sig):
        return False, "File signature does not match its type. File may be corrupted or renamed."
    return True, "OK"
