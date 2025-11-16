"""
setup.py

from setuptools import setup, find_packages

setup(
    name='algoritmia',
    version='1.0.0',
    description='Intérprete del lenguaje de programación musical Algoritmia',
    author='Tu Nombre',
    author_email='tu@email.com',
    python_requires='>=3.8',
    install_requires=[
        'antlr4-python3-runtime==4.13.1',
    ],
    entry_points={
        'console_scripts': [
            'algoritmia=algoritmia:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
"""
