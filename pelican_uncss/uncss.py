import os
import logging
import subprocess
from bs4 import BeautifulSoup

from glob import glob
from multiprocessing import Pool


class Uncss(object):
    def __init__(self, sender):
        self.sender = sender
        self.settings = self.sender.settings

        self.uncss_bin = self.get_settings(
            'UNCSS_BIN',
            '/usr/bin/uncss',
            executable=True
        )
        self.css_path = self.get_settings('UNCSS_CSS_PATH')
        self.html_root = self.get_settings('OUTPUT_PATH')
        self.stylesheets = self.settings['UNCSS_STYLESHEETS']

        self.yuicompressor_bin = self.get_settings(
            'YUICOMPRESSOR_BIN',
            '/usr/bin/yuicompressor',
            executable=True
        )

        self.templates_path_glob = self.get_settings('UNCSS_TEMPLATES_PATHS', [
            self.html_root + '/*.html',
            self.html_root + '/**/*.html'
        ])

        self.templates_path = self.get_templates_path()

        self.pool = Pool()

    def __getstate__(self):
        self_dict = self.__dict__.copy()
        del self_dict['pool']
        return self_dict

    def __setstate__(self, state):
        self.__dict__.update(state)

    def get_settings(self, variable_name, fallback=None, executable=False):
        """
        Returns value for given variable name in settings or raise exception.

        :param variable_name: VARIABLE_NAME located in pelicanconf.py file.
        :type variable_name: str
        :param fallback: fallback value
        :param executable: check if fallback value exists as executable binary.
        :return: value for given variable name.
        """
        try:
            return self.settings[variable_name]
        except:
            if fallback and not executable:
                return fallback
            elif os.path.exists(fallback):
                return fallback
            else:
                raise Exception('{} is not set in your pelicanconf.py'.format(variable_name))

    def get_templates_path(self):
        """
        Return list of template files.

        :return: list of template files.
        :rtype: list
        """
        templates_path = []
        for path in self.templates_path_glob:
            for file in glob(path):
                templates_path.append(file)

        return templates_path

    def run_uncss(self, file):
        logging.info('Processing {}....\n'.format(file))

        try:
            return subprocess.check_output(
                [
                    self.uncss_bin,
                    file,
                    '--csspath',
                    os.path.join(
                        os.path.relpath(self.css_path, file), 'output'
                    )
                ],
            )
        except:
            return False

    def inline_css(self, css):
        # TODO: Implement inlining css
        return css

    def patch_file(self, file, css_file):
        html = BeautifulSoup(open(file), 'html.parser')
        [tag.decompose() for tag in html.findAll('link', rel='stylesheet')]
        style = html.new_tag('style')
        style.string = css_file
        html.find('head').insert(1, style)

    def process_file(self, file):
        css = self.run_uncss(file)
        if css:
            css = self.inline_css(css)
            self.patch_file(file, css)
        else:
            logging.warning('File {} is skipped', file)

    def perform(self):
        for template in self.templates_path:
            self.process_file(template)
            #     self.pool.apply_async(self.process_file, args=(template,))
            # self.pool.close()
            # self.pool.join()
