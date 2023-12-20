from setuptools import setup, find_packages

from ps.version import __version__



setup(
    name = 'pulsarstellar',
    version= __version__,
    url = 'https://github.com/pulsarstellar/pulsarstellar',
    author = 'Pulsar-Stellar',
    author_email = 'lalo@pulsarstellar.ai',
    description = 'Pulsar-Stellar a Robotics & AI Library',
    long_description = 'Pulsar-Stellar is an innovative, open-source library designed for building customizable and intelligent robots.',
    packages = find_packages(),    
    install_requires = [
        'tensorflow==2.15.0',
        'opencv-python==4.8.1.78',
        'numpy==1.26.2',
    ],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)