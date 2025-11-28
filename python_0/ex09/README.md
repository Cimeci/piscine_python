# ft_package

A simple Python package for counting elements in lists.

## Bash Command pip

### Installation
```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
# or
pip install ./dist/ft_package-0.0.1.tar.gz
```

### Unstallation
```bash
pip uninstall ft-package -y
```

### Show
```bash
pip show -v ft_package
```

## Usage
```python
from ft_package import count_in_list

result = count_in_list(["toto", "tata", "toto"], "toto")
print(result)  # Output: 2
```

## License

MIT