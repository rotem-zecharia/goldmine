# lk-geimfari/mimesis

Mimesis is a Python library for generating fake but realistic data in multiple languages and locales.

## installation

To install Mimesis, use pip:

```
~ pip install mimesis
```

## Documentation

You can find the complete documentation on the [Read the Docs](https://mimesis.name/).

It is divided into several sections:

-  [About Mimesis](https://mimesis.name/latest/about.html)
-  [Quickstart](https://mimesis.name/latest/quickstart.html)
-  [Locales](https://mimesis.name/latest/locales.html)
-  [Data Providers](https://mimesis.name/latest/providers.html)
-  [Structured Data Generation](https://mimesis.name/latest/schema.html)
-  [Relational Data Generation](https://mimesis.name/latest/relational.html)
-  [Random and Seed](https://mimesis.name/latest/random_and_seed.html)
-  [Integration with factory_boy](https://mimesis.name/latest/factory_plugin.html)
-  [API Reference](https://mimesis.name/latest/api.html)
-  [Changelog](https://mimesis.name/latest/index.html#changelog)

You can improve it by sending pull requests to this repository.

## tools

Import a data provider that corresponds to the data type you need.

For example, the [Person](https://mimesis.name/latest/api.html#person) provider gives access to personal information,
including name, surname, email, and other related fields:

```python
from mimesis import Person
from mimesis.locales import Locale

person = Person(Locale.EN)

person.full_name()
# Output: 'Brande Sears'

person.email(domains=['example.com'])
# Output: 'roccelline1878@example.com'

person.email(domains=['mimesis.name'], unique=True)
# Output: 'f272a05d39ec46fdac5be4ac7be45f3f@mimesis.name'

person.telephone(mask='1-4##-8##-5##3')
# Output: '1-436-896-5213'
```

## License

Mimesis is licensed under the MIT License. See [LICENSE](https://github.com/lk-geimfari/mimesis/blob/master/LICENSE) for more information.
