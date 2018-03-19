# Kumparan's Python Package

`kumparan` is a collection of commonly-used Python modules in Kumparan.

The Python package is available at [pypi](https://pypi.org/project/kumparan/)
and you can install it using the following command:

    pip install kumparan

The documentation is available [here](https://kumparan.github.io/kumparan.py).


### Overview

At Kumparan, we use python mainly to solve data engineering and data 
science problems. From our tracker services that can digest tracking events 
in less than 10ms to our machine learning services are all written in Python.

One of the challenge that we face as a team is the source code management, 
with `kumparan` package it allows us to:

1. **Re-use our existing implementation easily**.
   This whill helps our engineers speed up the development process
   and not to re-invent the wheel.
2. **Centralize a shared modules management**.
   Centralized shared modules means that there is only one source of
   the truth. We can update & improve the shared module once and it 
   will affect to all services that use it.


### Semantic Versioning
We follow [semantic versioning](https://semver.org/) for a release procedure.
When there is a breaking changes in the API, we will make sure the old code
still run in a period of time. This will prevent breaking build in production
and a give a time to the engineer to update their services.

