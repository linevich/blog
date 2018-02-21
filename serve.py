import os
from subprocess import CalledProcessError, check_output

from livereload import Server

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

STYLES_PATH = os.path.join(BASE_DIR, 'theme/assets/scss/')
TEMPLATES_PATH = os.path.join(BASE_DIR, 'theme/templates/*')
ARTICLES_PATH = os.path.join(BASE_DIR, 'content/')
BUILD_PATH = os.path.join(BASE_DIR, 'theme/static')
OUTPUT = os.path.join(BASE_DIR, 'output/')

SASS_COMPILER = '/usr/local/bin/sass'
SASS_ARGS = ['--no-cache', '--update']
SASS_SOURCE = STYLES_PATH
SASS_TARGET = os.path.join(BUILD_PATH, 'css')

server = Server()


def call_debug(args):
    try:
        print(check_output(args).decode('utf-8'))
    except CalledProcessError as e:
        print(e)


def build_scss():
    call_debug([SASS_COMPILER, *SASS_ARGS, '{}:{}'.format(SASS_SOURCE, SASS_TARGET)])
    call_debug([SASS_COMPILER, *SASS_ARGS, '{}:{}'.format(SASS_SOURCE, os.path.join(OUTPUT, 'theme/css'))])
    # call_debug(['cp', os.path.join(SASS_TARGET, './*'), os.path.join(OUTPUT, 'theme/')])
    # # call_debug(['cp', '{}.map'.format(SASS_TARGET), os.path.join(OUTPUT, 'theme/*')])


def build_pelican():
    call_debug(['make', 'html'])


server.watch(STYLES_PATH, build_scss)
server.watch(ARTICLES_PATH, build_pelican)
server.watch(TEMPLATES_PATH, build_pelican)
server.watch(os.path.join(BUILD_PATH, '/**'))
# server.watch(os.path.join(OUTPUT, '*/*'))
server.watch(os.path.join(OUTPUT, '/**.css'))

server.serve(root='output/', open_url=True, debug=True)
