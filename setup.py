from setuptools import setup, find_packages

from ps.version import __version__



setup(
    name = 'Pulsar-Stellar',
    version= __version__,
    url = 'https://github.com/pulsarstellar/pulsarstellar',
    author = 'Lalo Blanc',
    author_email = 'blanc@pulsarstellar.ai',
    description = 'Pulsar-Stellar a Robotics & AI Library',
    long_description = 'Pulsar-Stellar is an innovative, open-source library designed for building customizable and intelligent robots.',
    packages = find_packages(),    
    install_requires = [
        'tensorflow==2.15.0',
        'numpy==1.26.2',
    ],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License 2.0',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)