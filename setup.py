import sys
import setuptools

setuptools.setup(
    # enable `import configparser` for Python 2
    py_modules=['configparser'] if sys.version_info < (3,) else [],
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
)
