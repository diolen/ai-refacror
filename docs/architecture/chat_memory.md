# AI Refactor System — Current State & Roadmap

## 📅 Status Overview (2026-05-09)

Проект представляет собой evolving architecture intelligence system для анализа legacy CakePHP 2 кодовой базы с целью оценки refactor risk, архитектурного reasoning и безопасной AI-assisted эволюции legacy-систем.

---

# 🧭 SYSTEM VISION

## Mission

Создать framework-agnostic систему архитектурного анализа и AI-assisted refactoring для legacy-проектов.

Система должна:

* анализировать структуру legacy-кода;
* понимать связи между сущностями;
* оценивать refactor risk;
* хранить архитектурную память проекта;
* помогать безопасно эволюционировать legacy-системы.

---

## Architectural Direction

Система эволюционирует из:

```text
simple static analyzer
```

в:

```text
architectural intelligence platform
```

---

## Long-Term Goal

Построить систему, способную:

* понимать legacy architecture;
* объяснять архитектуру;
* оценивать propagation risk;
* сохранять architectural memory;
* генерировать explainable refactor guidance;
* поддерживать безопасную AI-assisted evolution больших legacy-систем.

---

## Key Architectural Shift

От:

```text
analysis tool
```

к:

```text
reasoning system for codebase evolution
```

---

# 🧱 CURRENT ARCHITECTURE

```text
ai-refactor/
├── .gitignore
├── README.md
├── requirements.txt
├── cli.py
├── config.py
├── memory.db
├── venv/
│
├── analysis/
│   ├── adapters/
│   │   └── cakephp2/
│   │       ├── association_parser.py
│   │       ├── dependency_scan.py
│   │       ├── graph_builder.py
│   │       └── runner.py
│   │
│   └── core/
│       ├── dependency_propagation.py
│       ├── dependency_propagation_engine.py
│       ├── entity_filter.py
│       ├── entity_model.py
│       ├── entity_normalizer.py
│       ├── entity_enricher.py
│       ├── graph_engine.py
│       ├── history_store.py
│       ├── impact_engine.py
│       │
│       └── prompt_builder/
│           ├── base_contract.py
│           ├── entity_prompt.py
│           ├── impact_prompt.py
│           ├── prompt_context.py
│           ├── prompt_renderer.py
│           └── refactor_prompt.py
│
├── core/
│   ├── llm.py
│   ├── parser.py
│   └── patcher.py
│
├── docs/
│   ├── architecture/
│   │   ├── contracts.md
│   │   ├── state_20260509.md
│   │   └── ...
│   └── contracts.md
│
├── memory/
│   ├── cleanup.py
│   ├── db.py
│   ├── init_db.py
│   ├── migrate.py
│   └── view.py
│
└── prompts/
    └── refactor.txt
```

---

# 🧠 CORE ARCHITECTURAL CONCEPTS

---

## Layered Connectivity Model

Impact analysis комбинирует:

* dependency connectivity
* association connectivity
* behavioral connectivity

Это создаёт более реалистичную модель архитектурного риска, чем обычный static dependency counting.

---

## Behavioral Graph Analysis

Система различает:

```text
domain interactions
```

и:

```text
framework interactions
```

что позволяет reasoning engine фокусироваться на business-critical entities.

---

## Adapter Architecture

Framework-specific parsing полностью изолирован от core intelligence engine.

### Current Adapter Support

* CakePHP 2

### Planned

* Laravel
* Symfony
* Custom PHP adapters

---

## Unified Entity Model

Entity Model является центральной абстракцией системы.

Он объединяет:

* methods
* dependencies
* associations
* behavioral signals
* normalized entities
* framework filtering
* identity resolution

---

## Prompt Builder Architecture

Prompt generation строится не как text template system, а как architectural reasoning pipeline.

Prompt builder использует:

* entity model
* impact analysis
* architectural context
* behavioral graph
* memory system

Цель:

из:

