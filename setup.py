import setuptools



with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.read().splitlines()

setuptools.setup(
    name="dsnkafka",
    version="0.0.1",
    author="Anders Launer Baek-Petersen",
    author_email="anders@baekpetersen.dk",
    #packages=["src.dsnkafka"],
    packages=setuptools.find_packages(),
    package_dir={'':'src'},
    license="MIT",
    description="TODO",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    python_requires=">=3.9",
)
