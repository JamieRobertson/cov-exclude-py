import os.path

from setuptools import setup, find_packages

HERE = os.path.dirname(__file__)


def read_version():
    about_data = {}

    with open(os.path.join(HERE, 'covexclude/__about__.py')) as fp:
        exec(fp.read(), about_data)

    return about_data['__version__']


setup(
    name='cov-exclude',
    version=read_version(),

    author='Magnus Hallin',
    author_email='mhallin@fastmail.com',

    license='MIT',

    packages=find_packages(exclude=['deps']),

    entry_points={
        'pytest11': [
            'cov-exclude = covexclude.plugin',
        ],
    },

    install_requires=[
        'coverage~=4.0.0',
    ],

    extras_require={
        'dev': [
            'pytest~=2.8.0',
        ],
    },
)
