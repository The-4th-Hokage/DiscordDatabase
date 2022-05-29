# Always prefer setuptools over distutils
# To use a consistent encoding
import re
from codecs import open
from os import path

from setuptools import setup

version = ''
with open('DiscordDatabase/__init__.py') as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

packages = [
    "DiscordDatabase",
]


# Get the long description from the README file
with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="DiscordDatabase",
    version=version,
    description="CRUD database for discord bots, using discord text channels to store data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ankushKun/DiscordDatabase",
    author="Ankush Singh",
    author_email="ankush4singh@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    extras_require = {
        'speed':  ["orjson"]
    },
    include_package_data=True,
    package_data={"fluxpoint": ["py.typed"]},
    packages=packages
)
