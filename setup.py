#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup
import platform


# Read the requirements from the requirements.txt file
with open("requirements.txt") as fp:
    install_requires = fp.read().splitlines()




setup(
    name="prompt_as",
    version="0.1.0",
    description="""GPT""",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/Upsonic/prompt-as-function",
    author="Upsonic",
    author_email="onur@upsonic.co",
    license="MIT",
    packages=[
        "prompt_as",
    ],
    include_package_data=True,
    install_requires=[],
    python_requires=">= 3.9",
    zip_safe=False,

)
