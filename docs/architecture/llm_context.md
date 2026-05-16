Вот финальная, чистая версия `llm_context.md`, уже полностью приведённая к твоей текущей цели — **Prompt Compiler для LLM**, без архитектурного “шума” и лишних системных слоёв.

---

# 🧠 LLM КОНТЕКСТ

## 📌 ПРОЕКТ

LLM Prompt Compiler for legacy CakePHP 2/3/4 codebases.

Purpose:
transform codebase + task into an optimized prompt for external LLM execution.

---

# 🎯 ГЛАВНАЯ ЦЕЛЬ СИСТЕМЫ

Система НЕ решает задачи напрямую.

Она компилирует вход в LLM-инструкцию:

```text id="goal"
CODEBASE(adapter:CakePHP2/3/4) + TASK
→ ANALYSIS(optional LLM)
→ OPTIMIZED LLM PROMPT
→ EXTERNAL LLM EXECUTION
```

---

# 🏗️ ОСНОВНОЙ PIPELINE

```text id="pipeline"
scan
→ entity_model
→ impact
→ prompt
```

Output:
→ structured prompt for external LLM

---

# 🧠 КЛЮЧЕВЫЕ МОДУЛИ

## entity_model

Normalized structural representation of codebase.

Contains:

* methods
* dependencies
* associations
* lightweight insights

Purpose:
provide deterministic structural IR for analysis.

---

## impact engine

Computes architectural characteristics:

* complexity score
* dependency connectivity
* coupling level
* architectural hotspots

Purpose:
enrich prompt with risk/complexity signals.

---

## prompt builder

Core system output generator.

Input:

* task (refactor / debug / feature)
* entity_model
* impact analysis

Output:

* optimized structured prompt for external LLM

Purpose:
compress full analysis into LLM-ready instruction set.

---

# ⚙️ ТЕКУЩИЕ ВОЗМОЖНОСТИ

* CakePHP 2 static code analysis
* dependency extraction
* association parsing
* entity normalization
* impact scoring
* prompt generation for LLM execution

---

# ⚠️ ОГРАНИЧЕНИЯ

* no persistent memory
* no runtime state retention
* no snapshot system
* no self-execution
* no long-term graph persistence
* no background knowledge accumulation

---

# 🧱 ПРИНЦИПЫ СИСТЕМЫ

* system is stateless
* CLI is single source of truth
* output is deterministic
* no hidden memory or caching
* each run is independent
* focus is prompt quality, not system evolution

---

# 🎯 ФОКУС СИСТЕМЫ

System is optimized for generating LLM prompts for:

* refactoring legacy code
* debugging issues
* generating new features

All logic exists only to improve prompt quality.

---

# 🧠 ТЕРМИНОЛОГИЯ

## entity_model

Structured representation of code architecture.

## impact

Scoring layer for complexity, coupling, and risk.

## prompt

Final LLM-ready instruction set.

---

# 🧭 EXECUTION MODEL

```text id="exec_model"
INPUT:
- task
- codebase

PROCESS:
scan → entity_model → impact → prompt

OUTPUT:
optimized LLM prompt
```

---

# 🛑 СТАБИЛЬНОЕ СОСТОЯНИЕ

System is stable and validated.

Working modules:

* scan
* impact
* prompt generation

Date:
2026-05-15

---

# VERSION

llm_context_version: 3.0-prompt-compiler-core

---

💬 ЧТО ЭТО ЗНАЧИТ ДЛЯ ТЕБЯ СЕЙЧАС

Самое важное:

👉 ты больше не “улучшаешь анализатор”
👉 ты “улучшаешь генератор промтов”

🧠 И ЭТО УЖЕ ДРУГОЙ КЛАСС СИСТЕМ

Это ближе к:

code intelligence compiler
LLM instruction optimizer
reasoning preprocessor

Если завтра продолжим, логичный следующий шаг будет очень сильный:

👉 Prompt Builder v2: framework-aware prompt shaping
(например: CakePHP2 → “legacy risk bias injection” в промт)

И это уже даст реальное качество LLM-результатов, а не просто структуру.