from setuptools import setup, find_packages

setup(
    name='remover',
    version='0.0.1',
    description='',
    author='geekyutao',
    packages=find_packages(),
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)

