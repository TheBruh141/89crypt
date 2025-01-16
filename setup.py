from setuptools import setup, find_packages

setup(
    name="ENcrypt",
    version="1.0.0",
    description="A small library written for TUBITAK 2204-a for encryption",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Burak Güngör",
    author_email="burak.gungor@enka.k12.tr",
    url="https://github.com/TheBruh141/89crypt",  # Repository URL
    license="GNU GPLv3",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",  # Specify the minimum Python version
)
