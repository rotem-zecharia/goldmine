# lk-geimfari/mimesis

Mimesis is a Python library for generating fake but realistic data in multiple languages and locales.

## installation

To install Mimesis, use pip:

```
~ pip install mimesis
```

## tools

Import a data provider that corresponds to the data type you need.

For example, the [Person](https://mimesis.name/latest/api.html#person) provider gives access to personal information,
including name, surname, email, and other related fields:

```python
from mimesis import Person
from mimesis.locales import Locale

person = Person(Locale.EN)

person.full_name()
