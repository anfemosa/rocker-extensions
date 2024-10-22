from setuptools import setup

with open("README.md", "r") as fin:
    long_description = fin.read()

setup(
    name='am_rocker',
    version='0.0.0',

    description='Extra plugins for rocker',
    long_description=long_description,
    long_description_content_type="text/markdown",

    author='Andres Montano  ',
    author_email='andres.montano@tecnalia.com',

    packages=['rocker_extensions'],
    package_data={'rocker_extensions': ['templates/*.em']},

    url="https://git.code.tecnalia.com/andres.montano/rocker-extensions/",

    install_requires=[
        'rocker',
    ],

    entry_points={
        'rocker.extensions': [
            'am_devtools = rocker_extensions.extensions:DevTools',
        ]
    },
)