```text
code completion
```

в:

```text
architecture-aware reasoning
```

---

## Memory as Externalized Cognition

Ключевая архитектурная идея:

```text
memory = file + CLI
```

а НЕ:

```text
memory = chat history
```

Система строит:

```text
externalized cognitive system
```

где:

* CLI = brain
* state.md = memory
* chat = reasoning interface
* LLM = stateless transformer

---

# ✅ CURRENT IMPLEMENTATION STATUS

---

# 🧠 1. Static Analysis Layer

Реализовано:

* Dependency scanner for controllers
* Method extraction from legacy CakePHP 2 code
* Framework/helper filtering
* Frequency-aware dependency tracking
* Graph builder (domain vs framework separation)

---

# 🧩 2. Association Analysis Layer

Реализовано:

* CakePHP ORM parser:

  * `belongsTo`
  * `hasMany`
  * `hasOne`
  * `hasAndBelongsToMany`
* Normalization of model relationships
* Entity association integration into graph

---

# 📊 3. Entity Model Core

Unified representation of architecture:

* Methods
* Dependencies
* Associations
* Domain entity normalization
* Entity filtering (framework vs domain)
* Identity resolution

---

# ⚙️ 4. Impact Engine

Architectural risk scoring system:

* Impact score calculation
* Connectivity scoring
* Business logic heuristics
* Aggregation root detection
* Refactor risk estimation

---

# 🧠 5. Entity Enrichment Layer

Behavioral intelligence layer:

* Timeline reconstruction
* Method frequency tracking
* Pattern detection:

  * repeated calls
  * hot methods
* Milestone detection:

  * stable usage
  * active dependency usage
* Decision log generation
* Insight extraction

---

# 💾 6. Memory System Integration

Persistent architectural knowledge:

* Milestones stored
* Decisions tracked
* Insights saved
* Historical pattern accumulation

---

# 🧾 7. Prompt Builder System

Structured LLM prompt generation:

* ImpactPrompt
* EntityPrompt
* RefactorPrompt
* PromptContext
* Render pipeline (JSON → CLI output)

---

# 🖥 8. CLI Interface

Unified command system:

* `scan`
* `impact`
* `merge`
* `prompt`
* `memory`

Поддерживается adapter routing.

---

# 🧱 9. Adapter Isolation Layer

Framework abstraction layer:

* CakePHP 2 adapter implemented
* Separation of:

  * parsing
  * graph building
  * core engine
* Core system remains framework-agnostic

---

# 🚀 CURRENT OUTPUT CAPABILITIES

Система сейчас генерирует:

* Impact score
* Connectivity score
* Methods list
* Associations graph
* Timeline of usage
* Pattern detection
* Milestones
* Decision log
* Architectural insights
* Structured LLM prompts

---

# 🔁 VERIFIED DATA FLOW

Текущий pipeline:

```text
scan
→ entity_model
→ impact
→ prompt
→ snapshot
→ memory log
```

---

# 🧪 VERIFIED SYSTEM BEHAVIOR

Проверено в CLI:

* scan produces frequency-based dependency graph
* impact engine correctly computes score + connectivity
* entity_model correctly builds associations for key entities (e.g. User, Sic)
* prompt system successfully injects impact context (score, timeline, insights)
* snapshot system stores enriched entity_model per run
* memory system stores milestones, decisions, insights as persistent logs

---

# 🧠 ARCHITECTURE STATE CONFIRMATION

Система уже является working multi-layer architecture:

* Static Analysis Layer ✔
* Entity Model Layer ✔
* Impact Reasoning Layer ✔
* Prompt Generation Layer ✔
* Snapshot Persistence Layer ✔
* Memory Event Layer ✔

---

# 📸 SNAPSHOT SYSTEM STATUS

Текущее состояние snapshot layer:

* snapshot creation: working
* snapshot retrieval: working
* snapshot listing: working
* snapshot versioning: implicit (same name multiple records exist)
* snapshot structure: enriched entity_model dump
* snapshot persistence: SQLite-based
* snapshot diffing: not implemented

