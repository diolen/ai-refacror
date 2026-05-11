Ок, давай сделаем это как **чистый туториал**, без “внутренних размышлений”, чтобы ты мог просто заменить файл и дальше на него опираться.

---

# 📄 `docs/architecture/commit_taxonomy.md` (TUTORIAL VERSION)

```markdown
# 🧠 AI Refactor System — Commit Taxonomy (Tutorial)

## 📌 Purpose

This document defines how commits are written in the AI Refactor System.

Instead of generic Git labels like:

- feat
- fix
- refactor

we use **architecture-aware semantic commit types**.

### Goal

Make Git history readable as:

> 🧠 architectural evolution of the system

---

# 🏗️ CORE PRINCIPLE

Every commit MUST describe:

- which architectural layer changed
- what system responsibility was affected
- what behavior or reasoning changed

NOT just code changes.

---

# 📊 ARCHITECTURAL LAYERS

The system is divided into 5 main layers:

```

RAW → CORE → GRAPH → ENRICHMENT → IMPACT → PROMPT → MEMORY → ADAPTER → SYSTEM

````

Each layer has its own commit prefix.

---

# 1. RAW LAYER (DATA EXTRACTION)

### Prefix:
```text
raw(...)
````

### Meaning:

Changes in raw code parsing logic.

### Includes:

* dependency scanning
* method extraction
* ORM parsing
* graph input data

### Examples:

```text
raw(scan): extract dependency frequency from controller
raw(graph): improve method call extraction
raw(association): fix belongsTo parsing
```

---

# 2. CORE ENTITY LAYER

### Prefix:

```text
core(...)
```

### Meaning:

Changes in unified entity representation.

### Includes:

* entity_model structure
* normalization
* filtering
* identity resolution

### Examples:

```text
core(entity): unify dependency and association model
core(normalizer): improve entity name normalization
core(model): restructure entity schema
```

---

# 3. GRAPH LAYER

### Prefix:

```text
graph(...)
```

### Meaning:

Changes in dependency / method relationship graphs.

### Includes:

* method graph building
* dependency propagation
* transitive relationships

### Examples:

```text
graph(build): improve method dependency resolution
graph(propagation): add multi-depth traversal
graph(method): fix domain vs framework separation
```

---

# 4. ENRICHMENT LAYER

### Prefix:

```text
enrich(...)
```

### Meaning:

Adds behavioral intelligence to entities.

### Includes:

* timeline generation
* patterns detection
* milestones
* insights
* decisions

### Examples:

```text
enrich(patterns): detect repeated dependency usage
enrich(timeline): add method execution history tracking
enrich(insights): improve coupling classification
```

---

# 5. IMPACT LAYER

### Prefix:

```text
impact(...)
```

### Meaning:

Changes in scoring and risk evaluation.

### Includes:

* impact score
* connectivity score
* risk classification

### Examples:

```text
impact(score): refine scoring model for dependencies
impact(connectivity): improve graph weight calculation
impact(risk): adjust aggregation risk detection
```

---

# 6. PROMPT LAYER (LLM INTERFACE)

### Prefix:

```text
prompt(...)
```

### Meaning:

Changes in LLM prompt generation logic.

### Includes:

* prompt structure
* renderer formatting
* entity → LLM mapping

### Examples:

```text
prompt(impact): include full enriched entity context
prompt(renderer): improve CLI output formatting
prompt(refactor): add structured reasoning output
```

---

# 7. MEMORY LAYER

### Prefix:

```text
memory(...)
```

### Meaning:

Changes in persistent architectural memory.

### Includes:

* milestones
* decisions
* insights
* patterns

### Examples:

```text
memory(insight): persist coupling classification signals
memory(milestone): track entity usage thresholds
memory(decision): store normalization decisions
```

---

# 8. ADAPTER LAYER

### Prefix:

```text
adapter(...)
```

### Meaning:

Framework-specific logic isolation.

### Includes:

* CakePHP parsing
* framework adapters
* extraction rules per framework

### Examples:

```text
adapter(cakephp2): isolate association parsing logic
adapter(scan): improve dependency extraction rules
adapter(graph): fix framework filtering in graph builder
```

---

# 9. SYSTEM LAYER

### Prefix:

```text
system(...)
```

### Meaning:

Cross-layer architectural changes.

### Includes:

* CLI system
* pipeline orchestration
* architecture-wide changes

### Examples:

```text
system(cli): unify command structure for analysis pipeline
system(prompt): integrate entity_model into prompt flow
system(architecture): refactor full analysis pipeline structure
```

---

# 🧾 COMMIT FORMAT RULE

### Standard format:

```text
<layer>(<scope>): <short description>
```

### Examples:

```text
core(entity): unify entity normalization logic
raw(scan): add dependency frequency tracking
graph(build): improve method graph resolution
enrich(patterns): detect repeated calls
impact(score): refine connectivity weighting
prompt(impact): include enriched context in prompt
memory(insight): persist architectural signals
adapter(cakephp2): isolate parsing logic
system(cli): unify prompt command flow
```

---

# 🧠 HOW TO USE THIS SYSTEM

## Step 1

Identify what layer changed

## Step 2

Choose correct prefix

## Step 3

Describe ONLY one responsibility change per commit

---

# ⚠️ RULES

### ❌ Do NOT use:

* feat:
* fix:
* refactor:

### ❌ Do NOT mix layers:

```text
core + graph + impact in one commit ❌
```

### ✅ Do:

One commit = one architectural intent

---

# 🚀 WHY THIS EXISTS

This system makes Git history:

* readable as architecture evolution
* traceable across layers
* useful for debugging reasoning
* compatible with AI analysis

---

# 🧠 RESULT

Git becomes:

> architectural event log of the system

```

---

# 📌 Готово

Это теперь:

- чистый туториал
- без лишней теории
- можно прямо заменить файл
- и сразу использовать как стандарт команды

---

Если дальше пойдёшь, следующий шаг будет очень сильный:

👉 автоматическая генерация commit message из CLI изменений (commit suggestion engine)

Но сейчас у тебя уже нормальная база, можно спокойно продолжать разработку без хаоса в git истории.
```
