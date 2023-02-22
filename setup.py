from setuptools import setup
import sys

setup(
    name='michalcider',
    version='0.1.19',
    author='Alex Holehouse',
    author_email='alex.holehouse@wustl.edu',
    packages=['michalcider', 'michalcider.tests', 'michalcider.backend', 'michalcider.backend.data'],
    scripts=[],
    url='http://pappulab.github.io/localCIDER/',
    license='LICENSE.txt',
    description='Tools for calculating sequence properties of disordered proteins [from the Pappu Lab at Washington University in St. Louis]',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy",
        "matplotlib",
        "scipy",
        "BioPython",
        "nardini"
    ],
    test_suite='michalcider.tests.suite')
#    **extras)
