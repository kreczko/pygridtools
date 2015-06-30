try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config{
    name="pygridtools",
    packages=['pygridtools'],
    version="0.0.1",
    description="A set of useful tools for the science computing grid",
    author='Luke Kreczko',
    author_email='lkreczko@gmail.com',
    url='https://github.com/kreczko/pygridtools',
    keywords=['grid'],
    include_package_data=True,
    entry_points={
        'console_scripts': ['pygridtools = pygridtools.__main__:main']
        },
    zip_safe=False,
}

setup(**config)
