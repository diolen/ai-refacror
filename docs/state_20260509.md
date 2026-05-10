```md
# AI Refactor System — Current State & Roadmap

## 📅 Status Overview (2026-05-09)

Проект представляет собой evolving architecture intelligence system для анализа legacy CakePHP 2 кодовой базы с целью оценки refactor risk и построения структурного понимания системы.

---

# ✅ WHAT HAS BEEN DONE (CURRENT IMPLEMENTATION)

## 🧠 1. Static Analysis Layer
- Dependency scanner for controllers
- Method extraction from legacy CakePHP 2 code
- Framework/helper filtering
- Frequency-aware dependency tracking
- Graph builder (domain vs framework separation)

---

## 🧩 2. Association Analysis Layer
- CakePHP ORM parser:
  - `belongsTo`
  - `hasMany`
  - `hasOne`
  - `hasAndBelongsToMany`
- Normalization of model relationships
- Entity association integration into graph

---

## 📊 3. Entity Model Core
Unified representation of architecture:

- Methods
- Dependencies
- Associations
- Domain entity normalization
- Entity filtering (framework vs domain)
- Identity resolution

---

## ⚙️ 4. Impact Engine
Architectural risk scoring system:

- Impact score calculation
- Connectivity scoring
- Business logic heuristics
- Aggregation root detection
- Refactor risk estimation

---

## 🧠 5. Entity Enrichment Layer
Adds behavioral intelligence:

- Timeline reconstruction
- Method frequency tracking
- Pattern detection:
  - repeated calls
  - hot methods
- Milestone detection:
  - stable usage
  - active dependency usage
- Decision log generation
- Insight extraction

---

## 💾 6. Memory System Integration
Persistent architectural knowledge:

- Milestones stored
- Decisions tracked
- Insights saved
- Historical pattern accumulation

---

## 🧾 7. Prompt Builder System
Structured LLM prompt generation:

- ImpactPrompt
- EntityPrompt
- RefactorPrompt
- PromptContext
- Render pipeline (JSON → CLI output)

---

## 🖥 8. CLI Interface
Unified command system:

- `scan`
- `impact`
- `merge`
- `prompt`
- `memory`

Supports adapter routing (CakePHP 2 implemented)

---

## 🧱 9. Adapter Architecture
Framework isolation layer:

- CakePHP 2 adapter implemented
- Separation of:
  - parsing
  - graph building
  - core engine
- Core system is framework-agnostic

---

# 🚀 CURRENT OUTPUT CAPABILITIES

System now generates:

- Impact score
- Connectivity score
- Methods list
- Associations graph
- Timeline of usage
- Pattern detection
- Milestones
- Decision log
- Architectural insights
- Structured LLM prompt

---

# 🔜 NEXT STEP ROADMAP (IMPORTANT)

## 🧠 1. Prompt Schema Validation Layer (CRITICAL NEXT STEP)

### Problem
Renderer is loosely coupled to evolving schema.

### Solution
Introduce strict contract:

- Required fields schema
- Missing field detection
- Auto validation before rendering

---

## 📊 2. Prompt Compiler v2

Replace ad-hoc prompt building with structured pipeline:

### Pipeline:
```

EntityModel
→ Semantic Graph
→ Impact Graph
→ Reasoning Graph
→ Prompt Plan
→ Rendered Prompt

```

---

## 🧾 3. Explainability Layer ("WHY ENGINE")

Add reasoning trace system:

### Output:
- Why entity is high risk
- Which dependencies contributed
- Which methods increased score
- Connectivity breakdown explanation
- Risk propagation path

---

## 🔁 4. Diff Mode (Evolution Tracking)

Track changes between runs:

- New dependencies
- Removed methods
- Risk delta
- Connectivity delta
- Pattern evolution

---

## 🧠 5. Narrative Layer

Convert raw metrics into story:

Example:
> "User evolved from medium coupling to aggregation root candidate due to increasing cross-model interaction with Center and UsersOperationUnit"

---

## ⚡ 6. Refactor Recommendation Engine (NEXT MAJOR FEATURE)

Automated suggestions:

- Service extraction hints
- God controller detection
- Coupling reduction strategy
- Dead dependency detection
- Safe refactor paths

---

## 🧬 7. Multi-Project Intelligence (FUTURE)

Cross-project learning system:

- reusable patterns
- anti-pattern memory
- framework heuristics
- domain archetypes

---

# 🧭 LONG-TERM VISION

System evolves from:

### CURRENT:
Static + heuristic analyzer

### TO:
**Architectural Intelligence Engine**

That can:

- understand legacy systems
- explain architecture
- estimate risk
- suggest safe evolution paths
- learn from history

---

# 🧩 KEY ARCHITECTURAL SHIFT

From:

> "analysis tool"

To:

> "reasoning system for codebase evolution"
```
