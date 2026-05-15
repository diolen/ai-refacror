# 🧠 LLM КОНТЕКСТ

## 📌 ПРОЕКТ

AI-assisted architectural reasoning system for legacy CakePHP 2 projects.

Purpose:
analyze legacy architecture, estimate refactor risk, and support safe AI-assisted system evolution.

---

# 📊 ТЕКУЩИЙ СТАТУС

System status:
PRODUCTION-STABLE (analysis engine active)

Validated pipeline stages:

* scan
* impact
* prompt
* snapshot
* merge

All current validation stages passing.

(memory system removed)

---

# 🏗️ ОСНОВНАЯ АРХИТЕКТУРА

Pipeline:

```text
scan
→ entity_model
→ impact
→ prompt
→ snapshot
````

Architecture layers:

* static analysis layer
* entity model layer
* impact reasoning layer
* prompt generation layer
* snapshot layer

Framework adapters are isolated from core engine.

Current supported framework:

* CakePHP 2

---

# 🧠 КЛЮЧЕВЫЕ КОНЦЕПЦИИ

## entity_model

Canonical architectural data contract (serialized IR).

Contains:

* methods
* dependencies
* associations
* behavioral signals
* insights
* patterns
* timeline

Acts as deterministic intermediate representation between parsing and reasoning.

---

## impact engine

Propagation-aware architectural risk scoring system.

Combines:

* dependency connectivity
* association connectivity
* behavioral signals

Produces:

* score
* connectivity
* insights

---

## prompt builder

Structured reasoning-oriented prompt generation system.

Uses:

* entity_model
* impact analysis
* prompt_context
* architectural metadata

---

## prompt contracts

Typed prompt generators defining structured LLM inputs:

* EntityPrompt
* ImpactPrompt
* RefactorPrompt

All prompts must be deterministic and serializable.

---

## snapshots

Persistent architectural state dumps.

Used for:

* state recovery
* reasoning continuity
* architecture inspection

---

# ⚙️ ТЕКУЩИЕ ВОЗМОЖНОСТИ

Implemented:

* dependency scanning
* CakePHP association parsing
* graph building
* impact scoring
* behavioral enrichment
* hotspot detection
* prompt generation
* snapshot persistence
* CLI routing

---

# ⚠️ ТЕКУЩИЕ ОГРАНИЧЕНИЯ

Known limitations:

* dependency transformation partially lossy
* no reasoning graph
* no semantic diff engine
* no explainability engine
* entity ordering not fully deterministic

---

# 🚀 ТЕКУЩИЙ ФОКУС РАЗРАБОТКИ

Current focus:
simplifying architectural context into portable LLM bootstrap format.

Decision:
replace complex memory/event system with curated llm_context.md.

Reason:
LLM needs compressed semantic state, not raw telemetry history.

---

# 🎯 АКТИВНЫЕ ЦЕЛИ

Near-term goals:

1. Stable llm_context.md workflow
2. Deterministic context structure
3. Lossless entity_model transformation
4. Explainability layer
5. Reasoning graph

---

# 📚 ВАЖНАЯ ТЕРМИНОЛОГИЯ

entity_model:
normalized architectural IR (deterministic contract)

impact:
propagation-aware architectural risk score

hotspot:
high-coupling or high-risk entity

snapshot:
persistent architecture state dump

adapter:
framework-specific parsing layer

prompt_context:
intermediate structured state between impact and prompt generation

---

# 🧱 ПРИНЦИПЫ СИСТЕМЫ

* CLI is source of truth
* chat is reasoning interface
* LLM is stateless
* architecture state must remain portable
* prompts must be deterministic
* framework parsing must stay isolated from reasoning core

---

# 🛡️ БЕЗОПАСНАЯ ЗОНА ЭВОЛЮЦИИ

Safe areas for continued development:

* explainability
* reasoning graph
* propagation modeling
* prompt quality
* deterministic serialization

Avoid large architectural rewrites unless required.

---

# ⚙️ КОНТРАКТ ВЫПОЛНЕНИЯ (RUNTIME CONTRACT)

This section defines how the system behaves during execution.

## INPUT STATE

All execution starts from:

* CLI command
* file path (controller/model)
* adapter (CakePHP2)

No persistent state is used.

---

## EXECUTION FLOW

All commands must follow deterministic pipeline:

1. scan → produces dependency graph
2. entity_model → normalized IR
3. impact → risk scoring + connectivity
4. prompt → structured LLM input

---

## STATE RULE

The system is stateless.

Allowed runtime state:

* in-memory entity_model
* in-memory impact result
* in-memory prompt_context

Disallowed:

* persistent memory
* hidden caches
* implicit historical state

---

## SOURCE OF TRUTH

* CLI execution is authoritative
* entity_model is canonical IR
* llm_context.md defines expected system behavior

---

## OUTPUT CONTRACT

All outputs must be:

* deterministic
* serializable
* free of hidden state

---

# 🧱 СХЕМА ENTITY MODEL

Canonical structure:

```json
{
  "methods": [],
  "dependencies": [],
  "associations": {},
  "milestones": [],
  "decisions": [],
  "patterns": [],
  "insights": [],
  "timeline": []
}
```

---

## RULES

* must be deterministic
* no duplicates
* all names normalized
* associations must be directional grouped

---

# 🔄 МОДЕЛЬ СОСТОЯНИЙ PIPELINE

Each entity passes through states:

* RAW (scan output)
* NORMALIZED (entity_model)
* ANALYZED (impact applied)
* ENRICHED (insights + patterns)
* PROMPTED (LLM-ready output)

---

## RULE

Each stage must be:

* pure function
* deterministic
* stateless

---

# 🛑 ПОСЛЕДНЕЕ СТАБИЛЬНОЕ СОСТОЯНИЕ

Validation summary:

* all major pipeline stages passing
* merge contract fixed
* self-loop dependency bug fixed
* snapshot serialization stable
* CLI contracts stable

Date:
2026-05-15

---

# VERSION

llm_context_version: 2.1-runtime-contract-stable

```

---

# 🧭 Что дальше (логично по системе)

Теперь у тебя есть стабильный фундамент. Следующий шаг **не усложнение**, а усиление:

## 👉 1. Explainability Layer (рекомендую дальше)
- почему entity “high risk”
- какие зависимости влияют на score
- разложение impact_score

## 👉 2. Context Compiler (позже)
- auto-build llm_context.md из entity_model + runtime run

---

Если хочешь, дальше можем сделать:
👉 :contentReference[oaicite:0]{index=0} (очень полезно для рефакторинга)
