from setuptools import find_packages,setup

setup(
    name='ML-project',
    version='0.0.1',
    author='Anuj Patel',
    author_email='anujpatel997780@gmail.com',
    packages=find_packages(where='src'),
    install_requires=['pandas','numpy','seaborn']
    
)