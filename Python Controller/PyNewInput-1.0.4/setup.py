import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyNewInput",
    version="1.0.4",
    author="Franco Valois",
    author_email="franco@delucca.pro.br",
    description="Python mouse and keyboard input automation for Windows, just a little patch of Direct Input.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Franko12345/PyNewInput",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.4',
)