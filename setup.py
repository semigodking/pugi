#!/usr/bin/env python

"""
setup.py file for Python wrapper of pugi
"""

from distutils.core import setup, Extension


pugi_module = Extension('_pugi',
                   sources=["pugi.i", './pugixml/src/pugixml.cpp'],
                   include_dirs=['./pugixml/src/', './pugixml/contrib/'],
                   swig_opts=['-c++']
                           )

setup (name = 'pugi',
       version = '1.8.1',
       author      = "Zhuofei Wang <semigodking@gmail.com>",
       description = """Python wrapper of pugixml.""",
       ext_modules = [pugi_module],
       #py_modules = ['pugi'],
       )
