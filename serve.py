import os

from livereload import Server, shell

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

STYLES_PATH = os.path.join(BASE_DIR, 'theme/assets/scss/')
TEMPLATES_PATH = os.path.join(BASE_DIR, 'theme/templates/')
ARTICLES_PATH = os.path.join(BASE_DIR, 'content/')
BUILD_PATH = os.path.join(BASE_DIR, 'theme/build')

SASS_COMPILER = '/usr/local/bin/sass'
SASS_ARGS = '--no-cache'
SASS_SOURCE = os.path.join(STYLES_PATH, 'index.scss')
SASS_TARGET = os.path.join(BUILD_PATH, 'style.css')

server = Server()

server.watch(STYLES_PATH, shell('{} {} {} {}'.format(SASS_COMPILER, SASS_ARGS, SASS_SOURCE, SASS_TARGET)))
server.watch(ARTICLES_PATH, shell('make html', cwd=BASE_DIR))
server.watch(TEMPLATES_PATH)
server.watch(BUILD_PATH)


server.serve(open_url=True)
