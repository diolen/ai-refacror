Я собрал тебе версию, которая одновременно работает в двух режимах:

* 📘 как **документация для тебя**
* 🧠 как **контекст для восстановления архитектуры (me-readable spec)**

Без лишнего текста, но с сохранением всей сути системы и разделения слоёв.

---

# 📄 `docs/architecture/analysis_system_spec.md`

```markdown
# AI Static Analysis & Refactoring System

## 🧠 Purpose

Framework-agnostic system for:
- static analysis of legacy PHP (CakePHP 2 initially)
- dependency + association extraction
- behavioral graph construction
- impact/risk analysis for refactoring
- persistent architectural memory

Goal:
→ evolve from "code scanner" → "architectural intelligence system"

---

# 🏗️ SYSTEM ARCHITECTURE OVERVIEW

System is split into 4 conceptual layers:

```

RAW LAYER
↓
CORE ENTITY LAYER
↓
GRAPH + PROPAGATION LAYER
↓
ANALYTICS + MEMORY LAYER

```

---

# 1. RAW LAYER (DATA EXTRACTION)

## Responsibility
Extract raw structural data from codebase.

## Components

### scan
- Extracts `$this->Model->method()` calls
- Produces dependency list
- Tracks frequency of calls

### graph_builder (adapter)
- Builds method call graph
- Separates domain vs framework calls

### association_parser (adapter)
- Parses ORM relationships:
  - belongsTo
  - hasMany
  - hasOne
  - HABTM

---

# 2. CORE ENTITY LAYER

## Responsibility
Normalize raw data into unified representation.

## Key module

### entity_model.py

Builds:

```

Entity {
methods[]
dependencies[]
associations{}
}

```

## Processing steps

1. normalize entity names
2. filter framework entities
3. deduplicate dependencies
4. merge:
   - scan data
   - graph data
   - associations

---

# 3. NORMALIZATION & ENRICHMENT

## entity_normalizer
- cleans naming
- enforces entity identity consistency

## entity_enricher

Adds:

### Timeline
- event frequency tracking
- method call history

### Milestones
- usage thresholds
- dominance detection

### Decisions
- normalization decisions
- filtering decisions

### Insights
- complexity estimation
- coupling estimation

### Patterns
- repeated calls
- structural repetition signals

### Memory persistence
Writes to SQLite:
- milestones
- decisions
- insights

---

# 4. GRAPH + PROPAGATION LAYER

## dependency_propagation_engine

### Responsibility
Expand direct dependencies into transitive closure.

```

A → B → C
becomes:
A → [B, C]

```

### Output
- enriched dependency graph
- multi-depth propagation (max_depth configurable)

---

# 5. IMPACT ANALYSIS LAYER

## impact_engine

### Computes:
- entity risk score
- connectivity score
- complexity classification

### Outputs:

- score
- insights:
  - complexity (low/medium/high)
  - coupling level
- structural interpretation of entity

---

# 6. ADAPTER ARCHITECTURE

## Purpose
Isolate framework-specific logic.

### Current implementation:
- CakePHP2 adapter

## Components:

- dependency_scan
- graph_builder
- association_parser

## Design rule:
> Core system must NOT depend on framework specifics

---

# 7. CLI LAYER (RUNNER INTERFACE)

## Commands

### scan
Raw dependency extraction
```

cli.py scan file.php

```

---

### impact
Entity-level analysis
```

cli.py impact Entity controller.php model.php

```

---

### merge
Full pipeline:
```

scan + graph + normalize + enrich

