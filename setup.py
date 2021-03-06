import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="food2vec",
    version="0.0.3",
    author="Joshua D'Arcy",
    author_email="joshuadrc@gmail.com",
    description="Tools for semantic nutrition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages = ["food2vec"],
    install_requires =[
        "numpy",
        "pandas",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
)