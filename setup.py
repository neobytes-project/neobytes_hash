#!/usr/bin/env python3

# Copyright (C) 2019 The Xaya developers
# Copyright (C) 2023 The Neobytes developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from setuptools import setup, Extension

neoscrypt_module = Extension('neoscrypt',
                               sources = ['neoscryptmodule.c',
                                          'neoscrypt.c'],
                               include_dirs=['.'])

setup (name = 'neobytes_hash',
       version = '1.0.3',
       license = 'MIT',
       description = 'Bindings for the NeoScrypt proof-of-work algorithm',
       author = 'Autonomous Worlds Ltd',
       author_email = 'info@autonomousworlds.com',
       url = 'https://github.com/neobytes-project/neobytes_hash',
       ext_modules = [neoscrypt_module])
