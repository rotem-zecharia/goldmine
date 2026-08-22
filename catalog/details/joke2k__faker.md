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
