# MarshalX/telegram-crawler

🕷 Automatically detects changes to the official Telegram sites, beta clients, MTProto servers and mini apps

## configuration

Every rule is a regex. Allow rules have higher priority than deny ones,
and an empty string matches any URL. For example, this keeps only the root,
the first level pages and the English categories of the translations platform:

```python
CRAWL_RULES = {
    'translations.telegram.org': {
        'allow': {
            r'^[^/]*$',  # root
            r'org/[^/]*/$',  # 1 lvl sub
            r'/en/[a-z_]+/$'  # 1 lvl after /en/
        },
        'deny': {
            '',  # all
        }
    },
