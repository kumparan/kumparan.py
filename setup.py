from setuptools import setup

# Package details
setup(
    name="kumparan",
    version="0.0.2",
    author="Bayu Aldi Yansyah",
    author_email="bayualdiyansyah@gmail.com",
    url="https://github.com/kumparan/kumparan.py",
    description="Kumparan's Python Package",
    long_description=open("README.rst", "r").read(),
    license="BSD 3-Clause License",
    packages=[
        "kumparan"
    ],
    install_requires=[
        "ujson==1.35",
        "google-cloud==0.32.0"
    ],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6"
    ]
)