---

# 🧠 MEMORY SYSTEM STATUS

Текущее состояние memory layer:

* milestones: working
* decisions: working
* insights: working
* pattern tracking: working (frequency-based)
* search: working
* last-events retrieval: working
* timeline: aggregated view (not event stream based)

---

# ⚠️ KNOWN LIMITATIONS

Текущие ограничения системы:

* snapshot versioning is not semantic
* no diff engine
* dependency data partially lost during entity_model transformation
* memory layer not connected back into analysis pipeline
* timeline is aggregated, not event-stream based
* entity prompt target can be lost in some modes ("TARGET: unknown")
* entity ordering is not fully deterministic across runs

---

# 🧠 MEMORY PROTOCOL v1 (MVP)

---

## 🎯 Goal

Синхронизировать:

* CLI (source of truth)
* Chat (reasoning layer)
* state.md (memory snapshot)
* LLM (stateless processor)

без потери контекста.

---

## 🧱 Core Principle

В системе существует только один источник истины:

```text
CLI state
```

Chat НЕ хранит память.

Chat:

* читает snapshot;
* предлагает reasoning;
* генерирует patch;
* интерпретирует entity_model.

---

## 📦 Memory Unit

Вся память разбивается на Memory Units:

```json
{
  "id": "uuid",
  "type": "milestone | decision | insight | pattern | state",
  "entity": "User",
  "timestamp": "...",
  "source": "cli | llm | system",
  "data": {}
}
```

---

## 📄 STATE SNAPSHOT

`state.md` — canonical architectural projection.

Не лог.

А:

```text
runtime truth layer
```

---

## Example Snapshot Structure

```markdown
# STATE SNAPSHOT

## VERSION
2026-05-09T21:00:00

## ENTITIES
- User
- Center
- UsersCenters
- UsersOperationUnit

## IMPACT SNAPSHOT
User:
  score: 26
  connectivity: 15

## DECISIONS
- normalized self references enabled
- framework entities excluded from graph

## MILESTONES
- User reached stable usage
- dependency scanner stabilized

## PATTERNS
- repeated method calls detected

## ACTIVE CONTEXT
- last_command: prompt impact User
```

---

# 🔁 SYNC PROTOCOL

---

## 🖥 CLI → CHAT

После каждого CLI run:

```bash
memory snapshot --write state.md
```

или автоматически:

* append diff to state.md
* update entity_model summary

---

## 💬 CHAT → CLI

Chat НЕ применяет изменения напрямую.

Chat возвращает:

```diff
MEMORY UPDATE:
- add decision: ...
- update insight: ...
- new milestone: ...
```

CLI применяет patch:

```bash
cli.py memory apply patch.diff
```

---

## 🧠 CHAT RULE

Chat никогда не говорит:

```text
I remembered
```

Chat говорит:

```text
here is a memory patch for CLI
```

---

# 🔄 SYNC CYCLE

```text
1. CLI scan/graph/impact
2. CLI updates state.md
3. Chat reads state.md
4. Chat produces reasoning / patch
5. CLI applies patch
6. CLI regenerates state.md
```

---

# 🧩 MEMORY TYPES

---

## 🟢 Decision

Архитектурные решения.

Пример:

```json
"decision": "entity_model unified abstraction"
```

---

## 🟡 Insight

Наблюдения системы.

Пример:

```json
"insight": "User is high coupling node"
```

---

## 🔵 Pattern

Повторяющиеся сигналы.

Пример:

```json
"pattern": "repeated dependency usage"
```

---

## 🔴 Milestone

Фиксация прогресса.

Пример:

```json
"milestone": "impact engine stabilized"
```

---

## ⚫ State

Snapshot состояния системы.

---

# 🧠 CONTEXT WINDOW RULE

LLM никогда не получает всю память.

Он получает только:

