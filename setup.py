from distutils.core import setup


setup(
    name="pydrawer",
    packages=["pydrawer"],
    version="0.0.1",
    license="MIT",
    description="Draw curves in a super easy way!",
    author="Dylan Tintenfich",
    author_email="tintenfichdylan05@gmail.com",
    url="https://github.com/dylannalex/pydrawer",
    keywords=[
        "pydrawer",
    ],
    install_requires=["PyYAML==6.0", "turtle==0.0.1"],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
)
