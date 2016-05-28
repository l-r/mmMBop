from distutils.core import setup
from mmmbop.config import *

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name=name,
    packages=packages,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    download_url=download_url,
    keywords=keywords,
    classifiers=[],
    install_requires=required,
    entry_points={
        'console_scripts': ['mmmbop=mmmbop.cli:serve'],
    }
)
