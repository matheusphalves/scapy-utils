from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='scapy4dummy',
   version='1.0',
   description='Networking operations using Scapy Framework',
   license="MIT",
   long_description=long_description,
   author='Matheus Phelipe',
   author_email='',
   url="",
   packages=['scpy4dummy'],
   install_requires=['scapy']
)