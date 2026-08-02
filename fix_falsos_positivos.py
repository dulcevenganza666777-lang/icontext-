import sys
import re

with open("icontext", "r") as f:
    content = f.read()

# 1. Separar README.md de TODOs (solo contexto, no pendientes)
# Agregar regla: si el archivo es README.md, no buscar TODOs
content = re.sub(
    r"if p.suffix in {\.py.*?} and not p.name.startswith.*?:",
    r'''if p.suffix in {".py", ".js", ".ts", ".tsx", ".jsx", ".rs", ".go", ".java", ".c", ".cpp", ".h", ".sh"} and not p.name.startswith(("fix_", "patch_", "restore_")) and p.name.lower() != "readme.md":''',
    content,
    flags=re.DOTALL
)

# 2. Ignorar .md en la detección de lenguaje principal
# Buscar la función detect_language y modificar
content = re.sub(
    r"def detect_language\(fs\):.*?return max\(exts, key=exts.get\)",
    '''def detect_language(fs):
        exts = {}
        for p in fs:
            ext = p.suffix.lower()
            # Ignorar documentación y archivos de configuración
            if ext in {".py", ".js", ".ts", ".tsx", ".jsx", ".rs", ".go", ".java", ".c", ".cpp", ".h", ".sh", ".php", ".rb"}:
                if ext:
                    exts[ext] = exts.get(ext, 0) + 1
        if not exts:
            return "No detectado (solo documentación)"
        return max(exts, key=exts.get)''',
    content,
    flags=re.DOTALL
)

# 3. Mejorar detección de "hebra" para proyectos pequeños
content = re.sub(
    r"integración general",
    "documentación / configuración inicial",
    content
)

with open("icontext", "w") as f:
    f.write(content)

print("✅ Falsos positivos corregidos")
