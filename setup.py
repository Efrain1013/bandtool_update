from setuptools import setup, find_packages

setup(
    name='bandtool_update',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'bandtool_update=bandtool_update.main:main',
        ],
    },
)

