# Отчёты по данным сессии (CSV)

Скрипт объединяет строки из нескольких CSV с колонками `student`, `date`, `coffee_spent`, … и строит отчёт по ключу `--report`. Сейчас реализован только `median-coffee`: медиана трат на кофе по каждому студенту по всем файлам, сортировка по убыванию медианы.

Новые отчёты добавляются классом в `exam_reports/`, регистрацией в `exam_reports/registry.py`.

## Пример запуска

Из корня репозитория (рядом с `main.py`):

```bash
python main.py --files examples/math.csv examples/physics.csv examples/programming.csv --report median-coffee
```

Те же имена файлов в текущей папке:

```bash
python main.py --files math.csv physics.csv programming.csv --report median-coffee
```

Для ревьюера: приложите скриншот запуска на ваших полных данных (как в задании) — так проще сверить таблицу.

## Тесты

```bash
pip install -r requirements.txt
pytest
```
