# -*- coding: utf-8 -*-
"""Setup module for flask taxonomy."""
import os

from setuptools import setup

readme = open('README.rst').read()

install_requires = [
    'marshmallow',
    'flask'
]

tests_require = [
    'invenio[base,metadata,sqlite,elasticsearch7]',
    'pytest>=4.6.3',
    'jsonschema',
    'pydocstyle',
    'isort',
    'check-manifest',
    'pytest-cov',
    'pytest-pep8',
    'oarepo-mapping-includes'
]

extras_require = {
    'tests': [
        *tests_require,
        ],
    'tests-es7': [
        *tests_require,
        ],
}

setup_requires = [
    'pytest-runner>=2.7',
]

g = {}
with open(os.path.join('oarepo_multilingual', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name="oarepo_multilingual",
    version=version,
    url="https://github.com/oarepo/oarepo-multilingual",
    license="MIT",
    author="Miroslav Simek",
    author_email="miroslav.simek@vscht.cz",
    description="Multilingual support for OARepo",
    zip_safe=False,
    packages=['oarepo_multilingual'],
    entry_points={
        'oarepo_mapping_handlers': [
            'multilingual=oarepo_multilingual.mapping.mapping_handler:handler'
        ],
        'invenio_jsonschemas.schemas': [
            'oarepo_multilingual = oarepo_multilingual.jsonschemas'
        ],
    },
    include_package_data=True,
    setup_requires=setup_requires,
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
    ],
)
