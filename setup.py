#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="hungman",
    version="0.0.0",
    author="Sergei Solovev",
    author_email="sergeisoly@gmail.com",
    url="https://github.com/sergeisoly/hungman",
    license="MIT",
    packages=[
        "hungman",
    ],
    install_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
