Отлично, ты по сути сделал **уровень “system spec v1.0”**, и теперь твоя шпаргалка уже должна отражать не только CLI, а именно **архитектурную модель + операционный слой + новые debug-команды**.

Я обновил твою шпаргалку так, чтобы она соответствовала твоему `analysis_system_spec.md`.

---

# 📄 UPDATED CHEAT SHEET (SYNCED WITH SYSTEM SPEC)

````markdown
# AI Refactor System — Operational Cheat Sheet (UPDATED)

## 🧠 SYSTEM PURPOSE

Framework-agnostic architecture intelligence system:

- static analysis
- dependency + association extraction
- entity modeling
- impact/risk scoring
- enrichment + behavioral analysis
- persistent architectural memory

Goal:
→ evolve from code scanner → architecture intelligence engine

---

# 🏗️ SYSTEM LAYERS (ACTUAL IMPLEMENTATION)

## 1. RAW LAYER (EXTRACTION)

### scan
Extracts:
- method calls
- dependencies
- frequency signals

### graph_builder (adapter)
- builds method graph
- separates domain/framework

### association_parser
- CakePHP ORM relations:
  - belongsTo
  - hasMany
  - hasOne
  - HABTM

---

## 2. CORE ENTITY LAYER

### entity_model

Unified structure:

- methods
- dependencies
- associations

Responsibilities:
- normalization
- deduplication
- entity identity resolution
- framework filtering

---

## 3. ENRICHMENT LAYER

### entity_enricher adds:

- timeline (event history)
- milestones (threshold events)
- patterns (repetition detection)
- decisions (normalization + filtering decisions)
- insights (complexity + coupling)
- memory persistence (SQLite)

---

## 4. GRAPH / PROPAGATION LAYER

- dependency propagation
- transitive closure support
- multi-depth relationship expansion

---

## 5. IMPACT ENGINE

Computes:

- impact score
- connectivity score
- risk classification
- architectural insights

---

## 6. MEMORY LAYER

Stored in SQLite:

- milestones
- decisions
- insights
- patterns

---

## 7. ADAPTER LAYER

Currently:

- CakePHP2 adapter

Responsibilities:
- dependency scan
- graph building
- association parsing

Rule:
> Core system must stay framework-agnostic

---

# ⚙️ CLI COMMANDS (CURRENT STATE)

## 🔍 scan (RAW LAYER)

```bash
python cli.py scan <controller_file> --adapter cakephp2
````

Output:

* raw dependencies
* method calls

---

## 📊 impact (MAIN ANALYSIS)

```bash
python cli.py impact <entity> <controller> <model> --adapter cakephp2
```

Output:

* impact score
* connectivity score
* methods
* associations
* timeline
* patterns
* milestones
* decisions
* insights

---

## 🧠 prompt (LLM GENERATION)

```bash
python cli.py prompt <entity> <controller> <model> --mode impact
```

Modes:

* impact → risk analysis prompt
* refactor → refactor suggestion prompt (emerging)

---

## 🔀 merge (FULL PIPELINE)

```bash
python cli.py merge <controller> <model> --adapter cakephp2
```

Output:

* full entity_model
* enriched graph
* LLM prompt

---

## 💾 memory (ARCHITECTURAL HISTORY)

```bash
python cli.py memory --last 20
python cli.py memory --timeline
python cli.py memory --search User
```

---

# 🧪 DEBUG / TEST COMMANDS (NEW — IMPORTANT)

## 🔬 Full prompt debug

```bash
python cli.py prompt User \
controller.php model.php \
--mode impact
```

---

## 🔬 Raw scan validation

```bash
python cli.py scan controller.php
```

---

## 🔬 Impact verification

```bash
python cli.py impact User controller.php model.php
```

---

## 🔬 Memory timeline inspection

```bash
python cli.py memory --timeline
```

---

## 🔬 Memory search

```bash
python cli.py memory --search User
```

---

## 🔬 Merge full graph validation

```bash
python cli.py merge controller.php model.php
```

---

# 🧠 KEY SYSTEM BEHAVIOR RULES

## RAW vs ENRICHED

### RAW:

* scan
* graph_builder
* association_parser

### ENRICHED:

* entity_model
* impact_engine
* enricher outputs

Rule:

> RAW must never depend on enriched layer

---

## ENTITY MODEL CONTRACT

Each entity contains:

* methods[]
* dependencies[]
* associations{}
* timeline[]
* patterns[]
* milestones[]
* decisions[]
* insights[]

---

## MEMORY CONTRACT

Memory stores:

* behavioral signals
* architectural decisions
* repeated patterns
* evolution history

---

# 🚀 SYSTEM STATE

## Fully working:

✔ dependency scanner
✔ graph builder
✔ association parser
✔ entity model
✔ enrichment system
✔ impact engine
✔ prompt builder
✔ CLI interface
✔ memory system
✔ adapter architecture (CakePHP2)

---

# 🧭 ARCHITECTURAL STATUS

System is now:

> Architecture Intelligence Engine (early v1)

Not a tool anymore.

---

# 🔥 NEXT STEP (FOR YOU TOMORROW)

If you continue:

👉 Prompt Compiler v2

* reasoning graph
* schema validation
* explainability layer
* diff-aware analysis

---

```

---

# 📌 Что изменилось в шпаргалке

Я синхронизировал её с твоим реальным состоянием:

### ✔ добавлено
- реальные CLI команды (scan / impact / prompt / merge / memory)
- debug commands как отдельный блок
- RAW vs ENRICHED формализация
- memory contract как слой системы
- entity model структура как “истина системы”

### ✔ усилено
- разделение слоёв (RAW / CORE / ENRICHMENT / IMPACT)
- правила архитектуры (dependency direction)
- системное описание CLI как интерфейса архитектуры

---

# 🧠 Итог

Теперь у тебя есть:

> 📐 operational cheat sheet = “как пользоваться системой”
> 📐 spec.md = “что система собой является”
> 📐 codebase = “как она реализована”

---

Если завтра продолжишь — следующий логический апгрейд будет:

👉 сделать auto-generation этой шпаргалки из CLI состояния (self-documenting system)

Но сейчас ты уже на хорошем уровне стабилизации архитектуры.
```
