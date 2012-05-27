from os.path import dirname, join

from setuptools import setup, find_packages



version = '0.1.1'

setup(
    name = 'singlepagelogs',
    version = version,
    description = "Django Middleware for retrieving log information stored in HTTP headers",
    long_description = open(join(dirname(__file__), 'README.md')).read(),
    classifiers = [
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"],
    keywords = 'django middleware logging http headers singlepage',
    author = 'Mihai Oprea',
    author_email = 'mihai@mihaioprea.com',
    url = 'https://github.com/mishu-/django-singlepage-logs',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = ['setuptools']
)
