from setuptools import setup
import log4py

setup(
    name='Log4py',
    version=log4py.__version__,
    description='A simple python logging package',
    url='https://github.com/PaddeCraft/Log4py',
    author='PaddeCraft',
    license='BSD 2-clause',
    packages=['log4py'],
    install_requires=['rich'],

    classifiers=[
        'Programming Language :: Python :: 3'
    ],
)
