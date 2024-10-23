from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='rocker-extensions',
    version='0.0.0',

    description='Extra plugins for rocker',
    long_description=long_description,
    long_description_content_type="text/markdown",

    author='Andres Montano',
    author_email='andres.montano@tecnalia.com',

    packages=['rocker_extensions'],
    package_data={'rocker_extensions': ['templates/*.em']},

    url="https://git.code.tecnalia.com/andres.montano/rocker-extensions/",

    install_requires=[
        'rocker',
    ],

    entry_points={
        'rocker.extensions': [
            'am_devtools = rocker_extensions.dev_tools:DevTools',
            'am_rostools = rocker_extensions.extensions:RosTools',
        ]
    },
)
