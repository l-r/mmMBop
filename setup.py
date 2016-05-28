from setuptools import setup
from mmmbop.config import *

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
    install_requires=[
        "docopt==0.6.2",
        "Flask==0.10.1",
        "Flask-Cors==2.1.2",
        "itsdangerous==0.24",
        "Jinja2==2.8",
        "MarkupSafe==0.23",
        "six==1.10.0",
        "Werkzeug==0.11.10"
    ],
    entry_points={
        'console_scripts': ['mmmbop=mmmbop.cli:serve'],
    }
)
