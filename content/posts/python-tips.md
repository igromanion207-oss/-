---
title: 5 приёмов Python, которые я использую каждый день
date: 2026-10-20
summary: f-строки, pathlib, enumerate и другие мелочи, делающие код чище.
tags: [python]
---

## 1. f-строки

```python
name = "Xagan6_9"
print(f"Привет, {name}!")
```

## 2. pathlib вместо os.path

```python
from pathlib import Path
for file in Path("downloads").glob("*.pdf"):
    print(file.name)
```

## 3. enumerate

```python
for i, item in enumerate(["a", "b", "c"], start=1):
    print(i, item)
```

## 4. Распаковка

```python
first, *rest = [1, 2, 3, 4]
```

## 5. Генераторы списков

```python
squares = [x * x for x in range(10) if x % 2 == 0]
```
