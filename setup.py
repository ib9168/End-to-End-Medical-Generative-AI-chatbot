#Setup of the project as local package
from setuptools import setup,find_packages

setup(
    name='Generative AI Project',#so that its in the terminal list
    version='0.0.0',
    author='Irin Boksh',
    author_email='irinboksh@gmail.com',
    packages=find_packages(),#it will find the init file
    install_requires=[]
)