import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yass",
    version="0.0.1",
    author="vee",
    install_requires=['docutils>=0.3', 'PyYAML>=5.2', 'requests>=2.22.0'],
    author_email="naeini.v@gmail.com",
    description="Yet Another Swagger Stuff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/iamv/yass",
    packages=setuptools.find_packages(),
    scripts=['bin/yass'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
