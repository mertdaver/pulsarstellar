from setuptools import setup, find_packages


setup(
    name='Pulsar-Stellar',
    version='0.1.0',
    url='https://github.com/pulsarstellar/pulsarstellar',
    author='Lalo Blanc',
    author_email='blanc@pulsarstellar.ai',
    description='Pulsar-Stellar is an innovative, open-source framework designed for building customizable and intelligent robots.',
    packages=find_packages(),    
    install_requires=[
        'torch',
        'numpy',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License 2.0',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)