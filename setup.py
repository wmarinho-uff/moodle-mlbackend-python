# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Version read from file.
version_file = open(os.path.join(here, 'moodlemlbackend', 'VERSION'))
version = version_file.read().strip()

setup(
    name='moodlemlbackend',

    version=version,

    description='Python machine learning backend used by mlbackend_python Moodle plugin',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/moodlehq/moodle-mlbackend-python',

    # Author details
    author='Moodle HQ',
    author_email='integration@moodle.com',

    # Choose your license
    license='GPLv3',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Education',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='moodle machine learning numpy scikit-learn tensorflow',

    packages=find_packages(),
    package_data={
        'moodlemlbackend': ['VERSION']
    },
    install_requires=[
        'matplotlib>=1.5.0,<1.6',
        'numpy>=1.11.0,<1.12',
        'scikit-learn>=0.17.0,<0.18',
        'scipy>=0.17.0,<0.18',
        'tensorflow>=1.0.0,<1.1',
    ],
)
