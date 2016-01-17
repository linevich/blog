#!/usr/bin/env bash
POTFILE=./locales/messages.pot
LOCALES_PATH=locales/

make potfile
pybabel update --input-file $POTFILE --output-dir $LOCALES_PATH --domain messages
#pybabel init --input-file $POTFILE --output-dir $LOCALES_PATH --locale "$1" --domain messages