# joke2k/faker

Faker is a Python package that generates fake data for you.

## tools

Install with pip:

.. code:: bash

    pip install Faker

Use ``faker.Faker()`` to create and initialize a faker
generator, which can generate data by accessing properties named after
the type of data you want.

.. code:: python

    from faker import Faker
    fake = Faker()

    fake.name()
    # 'Lucy Cechtelar'

    fake.address()
    # '426 Jordy Lodge
    #  Cartwrightshire, SC 88120-6700'

    fake.text()
    # 'Sint velit eveniet. Rerum atque repellat voluptatem quia rerum. Numquam excepturi
    #  beatae sint laudantium consequatur. Magni occaecati itaque sint et sit tempore. Nesciunt
    #  amet quidem. Iusto deleniti cum autem ad quia aperiam.
    #  A consectetur quos aliquam. In iste aliquid et aut similique suscipit. Consequatur qui
    #  quaerat iste minus hic expedita. Consequuntur error magni et laboriosam. Aut aspernatur
    #  voluptatem sit aliquam. Dolores voluptatum est.
    #  Aut molestias et maxime. Fugit autem facilis quos vero. Eius quibusdam possimus est.
    #  Ea quaerat et quisquam. Deleniti sunt quam. Adipisci consequatur id in occaecati.
    #  Et sint et. Ut ducimus quod nemo ab voluptatum.'

Each call to method ``fake.name()`` yields a different (random) result.
This is because faker forwards ``faker.Generator.method_name()`` calls
to ``faker.Generator.format(method_name)``.

.. code:: python

    for _ in range(10):
      print(fake.name())

    # 'Adaline Reichel'
    # 'Dr. Santa Prosacco DVM'
    # 'Noemy Vandervort V'
    # 'Lexi O'Conner'
    # 'Gracie Weber'
    # 'Roscoe Johns'
    # 'Emmett Lebsack'
    # 'Keegan Thiel'
    # 'Wellington Koelpin II'
    # 'Ms. Karley Kiehn V'

Pytest fixtures
---------------

``Faker`` also has its own ``pytest`` plugin which provides a ``faker`` fixture you can use in your
tests. Please check out the `pytest fixture docs` to learn more.

Providers
---------

Each of the generator properties (like ``name``, ``address``, and
``lorem``) are called "fake". A faker generator has many of them,
packaged in "providers".

.. code:: python

    from faker import Faker
    from faker.providers import internet

    fake = Faker()
    fake.add_provider(internet)

    print(fake.ipv4_private())


Check the `extended docs`_ for a list of `bundled providers`_ and a list of
`community providers`_.

Localization
------------

``faker.Faker`` can take a locale as an argument, to return localized
data. If no localized provider is found, the factory falls back to the
default LCID string for US english, ie: ``en_US``.

.. code:: python

    from faker import Faker
    fake = Faker('it_IT')
    for _ in range(10):
        print(fake.name())

    # 'Elda Palumbo'
    # 'Pacifico Giordano'
    # 'Sig. Avide Guerra'
    # 'Yago Amato'
    # 'Eustachio Messina'
    # 'Dott. Violante Lombardo'
    # 'Sig. Alighieri Monti'
    # 'Costanzo Costa'
    # 'Nazzareno Barbieri'
    # 'Max Coppola'

``faker.Faker`` also supports multiple locales. New in v3.0.0.

.. code:: python

    from faker import Faker
    fake = Faker(['it_IT', 'en_US', 'ja_JP'])
    for _ in range(10):
        print(fake.name())

    # 鈴木 陽一
    # Leslie Moreno
    # Emma Williams
    # 渡辺 裕美子
    # Marcantonio Galuppi
    # Martha Davis
    # Kristen Turner
    # 中津川 春香
    # Ashley Castillo
    # 山田 桃子

You can check available Faker locales in the source code, under the
providers package. The localization of Faker is an ongoing process, for
which we need your help. Please don't hesitate to create a localized
provider for your own locale and submit a Pull Request (PR).

Optimizations
-------------
The Faker constructor takes a performance-related argument called
``use_weighting``. It specifies whether to attempt to have the frequency
of values match real-world frequencies (e.g. the English name Gary would
be much more frequent than the name Lorimer). If ``use_weighting`` is ``False``,
then all items have an equal chance of being selected, and the selection
process is much faster. The default is ``True``.

Com
