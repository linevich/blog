"""
Pelican Creative Commons
------------------------

Set of classes for CC License setting. Provides a context variable with license name, url and icon.

Usage
=====

.. code-block: python

    from core import cc
    CC_LICENSE = cc.AttributionShareAlike

.. code-block: html

    <a rel="license" href="{{ license.url }}" target="_blank">
        <img alt="Creative Commons License" src="{{ license.icon }}">
    </a> Content licensed under a <a rel="license" href="{{ license.url }}" target="_blank">{{ license.full_name }}</a>,
    except where indicated otherwise.

Settings
========

- `CC_LICENSE` required --- license class (not instance!).
- `CC_VERSION` optional, default: 4.0 --- license version.
- `CC_ICON_FOLDER` optional, default: `/{theme_name}/images/cc` --- absolute URI to folder with icons.
- `CC_ICON_FORMAT` optional, default: svg --- icons file format.
"""

import os
import logging

from pelican import signals

logger = logging.getLogger(__name__)


def add_context(generator):
    settings = generator.settings
    cc_license = settings.get('CC_LICENSE', None)

    if not cc_license:
        logger.warning('No CC_LICENSE defined')
        return

    version = settings.get('CC_VERSION', '4.0')
    theme = os.path.basename(generator.theme)
    icons_folder = settings.get('CC_ICON_FOLDER', os.path.join('/', theme, 'images/cc'))
    icon_format = settings.get('CC_ICON_FORMAT', 'svg')

    generator.context.update({
        'license': cc_license(version, icons_folder, icon_format)
    })


def register():
    signals.generator_init.connect(add_context)


class CCLicense(object):
    code = NotImplemented
    name = NotImplemented

    def __init__(self, version, icon_folder, icon_format):
        self.version = version
        self.icon_folder = icon_folder
        self.icon_format = icon_format

    @property
    def icon(self):
        return os.path.join(self.icon_folder, self.icon_format, '{}.{}'.format(self.code, self.icon_format))

    @property
    def url(self):
        return 'https://creativecommons.org/licenses/{}/{}/'.format(self.code, self.version)

    @property
    def full_name(self):
        return 'Creative Commons {} {} International'.format(self.name, self.version)


class Attribution(CCLicense):
    code = 'by'
    name = 'Attribution'


class AttributionShareAlike(CCLicense):
    code = 'by-sa'
    name = 'Attribution-ShareAlike'


class AttributionNoDerivs(CCLicense):
    code = 'by-nd'
    name = 'Attribution-NoDerivs'


class AttributionNonCommercial(CCLicense):
    code = 'by-nc'
    name = 'Attribution-NonCommercial'


class AttributionNonCommercialShareAlike(CCLicense):
    code = 'by-nc-sa'
    name = 'Attribution-NonCommercial-ShareAlike'


class AttributionNonCommercialNoDerivs(CCLicense):
    code = 'by-nc-nd'
    name = 'Attribution-NonCommercial-NoDerivs'
