from pelican import signals
from pelican.generators import PagesGenerator, ArticlesGenerator

_LANGUAGES = {
    'en': 'English',
    'uk': 'Українська',
}

_LANGUAGES_TRANSLATION_LINK_TEXT = {
    'en': 'View English version',
    'uk': 'Переглянути Українську версію',
}

content_types = {
    PagesGenerator: 'pages',
    ArticlesGenerator: 'articles',
}


def translations_extra(generator):
    """
    Add `full_language_name` and `translation_link_text` attributes to article translations.

    List of available translation languages:

    .. code-block:: html


        {% for translation in article.translations -%}
            <a href="{{ translation.url }}">{{ translation.full_language_name }}</a>
        {%- endfor %}

        <a href="/en/article">English</a>
        <a href="/sk/article">Slovak</a>

    Custom text for translation link:

    .. code-block: html

        {% for translation in article.translations -%}
            <a href="{{ translation.url }}">{{ translation.translation_link_text }}</a>
        {%- endfor %}

        <a href="/en/article">View English version</a>
    """
    settings = generator.settings
    full_name = settings.get('LANGUAGES', _LANGUAGES)
    translation_link_text = settings.get('LANGUAGES_TRANSLATION_LINK_TEXT', _LANGUAGES_TRANSLATION_LINK_TEXT)

    objects = []
    field = content_types[generator.__class__]

    for obj in generator.context.get(field, []):
        for translation in getattr(obj, 'translations', []):
            translation.full_language_name = full_name.get(translation.lang, None)
            translation.translation_link_text = translation_link_text.get(translation.lang, None)

        objects.append(obj)

    generator.context[field] = objects


def register():
    signals.page_generator_finalized.connect(translations_extra)
    signals.article_generator_finalized.connect(translations_extra)
