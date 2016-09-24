# README

This is the sources of my blog designed with bootstrap 3 and material design.

# Installation

```
git clone https://github.com/linevich/blog
cd blog
mkvirtualenv blog --python=/usr/bin/python3
pip install -r requirements.txt
mv Makefile.example Makefile
cd theme
npm install
node_modules/.bin/bower install
node_modules/.bin/grunt copy
node_modules/.bin/grunt less:production
node_modules/.bin/grunt uglify
```