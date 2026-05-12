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
Вот обновленный `analysis_system_spec.md` с командами для управления системой, добавленными в конец файла:

```markdown
# Анализ Системы

## Команды управления системой

### 1. Работа с снапшотами памяти
```bash
# Сохранить текущее состояние системы в файл state.md
memory snapshot --write state.md

# Применить изменения из патча к системе
cli.py memory apply patch.diff

# Список всех сохраненных снапшотов
snapshot list
```

### 2. Управление зависимостями
```bash
# Сгенерировать граф зависимостей для указанной сущности
prompt impact <entity_name>

# Обновить модель сущностей с учетом новых зависимостей
entity_model update --dependencies <dependency_list>
```

### 3. Синхронизация с чатом
```bash
# Применить изменения, полученные от LLM (через чат)
cli.py memory apply --from-chat

# Синхронизировать состояние системы с последним снапшотом
sync state.md
```

### 4. Работа с патчами
```bash
# Создать патч на основе изменений в системе
diff generate --output changes.patch

# Применить патч к текущему состоянию
patch apply changes.patch
```

### 5. Управление архитектурными решениями
```bash
# Добавить новое архитектурное решение в memory
memory add decision "<decision_description>"

# Показать историю принятых решений
memory decisions
```

### 6. Анализ регрессий
```bash
# Сравнить текущее состояние с предыдущим снапшотом
diff analyze --baseline previous_state.md

# Найти деградации в архитектуре
regression detect
```

## Примечания
- Все команды должны быть реализованы через CLI как оболочку для взаимодействия с memory layer.
- Патчи и снапшоты должны сохраняться в формате, совместимом с `state.md`.
- При работе с LLM все команды должны использовать структурированный формат обмена данными (JSON, diff).
```

---

### Где найти дополнительную информацию:
1. Конкретная реализация команд находится в `memory/db.py` (функции `save_snapshot`, `list_snapshots`, `apply_patch`).
2. Логика работы с патчами описана в `docs/architecture/memory_layer.md`.
3. Примеры использования CLI приведены в `docs/architecture/prompt_contracts.md`.