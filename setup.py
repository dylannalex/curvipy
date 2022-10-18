from distutils.core import setup


setup(
    name="curvipy",
    packages=["curvipy"],
    version="1.0.0",
    license="MIT",
    description="The Python library for making math animations in a few lines of code.",
    author="Dylan Tintenfich",
    author_email="tintenfichdylan05@gmail.com",
    url="https://github.com/dylannalex/curvipy",
    keywords=["curves", "linear-algebra", "mathematics", "animations"],
    install_requires=["PyYAML==6.0", "turtle==0.0.1"],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)
