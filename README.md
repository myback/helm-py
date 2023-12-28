# helm-wrap

Python wrapper for Helm binary

### Usage
```py
from helm_wrap import helm

h = helm.Helm(o='json')
lst = h.list()
print(lst.json)
```
