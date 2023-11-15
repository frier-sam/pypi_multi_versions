Manage and use multiple versions of PyPI packages in your Python projects.

## Installation

Install `pypi_multi_versions` using pip:

```
pip install pypi_multi_versions
``````

# Usage


### Python Interface

Install a Specific Version of a python  Package in a directory


```
from pypi_multi_versions.installer import install_version

install_version('scikit-learn', '0.24.1', './my_packages')
```


Import a Specific Version of a Package


```
from pypi_multi_versions.importer import import_helper

with import_helper('scikit-learn', '0.24.1', './my_packages'):
    import sklearn
print(sklearn.__version__)  # Should print '0.24.1'

```

import dependecy that staifies with other package
```
from pypi_multi_versions.importer import import_helper

with import_helper('scikit-learn', '0.24.1', './my_packages'):
    import numpy
print(numpy.__version__)  # Should be version compatable with scikit-learn==0.24.1

```


### CLI Commands

Install a Specific Version of a Package

```
pypi-multi-versions install --package <package_name> --version <version_number> --path <target_path>
```
Example:
```
pypi-multi-versions install --package scikit-learn --version 0.24.1 --path ./my_packages
```


## Development

Clone the repository and install dependencies:

```
git clone https://github.com/frier-sam/pypi_multi_versions.git
cd pypi_multi_versions
pip install -r requirements.txt
```
## Contributing

Contributions are welcome! Please read our Contributing Guide for details on our code of conduct, and the process for submitting pull requests.

License
This project is licensed under the MIT License.

