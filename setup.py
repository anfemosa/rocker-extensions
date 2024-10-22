from setuptools import setup

with open("README.md", "r") as fin:
    long_description = fin.read()

setup(
    name='rocker-extensions',
    version='0.1.0',
    packages=['rocker_extensions'],
    package_data={'rocker_extensions': ['templates/*.em']},
    author='Andres Montano  ',
    author_email='andres.montano@tecnalia.com',
    description='Extra plugins for rocker',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://git.code.tecnalia.com/andres.montano/rocker-extensions/",
    license='Apache 2.0',
    install_requires=[
        'rocker',
    ],
    entry_points={
        'rocker.extensions': [
            'am_devtools = rocker_extensions.extensions:DevTools',
        ]
    }
)
