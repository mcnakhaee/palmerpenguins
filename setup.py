from setuptools import setup

setup(name='palmerpenguins',
      version='0.0.1',
      description="A python wrapper for palmer penguins's dataset",
      author='Muhammad Chenariyan Nakhaee',
      author_emai='mcnakhaee@gmail.com',
      packages = ['palmerpenguins'],
      install_requires=['pandas', 'seaborn', 'numpy'])
