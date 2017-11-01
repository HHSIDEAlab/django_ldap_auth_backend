import os
from setuptools import setup

__author__ = "Alan Viars"

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name="django_ldap_auth_backend",
      version="0.1",
      description="LDAP Authentication Backend",
      long_description="""A Django backend for LDAP.""",
      author="Alan Viars",
      url="https://github.com/HHSIDEAlab/django_ldap_auth_backend",
      download_url="https://github.com/HHSIDEAlab/django_ldap_auth_backend"
                   "tarball/master",
      install_requires=['django', 'pyldap'],
      packages=['django_ldap.backends', ],
      include_package_data=True,
      )
