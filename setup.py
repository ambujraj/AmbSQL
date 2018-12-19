from setuptools import setup, find_packages
from os import path
with open("README.md", "r") as fh:
    long_description = fh.read()

here = path.abspath(path.dirname(__file__))

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]


setup(
    name="ambsql",
    version="1.1.1",
    author="Ambuj Raj",
    author_email="thecoderguy@outlook.com",
    description="AmbSQL is a DBMS which is approx 10x faster and the most EASY to operate on.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ambujraj/AmbSQL",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=['docs', 'download']),
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    keywords='database management system python ambsql terminal command-line',
)
