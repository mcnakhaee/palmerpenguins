from setuptools import setup
import os
import numpy
import platform
setup(name='palmerpenguins',
      version='0.1.1',
      url="https://github.com/mcnakhaee/palmerpenguins",
      description="A python wrapper for palmer penguins's dataset",
      long_description=open('README.md').read(),
      author='Muhammad Chenariyan Nakhaee',
      author_emai='mcnakhaee@gmail.com',
      packages = ['palmerpenguins'],
      install_requires=['pandas', 'seaborn', 'numpy'],
      include_package_data=True,
      package_data={'': ['data/*.csv']},
      )
