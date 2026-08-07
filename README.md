![iContext Logo](Screenshot_20260806-191158.png)

<p align="center">
  <img src="Screenshot_20260806-191158.png" alt="iContext Logo" width="100%">
</p>

---


<p align="center">
  <img src="docs/assets/icontext-logo.png" alt="iContext Logo" width="200"/>
</p>

<h1 align="center">iContext</h1>

<p align="center">
  <strong>Give AI the map, not the whole forest.</strong>
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#usage">Usage</a> ·
  <a href="#examples">Examples</a> ·
  <a href="#contribute">Contribute</a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub stars](https://img.shields.io/github/stars/dulcevenganza666777-lang/iContext)](https://github.com/dulcevenganza666777-lang/iContext/stargazers)
```text
# 🧭 iContext

**Give AI the context it needs from your codebase — without dumping hundreds of files into the chat.**

iContext is a lightweight, local-first project diagnostic tool that analyzes a codebase and produces a compact context report you can give to an AI coding assistant. Instead of manually explaining a large repository to an AI, run one command and get a structured overview of what is happening inside the project.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](https://github.com/dulcevenganza666777-lang/icontext-)

---

## Why iContext?

When an AI assistant needs to work on an existing project, the first problem is often not the code itself. It is **context**.

A repository may contain:
- Hundreds or thousands of files
- Multiple modules
- Old and new implementations
- TODOs and FIXMEs
- Uncommitted changes
- Several entry points
- Active development in only a few areas

You could paste files into the AI one by one. Or you can start with a project diagnostic.

**iContext gives the AI a map before you give it the files.**

---

# 🚀 Quick Start

Clone the repository:
```bash
git clone https://github.com/dulcevenganza666777-lang/icontext-.git
```

Enter the directory:

```bash
cd icontext-
```

Make the executable runnable:

```bash
chmod +x icontext
```

Now run it:

```bash
./icontext
```

That's it.

No API key is required.
No cloud account is required.
No AI API is required.

---

🖥️ Run iContext on your own project

After installing iContext, copy or use the executable inside the project you want to inspect.

Example:

```bash
cd ~/my-project
/path/to/icontext
```

Or, if icontext is already in the project:

```bash
cd ~/my-project
./icontext
```

iContext analyzes the project from the terminal and produces a diagnostic report.

---

📊 Example output

For example, running iContext on a large Python project can produce output like:

```
╔══════════════════════════════════════════════════════════════╗
║                         🧭 iContext                          ║
╚══════════════════════════════════════════════════════════════╝

📁 PROJECT: Cronos-V3
📄 FILES: 389
🔤 MAIN LANGUAGE: .py

━━━━━━━━ ARCHITECTURE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✓ adapters
  ✓ archive
  ✓ assets
  ✓ biblioteca
  ✓ brain
  ✓ capa_adn
  ✓ capa_biblioteca
  ✓ capa_cine
  ✓ capa_composer
  ✓ capa_director
  ✓ capa_idea
  ✓ capa_interprete
  ✓ capa_operadores
  ✓ capa_parametros

🚀 ENTRY POINTS:
  → run_verified.py
  → run.py
  → run_quick.py

📚 Documentation: ✅ Yes
🧪 Tests: ✅ Yes

🔀 GIT BRANCH: main
📝 UNCOMMITTED CHANGES: 165

━━━━━━━━ RECENT ACTIVITY ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 LAST MODIFICATION: 2026-08-04 02:38
📊 MODIFIED FILES: 12
📈 ACTIVITY: 6.4 files/day

MOST RECENT FILES:
  08-04 02:38 icontext
  08-04 02:17 registry.py
  08-04 02:17 run_verified.py
  08-04 02:16 RESUMEN_EJECUTIVO.md
  08-04 02:15 explorer_real.py

━━━━━━━━ ACTIVE THREAD ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACTIVE AREAS:
  → motores
  → núcleo / core
  → registro

MAIN EVIDENCE:
  ✓ registry.py
  ✓ run_verified.py
  ✓ explorer_real.py
  ✓ brain_state.pkl

━━━━━━━━ PROBLEMS / PENDING WORK ━━━━━━━━━━━━━━━━━━━━━━━━━━━
🟠 PENDING INTEGRATIONS:
  → Integrate Groq for idea generation
  → Connect real YouTube Analytics

🟡 EXPLICIT TODOs:
  → Implement persistent memory
  → Add more rendering engines

━━━━━━━━ PROJECT DIRECTION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OBJECTIVE:
  → Complete and verify pending integrations.

━━━━━━━━ NEXT ACTION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  → Review the first pending integration.

iContext: diagnostic only. Does not modify projects.
```

The important part is not the formatting. The important part is that the output gives you a compact map of the repository.

---

🤖 Give the result to an AI

After running:

```bash
./icontext
```

copy the output and give it to your AI assistant.

For example:

Here is the current diagnostic context of my project.
[PASTE iContext OUTPUT HERE]
Based on this context:

1. Identify the most important pending integration.
2. Tell me which files I should inspect first.
3. Do not invent missing architecture.
4. Ask for specific files only when necessary.

The AI now has a high-level understanding of the repository before you start sending source files.

This can reduce unnecessary context and token usage, depending on the project and the AI workflow.

---

🧠 Why this can save tokens

Imagine a project with hundreds of files.

Without a diagnostic layer, you may end up explaining: project structure + modules + entry points + recent changes + TODOs + Git state + active development + relevant files before the AI can even begin working.

iContext summarizes those signals first.

Instead of immediately dumping a large repository into the conversation:

```text
Large project
     ↓
     ↓
Compact diagnostic
     ↓
AI understands the project map
     ↓
Only relevant files need to be discussed
```

The actual token savings depend on the repository, model, and workflow.

---

🔍 What does iContext detect?

iContext can identify useful project signals such as:

Architecture
Major directories and project organization.

Language
The primary programming language detected from the project.

Stack
Technology and project configuration signals.

Entry points
Files that appear to be important execution points.

Git state
Current branch and uncommitted changes.

Recent activity
Recently modified files and development activity.

TODOs and FIXMEs
Explicit unfinished work found in the source tree.

Active development
Groups of files that appear to be related to current work.

Evidence
Files and code markers supporting the detected project activity.

Next action
A suggested place to begin investigating.

---

⚙️ Command examples

Basic diagnostic:

```bash
./icontext
```

Compact output:

```bash
./icontext --compact
```

AI-oriented diagnostic:

```bash
./icontext --ai
```

Fix/diagnostic mode:

```bash
./icontext --fix
```

The available options depend on the version of iContext you are running.

---

🔒 Local-first

iContext is designed to inspect projects locally. It does not require sending your source code to an AI API to generate the basic diagnostic. Your code stays on your machine during normal operation.

This makes it useful for:

· Local development
· Termux
· Linux
· Offline workflows
· Private repositories
· Large codebases

---

🌎 Language and project support

iContext is designed around project structure rather than a single framework. It can work with repositories containing technologies such as:

· Python
· JavaScript
· TypeScript
· Java
· C
· C++
· Go
· Rust
· PHP
· Ruby
· Other file-based project structures

---

📱 Termux

iContext can be used directly from Termux.

Example:

```bash
cd ~/Cronos-V3
cp ~/icontext-free/icontext .
chmod +x icontext
./icontext
```

You can then copy the diagnostic output directly into an AI assistant.

This makes iContext practical even when working entirely from an Android phone.

---

🧪 Real-world workflow

A typical workflow looks like this:

1. Open a project
2. Run iContext
3. Inspect the diagnostic
4. Copy the output
5. Give it to your AI
6. AI identifies relevant areas
7. Inspect only the files that matter

The objective is not to replace your code editor. The objective is to reduce the time spent explaining the project before actually working on it.

---

🧭 iContext vs tree

tree answers: What files and folders exist?

iContext tries to answer:

· What is happening in this project?
· What changed?
· Where is development active?
· What problems are visible?
· What should I inspect next?

That distinction is the core idea behind iContext.

---

🛣️ Roadmap

Potential future improvements include:

· Deeper dependency analysis
· Change impact analysis
· Project history
· Persistent project memory
· More advanced recommendations
· HTML reports
· PDF reports
· CI/CD integrations
· AI agent integrations
· Multi-project analysis

The Community version focuses on the core diagnostic experience.

---

🤝 Contributing

Issues, suggestions, testing and pull requests are welcome.

If you find iContext useful, consider:

· ⭐ Starring the repository
· 🍴 Forking it
· 🐛 Reporting problems
· 💡 Suggesting improvements
· 🔧 Contributing code

---

📜 License

MIT License.

See LICENSE for details.

---

🧭 iContext
Understand your codebase before asking AI to change it.

GitHub:
https://github.com/dulcevenganza666777-lang/icontext-

```