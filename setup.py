from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()
    
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
    
setup(
    name='image-processing-package',
    version='0.0.1',
    author='Marcus Vinicius Werhli',
    description='Package to process images',
    long_description=page_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=requirements,
)