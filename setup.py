from setuptools import find_packages, setup
setup(
    name='scapy-utils',
    packages=find_packages(include=['scapy']),
    version='0.1.0',
    description='Scapy Operations',
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    author='Matheus Phelipe',
    license='MIT',
)