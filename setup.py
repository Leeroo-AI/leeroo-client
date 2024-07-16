from setuptools import setup, find_packages

setup(
    name="leeroo-client",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author="Leeroo",
    author_email="arshad@leeroo.com",
    description="A client library for Leeroo Workflow Management",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Leeroo-AI/leeroo-client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)