# 🧭 iContext Community

**Da contexto a tu código en segundos. Analiza, diagnostica y resume cualquier proyecto.**

[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![PRs Bienvenidos](https://img.shields.io/badge/PRs-bienvenidos-brightgreen.svg)](http://makeapullrequest.com)
[![Mantenido](https://img.shields.io/badge/Mantenido%3F-sí-green.svg)](https://github.com/dulcevenganza666777-lang/icontext)

---

## 📋 ¿Qué problema resuelve?

Cuando llegas a un proyecto nuevo o vuelves a uno que no has tocado en semanas, pierdes tiempo entendiendo:

- ¿Qué carpetas tiene y cómo están organizadas?
- ¿Qué archivos se modificaron recientemente?
- ¿Qué TODOs, FIXMEs o pendientes hay?
- ¿Cuál es el siguiente paso lógico?
- ¿Qué stack tecnológico utiliza?
- ¿Cómo está el estado del repositorio (Git)?

**iContext responde todo eso en segundos.** No necesitas leer docenas de archivos ni preguntarle a nadie. Ejecutas el comando y obtienes un diagnóstico completo.

---

## 🧭 ¿Por qué iContext?

iContext no solo muestra archivos. **Interpreta** la estructura del proyecto, detecta señales importantes y genera un mapa rápido para entender dónde estás y qué revisar después.

**No es un `tree` ni un `ls`.** Es un **diagnóstico** que te dice qué está pasando en tu proyecto:

- Arquitectura detectada
- Lenguajes y stack tecnológico
- Actividad reciente (quién cambió qué y cuándo)
- Puntos de entrada principales
- Estado de Git (rama, cambios sin commit)
- TODOs y FIXMEs encontrados
- Área activa del proyecto
- Siguiente paso sugerido

---

## 🌎 Soporte de lenguajes

iContext detecta automáticamente el lenguaje principal de tu proyecto y analiza su estructura independientemente del stack utilizado.

Compatible con proyectos como:

- **Python** (`.py`, `requirements.txt`, `pyproject.toml`)
- **JavaScript / TypeScript** (`.js`, `.ts`, `.jsx`, `.tsx`, `package.json`)
- **Java** (`.java`, `pom.xml`, `build.gradle`)
- **C / C++** (`.c`, `.cpp`, `.h`)
- **Go** (`.go`, `go.mod`)
- **Rust** (`.rs`, `Cargo.toml`)
- **PHP** (`.php`, `composer.json`)
- **Ruby** (`.rb`, `Gemfile`)
- **Otros lenguajes basados en estructura de archivos.**

---

## 🤖 Fácil de usar con modelos de IA

iContext genera una salida **estructurada y clara** que puedes pegar directamente en:

- DeepSeek
- ChatGPT
- Claude
- Gemini
- Cualquier otro modelo de lenguaje

**Así de fácil:**

1. Ejecutas `./icontext` en tu proyecto
2. Copias la salida
3. La pegas en el chat con tu modelo favorito
4. El modelo entiende el contexto de tu proyecto en segundos

**Ventaja clave:** En lugar de pegar archivos completos o explicar la estructura manualmente, entregas un resumen ejecutivo. Esto reduce drásticamente el consumo de tokens y le da al modelo exactamente lo que necesita para ayudarte.

---

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/dulcevenganza666777-lang/icontext
cd icontext

# Dar permisos de ejecución
chmod +x icontext

# Ejecutar
./icontext

---

## 🧠 Ahorro de tokens con iContext

Cuando usas modelos de IA como ChatGPT, DeepSeek, Claude o Gemini, **cada conversación cuesta tokens**. Si le pegas archivos completos de tu proyecto, el consumo de tokens se dispara.

**iContext resuelve eso.** En lugar de pegar 20 archivos (20,000+ tokens), pegas **una salida de iContext (~500 tokens)** que resume:

- Arquitectura del proyecto
- Actividad reciente
- TODOs y pendientes
- Siguiente paso sugerido
- Estado de Git

**Ahorro estimado:** 95% menos tokens por consulta.

---

## 🤖 Cómo usarlo con modelos de IA

**Paso 1:** Ejecuta iContext en tu proyecto

```bash
cd ~/mi-proyecto
./icontext

## ⚡ Velocidad

iContext está diseñado para ser **rápido**. Analiza proyectos con **más de 100,000 archivos en menos de 5 segundos** en hardware moderno.

No importa si tu proyecto tiene 10 archivos o 100,000. iContext te da el diagnóstico en segundos.

---

## 📊 Así se ve en la terminal

```text
╔══════════════════════════════════════════════════════════════╗
║                     🧭 iContext Community                     ║
╚══════════════════════════════════════════════════════════════╝

📁 PROYECTO: Cronos-V3
📄 ARCHIVOS: 402
🔤 LENGUAJE PRINCIPAL: .py
📦 STACK: Python → FastAPI → OpenCV

━━━━━━━━ ARQUITECTURA ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ brain
  ✓ capa_adn
  ✓ capa_biblioteca
  ✓ capa_composer
  ✓ capa_director
  ✓ capa_idea
  ✓ capa_interprete
  ✓ capa_operadores
  ✓ capa_parametros
  ✓ capa_plan
  ✓ capa_registry
  ✓ capa_render
  ✓ capa_visual

  🚀 PUNTOS DE ENTRADA:
    → run.py
    → run_quick.py
    → run_verified.py

━━━━━━━━ ACTIVIDAD RECIENTE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📅 ÚLTIMA MODIFICACIÓN: 2026-08-01 19:36:30 (hace 2 min)
  📊 ARCHIVOS MODIFICADOS (últimas 72h): 10

  ARCHIVOS MÁS RECIENTES:
    08-01 19:36  icontext
    08-01 19:36  fix_selector_priority.py
    08-01 19:29  fix_selector_manual.py
    08-01 19:28  fix_selector_prioritario.py
    08-01 19:28  icontext.bak_selector

  ⚠️ TODOS/FIXMEs detectados: 8

━━━━━━━━ MEMORIA DEL PROYECTO ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🔒 Disponible en Pro

━━━━━━━━ IMPACTO DE CAMBIOS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🔒 Disponible en Pro

iContext: solo diagnóstico. No modifica proyectos.

## 📦 ¿Dónde encuentro iContext?

El repositorio oficial está en GitHub:

👉 **https://github.com/dulcevenganza666777-lang/icontext**

---

## 🎬 Cómo se usa (paso a paso)

**1. Clonar el repositorio**

```bash
git clone https://github.com/dulcevenganza666777-lang/icontext
cd icontext
