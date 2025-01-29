from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'flask>=2.2',
        'requests>=2.31',
    ],
    entry_points={
        'console_scripts': [
            'my_project= my_project.main:main',
        ],
    },
)
