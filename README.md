# ai-refactor

## Структура проекта

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
├── analysis/
│   ├── adapters/
│   │   └── cakephp2/
│   │       ├── association_parser.py
│   │       ├── dependency_scan.py
│   │       └── graph_builder.py
│   ├── core/
│   │   ├── entity_filter.py
│   │   ├── entity_model.py
│   │   ├── entity_normalizer.py
│   │   ├── graph_engine.py
│   │   └── impact_engine.py
├── core/
│   ├── llm.py
│   ├── parser.py
│   └── patcher.py
├── memory/
│   ├── cleanup.py
│   ├── db.py
│   ├── init_db.py
│   ├── migrate.py
│   └── view.py
└── prompts/
    └── refactor.txt
```

Ниже — roadmap, который уже соответствует текущей архитектуре проекта и тому направлению, куда вы пришли после adapter refactor.

# AI Refactor System Roadmap

## Vision

Создать framework-agnostic систему архитектурного анализа и AI-assisted refactoring для legacy-проектов.

Система должна:

* анализировать структуру legacy-кода;
* понимать связи между сущностями;
* оценивать refactor risk;
* хранить архитектурную память проекта;
* помогать безопасно эволюционировать legacy-системы.

---

# STAGE 1 — FOUNDATION CORE

## 1. CLI Infrastructure

Базовый CLI-движок системы.

### Цель

Создать единый вход для всех операций анализа и refactoring.

### Модули

* cli.py
* command dispatcher
* usage/help system
* argument validation

### Статус

Mostly completed.

---

## 2. Local AI Integration

Интеграция локальных LLM.

### Цель

Обеспечить offline AI refactoring pipeline.

### Модули

* Ollama integration
* prompt pipeline
* response sanitizer
* code transformer

### Статус

Completed baseline.

---

## 3. Memory System

Историческая память проекта.

### Цель

Сохранять архитектурные знания и refactor history.

### Модули

* SQLite storage
* timeline
* pattern storage
* historical insights
* change tracking

### Статус

Partially stabilized.

---

# STAGE 2 — STATIC ANALYSIS CORE

## 4. Dependency Scanner

Анализ зависимостей контроллеров и моделей.

### Цель

Построение базового dependency graph.

### Модули

* dependency_scan.py
* framework filtering
* helper filtering
* frequency tracking

### Статус

Working.

---

## 5. Method Graph Engine

Построение behavioral graph.

### Цель

Понимать какие методы вызываются и как связаны сущности.

### Модули

* graph_builder.py
* method extraction
* domain/framework separation

### Статус

Working baseline.

---

## 6. Association Parser

Парсинг ORM-связей.

### Цель

Понимать indirect domain coupling.

### Модули

* belongsTo parser
* hasMany parser
* HABTM parser
* normalization layer

### Статус

Working baseline.

---

## 7. Unified Entity Model

Единый архитектурный слой.

### Цель

Объединить:

* зависимости,
* associations,
* behavioral graph,
* memory insights.

### Модули

* entity_model.py
* normalization
* identity resolution
* entity filtering

### Статус

Core implemented.

---

# STAGE 3 — IMPACT ANALYSIS

## 8. Impact Engine

Система оценки риска изменений.

### Цель

Понимать насколько опасно менять сущность.

### Модули

* connectivity scoring
* dependency weighting
* behavioral heuristics
* business logic detection

### Статус

Working baseline.

---

## 9. Architectural Insights

Объяснимый анализ системы.

### Цель

Генерировать human-readable reasoning.

### Модули

* insights engine
* heuristic explanations
* risk explanations
* aggregation detection

### Статус

Early stage.

---

## 10. Historical Intelligence

Использование memory в анализе.

### Цель

Учитывать исторические знания проекта.

### Модули

* historical weighting
* recurring patterns
* change propagation memory
* historical risk amplification

### Статус

Partially implemented.

---

# STAGE 4 — ADAPTER ARCHITECTURE

## 11. Framework Adapters

Framework-specific parsing layer.

### Цель

Сделать core независимым от framework.

### Модули

* adapters/cakephp2
* adapters/laravel
* adapters/symfony
* adapters/custom_php

### Статус

CakePHP2 adapter implemented.

---

## 12. Adapter Contracts

Стандартизация adapter API.

### Цель

Сделать adapters interchangeable.

### Модули

* parser contracts
* graph contracts
* entity contracts
* adapter registry

### Статус

Planned.

---

# STAGE 5 — REFACTOR INTELLIGENCE

## 13. Safe Refactor Engine

AI-assisted safe transformations.

### Цель

Автоматизировать безопасный refactor.

### Модули

* safe rewrite validation
* business logic preservation
* semantic verification
* rollback support

### Статус

Early prototype exists.

---

## 14. Merge & Propagation Engine

Propagation-aware refactoring.

### Цель

Понимать chain impact изменений.

### Модули

* merge graph
* cross-entity propagation
* blast radius estimation
* architectural cascade detection

### Статус

Planned.

---

## 15. Refactor Recommendations

Архитектурные рекомендации.

### Цель

Подсказывать направления улучшения legacy-кода.

### Модули

* service extraction hints
* god-controller detection
* coupling reduction hints
* dead dependency detection

### Статус

Planned.

---

# STAGE 6 — ADVANCED ARCHITECTURE INTELLIGENCE

## 16. Architectural Memory Graph

Knowledge graph проекта.

### Цель

Хранить evolving architecture knowledge.

### Модули

* graph persistence
* entity evolution tracking
* historical architecture map
* dependency evolution

### Статус

Future stage.

---

## 17. Explainable AI Layer

Объяснимый reasoning.

### Цель

Показывать почему система пришла к выводу.

### Модули

* reasoning traces
* scoring explanations
* confidence estimation
* impact explanation tree

### Статус

Future stage.

---

## 18. Multi-Project Intelligence

Cross-project learning.

### Цель

Накапливать reusable architectural patterns.

### Модули

* reusable patterns
* framework heuristics
* anti-pattern memory
* domain archetypes

### Статус

Research stage.

---

# STAGE 7 — STABILIZATION

## 19. Regression Protection

Защита от architectural regressions.

### Цель

Стабилизировать evolving architecture.

### Модули

* smoke tests
* CLI validation
* adapter validation
* graph consistency tests

### Статус

Needed now.

---

## 20. Output Layer

Единый presentation layer.

### Цель

Унифицировать CLI output.

### Модули

* human-readable reports
* JSON mode
* debug mode
* export layer

### Статус

Partially implemented.

---

# LONG-TERM DIRECTION

Система постепенно движется от:

* simple static analyzer

к:

* architectural intelligence platform

которая:

* понимает legacy architecture;
* хранит историю системы;
* оценивает refactor risk;
* помогает безопасной эволюции больших legacy-кодовых баз.

## 21. Prompt Builder

### Цель

* Превратить LLM из:

“анализатора кода”
в:
“архитектурного консультанта, работающего на основе модели системы”

* Layer 1 — deterministic engine (система)
graph
impact
entity model
memory

* Layer 2 — reasoning engine (LLM)
refactor plan
explanations
design decisions

* Добавить CLI:
python cli.py prompt User UsersController.php User.php

### Модули

* prompt_builder/
    entity_prompt.py
    impact_prompt.py
    refactor_prompt.py

### Статус

Research stage.
