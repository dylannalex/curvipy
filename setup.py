from distutils.core import setup


setup(
    name="curvipy",
    packages=["curvipy"],
    version="0.1.1",
    license="MIT",
    description="The Python package for visualizing mathematical functions, curves and linear transformations with animations.",
    author="Dylan Tintenfich",
    author_email="tintenfichdylan05@gmail.com",
    url="https://github.com/dylannalex/curvipy",
    keywords=["calculus", "linear-algebra", "matrix", "mathematics"],
    install_requires=["PyYAML==6.0", "turtle==0.0.1"],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)
