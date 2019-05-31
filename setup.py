#!/usr/bin/env python

import os
from setuptools import setup, find_packages

REQUIREMENTS = [line.strip() for line in
                open(os.path.join("requirements", "requirements.txt")).readlines()]
setup(
    name='diff_cover',
    version='2.0.1',
    author='Matt Bachmann',
    url='https://github.com/Bachmann1234/diff-cover',
    test_suite='nose.collector',
    description='Automatically find diff lines that need test coverage.',
    license='Apache 2.0',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: Implementation :: CPython',
                 'Programming Language :: Python :: Implementation :: PyPy',
                 'Topic :: Software Development :: Testing',
                 'Topic :: Software Development :: Quality Assurance'],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={'diff_cover': ['templates/*.txt', 'templates/*.html', 'templates/*.css']},
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': ['diff-cover = diff_cover.diff_cover_tool:main',
                            'diff-quality = diff_cover.diff_quality_tool:main']
    }
)