```

Produces full entity_model.

---

### graph_engine analyze_file
Direct full pipeline execution (core-level API)

---

# 8. MEMORY LAYER (PERSISTENT KNOWLEDGE)

## Stored in SQLite

### Types:

- milestone
- decision
- insight
- pattern

## Purpose:

Store architectural evolution over time:
- how system behaves
- how entities change
- recurring patterns

---

# 9. RAW vs ENRICHED SEPARATION (CRITICAL CONTRACT)

## RAW DATA
- scan output
- graph output
- associations

NO interpretation

---

## ENRICHED DATA
- entity_model
- milestones
- insights
- patterns
- memory writes

WITH interpretation

---

## RULE:
> RAW must never depend on enriched layer

---

# 10. CURRENT SYSTEM STATE

## Implemented

✔ dependency scanner  
✔ method graph builder  
✔ association parser  
✔ entity model  
✔ normalization layer  
✔ enrichment engine  
✔ impact scoring  
✔ memory persistence  
✔ CLI interface  
✔ adapter system (CakePHP2)  
✔ propagation engine  

---

## Emerging capabilities

- architectural reasoning
- refactor risk scoring
- behavioral coupling detection
- persistent memory graph

---

# 11. ARCHITECTURAL INTENT

System is evolving into:

> "queryable architecture intelligence system"

Future capabilities:
- impact User
- why is this risky?
- what changed since last scan?
- dependency evolution tracking
```

---

# 12. USEFUL SYSTEM COMMANDS (OPERATIONAL CHEATSHEET)

## 🔍 ANALYSIS COMMANDS

### Scan (raw dependency extraction)

```bash id="scan_cmd"
python cli.py scan ../sic/app/Controller/UsersController.php --adapter cakephp2
```

---

### Impact (entity risk analysis)

```bash id="impact_cmd"
python cli.py impact User \
../sic/app/Controller/UsersController.php \
../sic/app/Model/User.php \
--adapter cakephp2
```

---

### Merge (full entity pipeline)

```bash id="merge_cmd"
python cli.py merge \
../sic/app/Controller/UsersController.php \
../sic/app/Model/User.php \
--adapter cakephp2
```

---

## 🧠 GRAPH ENGINE (CORE API)

### Full analysis pipeline

```bash id="graph_cmd"
python -c "from analysis.core.graph_engine import analyze_file; import json; print(json.dumps(analyze_file('../sic/app/Controller/UsersController.php','../sic/app/Model/User.php'), indent=2, ensure_ascii=False))"
```

---

## 💾 MEMORY COMMANDS

### Run migration (init DB)

```bash id="mem_migrate"
python memory/migrate.py
```

---

### Last recorded events

```bash id="mem_last"
python cli.py memory --last 20
```

---

### Full timeline (architecture history)

```bash id="mem_timeline"
python cli.py memory --timeline
```

---

### Search memory by entity

```bash id="mem_search"
python cli.py memory --search User
```

---

### Patterns (repeated architectural signals)

```bash id="mem_patterns"
python cli.py memory patterns
```

---

## 🧪 DEBUG / VALIDATION

### Direct entity inspection (raw output)

```bash id="debug_entity"
python cli.py merge ... --adapter cakephp2
```

(useful for verifying consistency between runner vs graph_engine)

---

## ⚠️ OPERATION RULE

All commands must respect:

* RAW layer = scan / graph extraction
* CORE layer = entity_model build
* ANALYTICS layer = impact + enrichment
* MEMORY layer = persistence only

---

# 🧠 PURPOSE OF THIS SECTION

This section exists to:

* provide quick operational access
* ensure reproducibility of analysis
* validate consistency between pipeline layers
* support debugging of runner vs graph_engine divergence
* serve as execution reference for CLI workflows

---

# 🧠 Почему эта версия хороша (важно)

## Для тебя:

* можно реально использовать как manual
* не перегружена текстом
* удобно расширять
* фиксирует архитектуру как spec

---

## Для меня (в будущем контексте):

* даёт полный reconstruction pipeline
* явно разделяет layers
* объясняет RAW vs enriched contract
* фиксирует intent системы
* позволяет восстанавливать логику анализа без кода

---

# 📌 Итог

Ты теперь фактически имеешь:

> 📐 “живую архитектурную спецификацию системы анализа кода”

а не просто документацию.

---

Если дальше пойдёшь правильно, следующий шаг будет:

👉 автоматически генерировать этот файл из CLI состояния (self-updating spec)

Но сейчас ты сделал правильный шаг: **зафиксировал систему до стабилизации graph/runner унификации**.
