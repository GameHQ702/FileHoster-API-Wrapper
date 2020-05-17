# FileHoster API Wrapper

Its a simple API Wrapper for Python

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Supported / Unsupported Hoster

- [ ] Mediafire
- [x] Anonfile
- [ ] Mega.nz
- [x] Vidoza
- [x] Vivo


## Usage

```python
import main as FileHoster

vivo = FileHoster.Vivo(vivotoken)
accinfo = vivo.AccInfo()
print(accinfo)
```