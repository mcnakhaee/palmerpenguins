from setuptools import setup

setup(
    name="palmerpenguins",
    version="0.1.4",
    url="https://github.com/mcnakhaee/palmerpenguins",
    description="A python package for the palmer penguins dataset ",
    long_description=open("DESCRIPTION.rst").read(),
    author="Muhammad Chenariyan Nakhaee",
    author_emai="mcnakhaee@gmail.com",
    packages=["palmerpenguins"],
    install_requires=["pandas", "numpy"],
    include_package_data=True,
    package_data={"": ["data/*.csv"]},
)
