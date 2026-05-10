Вот уже обновлённый блок для README с учётом того, что у тебя реально есть сейчас в проекте (prompt_builder, enrich pipeline, layered connectivity и adapter architecture уже отражены корректнее).

# ai-refactor

AI-assisted architectural analysis and safe refactoring platform for legacy PHP systems.

---

# Vision

Создать framework-agnostic систему архитектурного анализа и AI-assisted refactoring для legacy-проектов.

Система должна:

* анализировать структуру legacy-кода;
* понимать связи между сущностями;
* оценивать refactor risk;
* хранить архитектурную память проекта;
* помогать безопасно эволюционировать legacy-системы.

---

# Current Architecture

```text
ai-refactor/
├── .gitignore
├── README.md
├── requirements.txt
├── cli.py
├── bootstrap_history.py
├── graph_v2_history.py
├── impact_analysis_history.py
├── memory.db
├── memory_tmp.txt
│
├── analysis/
│   ├── adapters/
│   │   └── cakephp2/
│   │       ├── association_parser.py
│   │       ├── dependency_scan.py
│   │       ├── graph_builder.py
│   │       └── runner.py
│   │
│   ├── core/
│   │   ├── entity_filter.py
│   │   ├── entity_model.py
│   │   ├── entity_normalizer.py
│   │   ├── entity_enricher.py
│   │   ├── graph_engine.py
│   │   ├── impact_engine.py
│   │   │
│   │   └── prompt_builder/
│   │       ├── entity_prompt.py
│   │       ├── impact_prompt.py
│   │       ├── refactor_prompt.py
│   │       ├── prompt_context.py
│   │       └── prompt_renderer.py
│
├── core/
│   ├── llm.py
│   ├── parser.py
│   └── patcher.py
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

# Current System Capabilities

## Static Analysis

* Dependency scanning
* ORM association parsing
* Behavioral method graph extraction
* Framework/domain separation
* Entity normalization
* Framework filtering

---

## Architectural Intelligence

* Unified entity model
* Connectivity-aware impact analysis
* Behavioral heuristics
* Refactor risk estimation
* Aggregation root detection
* Business logic detection
* Frequency-aware dependency analysis

---

## Memory System

* Milestones
* Decisions
* Insights
* Patterns
* Historical persistence
* Timeline generation

---

## Prompt Builder

Structured LLM prompts generated from:

* entity model
* impact analysis
* architectural context
* behavioral graph
* memory system

Goal:
move LLM usage from:

```text
code completion
```

to:

```text
architecture-aware reasoning
```

---

# CLI Commands

## Scan Dependencies

```bash
python cli.py scan Controller.php --adapter cakephp2
```

---

## Impact Analysis

```bash
python cli.py impact User \
Controller.php \
User.php \
--adapter cakephp2
```

---

## Merge Entity Model

```bash
python cli.py merge \
Controller.php \
User.php \
--adapter cakephp2
```

---

# Architectural Direction

The system is evolving from:

```text
simple static analyzer
```

toward:

```text
architectural intelligence platform
```

The long-term goal is a system capable of:

* understanding legacy architecture;
* estimating propagation risk;
* preserving architectural memory;
* generating explainable refactor guidance;
* supporting safe AI-assisted evolution of large legacy systems.

---

# Core Architectural Concepts

## Layered Connectivity Model

Impact analysis currently combines:

* dependency connectivity
* association connectivity
* behavioral connectivity

This creates a more realistic architectural risk model than traditional static dependency counting.

---

## Behavioral Graph Analysis

The system distinguishes between:

```text
domain interactions
```

and:

```text
framework interactions
```

allowing architectural reasoning to focus on business-critical entities.

---

## Adapter Architecture

Framework-specific parsing is isolated from the core intelligence engine.

Current adapter support:

* CakePHP 2

Planned:

* Laravel
* Symfony
* Custom PHP adapters

---

# Current Development Stage

The project is currently transitioning from:

```text
static analysis engine
```

to:

```text
behavior-aware architectural intelligence system
```

Main active areas:

* propagation-aware impact analysis
* graph density modeling
* explainable architectural reasoning
* AI-assisted safe refactoring
