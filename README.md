# Testing in Python

“Code without tests is bad code. It doesn’t matter how well-written it is; it doesn’t matter how pretty or object-oriented or well-encapsulated it is. With tests, we can change the behavior of our code quickly and verifiably. Without them, we really don’t know if our code is getting better or worse.” - _Working Effectively with Legacy Code_ by Michael Feathers.</small>

If code without tests is bad code, then the first step to writing good code is learning to write tests. Join the Spokane Python User Group as we learn how to craft tests for our code!

## Resources
- [unittest](https://docs.python.org/3/library/unittest.html)
- [pytest](https://docs.pytest.org/)
- [Star Wars API](https://swapi.dev/documentation)
- [Kevin Bost](https://github.com/Keboo)
- [marp](https://marp.app/)

## Development

### Getting Started
**Linux**
```bash
python -m venv .venv
source .venv/bin/python
pip install -r requirements.txt
```

**Windows**
```powershell
python -m venv .venv
.venv/Scripts/activate.ps1
pip install -r requirements.txt
```

### Generate Slides
```bash
# See here to install marp: https://github.com/marp-team/marp-cli
marp --watch --html slides.md
```
