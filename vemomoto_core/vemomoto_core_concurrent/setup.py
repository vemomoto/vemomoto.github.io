'''
Setup of the package vemomoto_core.vemomoto_core_concurrent
'''

from setuptools import setup


PATHADD = 'vemomoto_core/concurrent/'
PACKAGEADD = PATHADD.replace("/", ".")

setup(
    name="vemomoto_core_concurrent",
    version="0.9.0.a1",
    install_requires=['numpy', 'sharedmem'], 
    packages=[PACKAGEADD[:-1]],
    python_requires='>=3.6',

    # metadata to display on PyPI
    author="Samuel M. Fischer",
    license='LGPL-3.0',
    description="Methods to ease parallelization of code", 
    keywords="parallel, shared memory, multiprocessing, concurrency", 
    url="https://github.com/vemomoto/vemomoto",
    project_urls={
        "Bug Tracker": "https://github.com/vemomoto/vemomoto",
        "Documentation": "https://vemomoto.github.io/vemomoto_core/vemomoto_core.concurrent",
        "Source Code": "https://github.com/vemomoto/vemomoto/tree/master/vemomoto_core/vemomoto_core_concurrent",
    },
    classifiers=[
        'License :: OSI Approved :: LGPL-3.0',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    ],
)
