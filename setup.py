#! /usr/bin/python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bbb-wss-proxy",
    version="0.0.1",
    author="Brent Baccala",
    author_email="cosine@freesoft.org",
    description="WebSocket proxy for Big Blue Button users",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BrentBaccala/bbb-wss-proxy",
    packages=setuptools.find_packages(),
    install_requires=[
        'websockify'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
        "License :: Freely Distributable",
    ],
)
