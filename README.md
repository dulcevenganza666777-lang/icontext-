# 🧭 iContext

**Give AI the context it needs from your codebase — without dumping hundreds of files into the chat.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](https://github.com/dulcevenganza666777-lang/texto-de-icono-.git)

---

## The problem

When working with AI coding assistants, one of the hardest parts is giving the model enough context about an existing project.

You can:

- Paste dozens of files manually
- Explain the architecture yourself
- Upload huge amounts of source code
- Waste tokens explaining things the model could infer

There is a simpler approach.

**iContext scans the project locally and creates a compact diagnostic context you can give to an AI model.**

---

## What iContext tells you

Instead of showing you a massive file tree, iContext extracts useful signals from the project:

- Project architecture
- Main programming language
- Technology stack
- Entry points
- Recent file activity
- Git branch and uncommitted changes
- TODOs and FIXMEs
- Active areas of development
- Evidence of ongoing work
- Suggested next action

**It is not just `tree` or `ls`.**

It is a project diagnostic designed to help you quickly understand **where the project is and what should be examined next.**

---

## Why use it with AI?

Imagine opening a project with hundreds of files.

Instead of telling your AI:

> "Here are 200 files. Please understand my project."

You can give it a compact iContext report first.

The workflow is simple:

```text
Your project
     ↓
  iContext
     ↓
Compact project context
     ↓
ChatGPT / Claude / Gemini / DeepSeek
     ↓
AI understands the project faster