```text
state.md (latest)
+
entity_model (current)
+
impact result (current entity)
```

---

# ⚙️ CLI COMMANDS (v1)

---

## 📸 Snapshot

```bash
cli.py memory snapshot
```

---

## 🔁 Apply Patch

```bash
cli.py memory apply patch.diff
```

---

## 📊 Show State

```bash
cli.py memory show
```

---

## 🔍 Entity History

```bash
cli.py memory entity User
```

---

# 🧠 CHAT ROLE

Chat выполняет только 3 функции:

### 1. Reasoning Engine

Объясняет:

* impact
* graph
* entity_model

---

### 2. Planner

Предлагает следующий шаг.

---

### 3. Patch Generator

Генерирует memory diff.

---

# 🚫 SYSTEM CONSTRAINTS

Chat НЕ:

* хранит долгую память;
* пересчитывает graph;
* дублирует CLI;
* является source of truth.

---

# 🔥 CURRENT DEVELOPMENT STAGE

Система сейчас переходит из:

```text
static analysis engine
```

в:

```text
behavior-aware architectural intelligence system
```

---

## Main Active Areas

* propagation-aware impact analysis
* graph density modeling
* explainable architectural reasoning
* AI-assisted safe refactoring

---

# 🔜 NEXT STEP ROADMAP

---

# 🧠 1. Prompt Schema Validation Layer

## Problem

Renderer loosely coupled to evolving schema.

## Solution

Ввести strict contract system:

* required fields schema
* missing field detection
* auto validation before rendering

---

# 📊 2. Prompt Compiler v2

Заменить ad-hoc prompt building на structured cognition pipeline.

## Planned Pipeline

```text
EntityModel
→ Semantic Graph
→ Impact Graph
→ Reasoning Graph
→ Prompt Plan
→ Rendered Prompt
```

---

# 🧾 3. Explainability Layer ("WHY ENGINE")

Добавить reasoning trace system.

## Planned Output

* why entity is high risk
* which dependencies contributed
* which methods increased score
* connectivity breakdown explanation
* risk propagation path

---

# 🔁 4. Diff Mode (Evolution Tracking)

Track architectural evolution between runs:

* new dependencies
* removed methods
* risk delta
* connectivity delta
* pattern evolution

---

# 🧠 5. Narrative Layer

Преобразование raw metrics в architectural story.

Пример:

> "User evolved from medium coupling to aggregation root candidate due to increasing cross-model interaction with Center and UsersOperationUnit"

---

# ⚡ 6. Refactor Recommendation Engine

Planned capabilities:

* service extraction hints
* god controller detection
* coupling reduction strategy
* dead dependency detection
* safe refactor paths

---

# 🧬 7. Multi-Project Intelligence

Future direction:

* reusable patterns
* anti-pattern memory
* framework heuristics
* domain archetypes

---

# 🚀 FUTURE ARCHITECTURAL DIRECTIONS

---

## Reasoning Graph

Следующий этап:

```text
WHY this entity is dangerous
```

Пример:

```text
User
 ├── high dependency fanout
 ├── aggregation root candidate
 ├── repeated transactional coordination
 └── controller-service coupling hotspot
```

---

## Architectural Event Stream

Переход от passive memory к event-based architecture:

```text
entity_changed
impact_increased
coupling_spike_detected
new_hotspot_detected
```

---

## Executable state.md

Следующий major milestone:

```text
state.md
```

как:

* machine-readable
* diffable
* reproducible
* deterministic
* executable architectural context

---

## Architectural Regression Detection

Будущие возможности:

* connectivity delta analysis
* cyclic dependency cluster detection
* impact instability detection
* aggregation root expansion detection

---

# 🧩 FINAL SYSTEM DEFINITION

Система эволюционирует из:

```text
Code Analysis Tool
```

в:

```text
State-aware Architectural Reasoning Platform
```

с externalized cognition architecture и explainable AI-assisted legacy evolution.
