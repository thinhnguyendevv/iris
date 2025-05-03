from setuptools import setup, find_packages

setup(
    name='iris_classifier',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
    ],
    author='Your Name',
    description='A simple classifier for the Iris dataset using RandomForest',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/iris_classifier',
)
