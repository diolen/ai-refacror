# Smoke Test System

## Goal

Validate that the architectural pipeline is operational.

---

# Validation Stages

## Stage 1

Scan pipeline:

- adapter
- parser
- entity_model

---

## Stage 2

Impact engine:

- graph
- impact scoring
- connectivity

---

## Stage 3

Prompt builder:

- rendering
- impact context
- entity targeting

---

## Stage 4

Memory system:

- database access
- retrieval
- persistence

---

## Stage 5

Entity history:

- entity lookup
- timeline retrieval

---

# Run Validation

```bash
python tests/smoke/validate_system.py