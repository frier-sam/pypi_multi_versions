from setuptools import setup, find_packages

setup(
    name='pypi_multi_versions',
    version='0.2.0',
    author='sam-iau',
    author_email='shop2local@gmail.com',
    description='Manage multiple versions of PyPI packages',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pypi_multi_versions',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your package might have
    ],
    entry_points={
        'console_scripts': [
            'pypi-multi-versions=pypi_multi_versions.cli:main',
        ],
    },
    classifiers=[
        # Choose your audience and license, see: https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
