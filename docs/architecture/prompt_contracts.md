Вот переработанный вариант `docs/architecture/prompt_contracts.md` — уже в формате, который можно использовать как **архитектурный контракт**, а не просто описание идеи.

---

```md
# Prompt Contracts Layer

## 1. Purpose

Prompt layer is a **translation boundary** between deterministic architecture analysis and LLM reasoning.

It converts:
- structured internal data (entity_model, impact, memory)
→ into LLM-compatible prompts

and converts:
- LLM responses
→ back into structured system data

### Key principle

> LLM is a plugin, not the system core.

---

## 2. Architecture Position

Prompt layer sits between:

```

entity_model → impact_engine → prompt_contracts → LLM → structured_output → memory/CLI

````

It does NOT:
- compute metrics
- analyze dependencies
- mutate entity model
- define business logic

It ONLY translates and normalizes.

---

## 3. Core Design Rules

### 3.1 LLM independence

Prompt contracts MUST NOT depend on:
- specific LLM provider (OpenAI / Ollama / Claude)
- model-specific prompt tuning
- response quirks of any model

LLM is replaceable via adapter layer only.

---

### 3.2 Deterministic input

All prompts MUST be built from structured data:

- entity_model
- impact result
- dependency graph
- memory insights

No raw code parsing inside prompt layer.

---

### 3.3 Structured output only

LLM outputs MUST be parsed into strict schemas.

No free-form text is allowed as final system output.

---

## 4. Contract Types

The system uses 3 main prompt contracts:

---

# 4.1 Entity Contract

## Input Schema

```json
{
  "entity": "User",
  "methods": [],
  "dependencies": [],
  "associations": {},
  "timeline": [],
  "insights": [],
  "patterns": []
}
````

---

## Prompt Goal

Explain entity behavior and structure.

---

## LLM Output Schema

```json
{
  "summary": "",
  "risk_level": "low | medium | high",
  "coupling_analysis": "",
  "refactor_suggestions": []
}
```

---

## Responsibility Boundary

Entity contract does NOT:

* compute complexity
* compute coupling score
* build graphs

---

# 4.2 Impact Contract

## Input Schema

```json
{
  "entity": "User",
  "score": 15.2,
  "connectivity": 3,
  "methods": [],
  "insights": []
}
```

---

## Prompt Goal

Interpret impact score and explain architectural risk.

---

## LLM Output Schema

```json
{
  "interpretation": "",
  "risk_explanation": "",
  "architecture_notes": "",
  "warnings": []
}
```

---

## Responsibility Boundary

LLM does NOT:

* calculate score
* modify entity graph
* decide dependencies

It ONLY explains existing computed metrics.

---

# 4.3 Refactor Contract

## Input Schema

```json
{
  "entity_model": {},
  "impact": {},
  "patterns": []
}
```

---

## Prompt Goal

Generate safe refactoring recommendations.

---

## LLM Output Schema

```json
{
  "recommendations": [
    {
      "type": "extract_service | split_controller | remove_coupling",
      "reason": "",
      "priority": "low | medium | high"
    }
  ],
  "risk_notes": []
}
```

---

## Responsibility Boundary

LLM does NOT:

* execute refactoring
* validate code correctness
* modify system state

---

## 5. Prompt Construction Rules

All prompts MUST follow:

### 5.1 Structured input first

Internal data → normalized dictionary → prompt rendering

### 5.2 No hidden system context

No implicit assumptions about:

* framework behavior
* code semantics
* business logic

Everything must be explicit in input.

---

### 5.3 Minimal prompt surface

Prompts should only include:

* entity data
* impact data
* associations
* derived insights

NOT raw code unless explicitly required.

---

## 6. LLM Adapter Independence

Prompt layer does not know:

* which model is used
* context window size
* temperature
* token limits

That is handled by:

```
prompt_builder/llm/
```

---

## 7. Output Processing Pipeline

```
LLM response
   ↓
parse_output()
   ↓
validation layer (future)
   ↓
entity_model / impact / memory
```

---

## 8. System Guarantees

This layer guarantees:

✔ reproducible prompts
✔ structured outputs
✔ model independence
✔ separation from core logic
✔ deterministic system behavior

---

## 9. Non-Goals

Prompt layer is NOT responsible for:

* dependency scanning
* graph building
* memory persistence
* scoring algorithms
* CLI formatting

---

## 10. Design Intent

This system is designed to evolve into:

> multi-LLM architecture intelligence layer

where:

* different models can be swapped
* outputs can be compared
* reasoning can be audited
* architectural decisions can be traced

without touching core engine.

```

---

Если дальше пойдёшь в этом направлении, следующий логичный шаг будет не код, а усиление контракта:

👉 добавить **JSON Schema validation (pydantic / jsonschema)**  
чтобы prompt layer стал строго типизированным API, а не просто текстовым трансформером.
```
