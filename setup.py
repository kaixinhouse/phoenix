# _*_ coding:utf-8 _*_

from setuptools import setup

project = "phoniex"


setup(
    name = phoniex,
    version = "0.1",
    description = "phoniex is a SNS website base on Flash",
    author = "KBoard",
    author_email = "kaixinhouse@gmail.com",
    packages = ["phoniex"],
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        "Flash",
	"Flash-SQLAlchemy",
	"mysql-python",
    ]
)
