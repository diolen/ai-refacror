Сейчас это лучший путь. Не расширять систему, а сделать controlled stabilization.

Я бы шел вот в таком порядке — это минимизирует regressions и позволит быстро вернуть систему в “рабочее ядро”.

# Stabilization Plan After Adapter Refactor

## Goal

Восстановить стабильность системы после перехода на adapter architecture.

Основная задача:

* вернуть работоспособность старых модулей;
* зафиксировать data contracts;
* устранить silent failures;
* подготовить систему к Prompt Builder layer.

---

# STEP 1 — Freeze Contracts

## Цель

Зафиксировать структуры данных между слоями.

## Нужно проверить

### dependency_scan.py

Должен возвращать:

```python
{
    "file": str,
    "dependencies": [
        {
            "name": str,
            "method": str,
            "frequency": int,
            "type": str
        }
    ]
}
```

---

### association_parser.py

Должен возвращать:

```python
{
    "model": str,
    "associations": {
        "belongsTo": [],
        "hasMany": [],
        "hasOne": [],
        "hasAndBelongsToMany": []
    }
}
```

---

### graph_builder.py

Должен возвращать:

```python
{
    "domain": {},
    "framework": {}
}
```

---

### entity_model.py

Должен принимать:

* dependency list
* association dict
* method graph

И возвращать:

```python
{
    "User": {
        "methods": [],
        "dependencies": [],
        "associations": {}
    }
}
```

---

# STEP 2 — Restore Timeline

## Цель

Вернуть historical memory layer.

## Проверить

* bootstrap_history.py
* graph_v2_history.py
* impact_analysis_history.py
* memory/db.py
* memory/view.py

## Нужно убедиться

Что новые adapters не сломали:

* history inserts;
* timeline rendering;
* pattern aggregation.

---

# STEP 3 — Restore Merge Engine

## Цель

Вернуть aggregation layer.

## Проверить

* merge command
* graph aggregation
* association merge
* dependency merge

## Результат

Команда:

```bash
python cli.py merge ...
```

должна снова работать.

---

# STEP 4 — Unified Output Layer

## Цель

Сделать единый формат вывода.

## Режимы

### Human mode

Для обычной работы.

### JSON mode

Для AI/pipeline integration.

### Debug mode

Для диагностики.

---

# STEP 5 — Remove Debug Noise

## Удалить

* [DEBUG]
* временные print()
* raw dumps

## Оставить

Только controlled debug mode.

---

# STEP 6 — Regression Protection

## Добавить smoke tests

Проверки:

```bash
python cli.py scan ...
python cli.py entity ...
python cli.py impact ...
python cli.py merge ...
```

## Цель

Не допускать silent breakage.

---

# STEP 7 — Adapter Validation Layer

## Цель

Проверять adapters до выполнения pipeline.

## Проверки

* структура graph
* структура associations
* структура dependencies

---

# STEP 8 — Prompt Builder Preparation

## Только после stabilization

Добавить:

```text
prompt_builder/
```

## Команды

```bash
python cli.py prompt ...
```

## Важно

LLM должен получать:

* только стабильный context;
* только normalized entities;
* только validated impact data.

Это как раз тот этап, где проект превращается из “набора модулей” в настоящую систему.
