#!/usr/bin/python
# -*- coding: utf-8; -*-

from setuptools import setup, find_packages


setup(
    name               = "netl2api.lib",
    namespace_packages = ["netl2api"],
    version            = "1.5.15",
    packages           = ["netl2api", "netl2api.lib"],
    zip_safe           = False,
    install_requires   = ["pyOpenSSL", "redis"],

    author       = "Eduardo S. Scarpellini",
    author_email = "eduardo.scarpellini@locaweb.com.br",
    description  = "Python generic API (vendor agnostic) for network/L2 operations",
    keywords     = "python generic vendor agnostic switch l2 api",
    url          = "https://github.com/locaweb/netl2api",
)
