# 🧭 iContext

**Give AI the context it needs from your codebase — without dumping hundreds of files into the chat.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](https://github.com/dulcevenganza666777-lang/icontext)

---

## The problem

When working with AI coding assistants, one of the hardest parts is giving the model enough context.

You can paste dozens of files manually, explain the architecture, or waste tokens explaining things the model could infer.

There is a simpler approach: **iContext scans locally and creates a compact diagnostic context for your AI.**

---

## What iContext tells you

- Project architecture
- Main language and tech stack
- Entry points
- Recent file activity and Git state
- TODOs and FIXMEs
- Active areas of development
- Suggested next action

**It is not just `tree`.** It's a diagnostic to help you understand where the project is and what to examine next.

---

## Why use it with AI?

Instead of telling your AI *"Here are 200 files, understand my project"*, give it a compact iContext report first.

```text
Your project
     ↓
  iContext
     ↓
Compact context
     ↓
ChatGPT / Claude / Gemini / DeepSeek
     ↓
AI understands the project faster
