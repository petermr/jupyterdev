import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ami-pkg-petermr", # Replace with your own username
    version="0.0.1",
    author="Peter Murray-Rust",
    author_email="peter.murray.rust@googlemail.com",
    description="AMI: intelligent tools for creating scientific knowledge from documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/petermr/jupyterdev",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
