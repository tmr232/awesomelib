import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='awesomelib',
    version='0.1.0',
    packages=['awesome'],
    url='https://github.com/tmr232/awesomelib',
    license='MIT',
    author='Tamir Bahar',
    author_email='',
    description='Awesome Python Utils.',
    long_description=(read('README.rst')),
)
