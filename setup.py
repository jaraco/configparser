import setuptools

setuptools.setup(
    use_scm_version=True,
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
)
