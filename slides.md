---
title: "🧪 Testing in Python 🐍"
marp: true
html: true
theme: gaia

---
<style>
p, pre {
    margin-top: 8px !important;
}
</style>
<style scoped>
h1 {
    font-size: 2.4rem;
}
h2 {
    font-size: 2rem;
}
</style>

<!-- _class: lead -->
# 🧪 Testing in Python 🐍

_May 17, 2022_

Joe Riddle

---

<!-- _class: lead -->
## What is "testing"?

<!-- Ask audience "What does 'testing' mean to you?" -->

---

<!-- _class: lead -->
Testing is the <mark>act of verifying that the code you write runs the way you expect it to.</mark>

---

<!-- _class: lead -->
> Code without tests is bad code. It doesn’t matter how well-written it is; it doesn’t matter how pretty or object-oriented or well-encapsulated it is. With tests, we can change the behavior of our code quickly and verifiably. Without them, we really don’t know if our code is getting better or worse.

<small>  - _Working Effectively with Legacy Code_ by Michael Feathers.</small>

---

<!-- _class: lead -->
> Code without tests is bad code. It doesn’t matter how well-written it is; it doesn’t matter how pretty or object-oriented or well-encapsulated it is. With tests, we can <mark>**change the behavior of our code quickly and verifiably**</mark>. Without them, we really don’t know if our code is getting better or worse.

<small>  - _Working Effectively with Legacy Code_ by Michael Feathers.</small>

---

<style scoped>
img {
  border-radius: 1000000px;
}
</style>

<!-- _class: lead -->
# [https://spokanepython.com/](https://spokanepython.com/) 

![width:200px height:200px](https://spokanepython.com/img/stan.jpg)

---

# The **[Kevin Bost](https://github.com/Keboo)** Slide
  - Think about what you're testing and why
  - Naming, Naming, Naming

---

# Thinking about Testing
Questions to ask yourself:
- Am I testing boiler-plate code (the framework, stdlib, etc.)?
- Am I testing implementation logic?

<!-- Ask, "What are some other questions to ask yourself when writing tests?" -->

---

# Naming, Naming, Naming
- `UnitOfWork_StateUnderTest_ExpectedBehavior`
- `sut = ...`
- `actual = ...`
- Arrange, Act, Assert

---

# unittest
- Class style tests
- Writing a unit test using `unittest`:
```python
import unittest

class TestAdd(unittest.TestCase):
  def test_add():
    self.assertEqual(2 + 2, 4)

```
```bash
$ python -m unittest
```

---

# pytest
- Function style tests
- fixtures
- [plugins](https://docs.pytest.org/en/7.1.x/reference/plugin_list.html#plugin-list)
- marks
- CLI options
- debugging with VS Code

---

# pytest
- writing a unit test using `pytest`:
```python
import pytest

def test_add():
    assert 2 + 2 == 4

```

```bash
$ python -m pytest
```

---

<style scoped>
h1 {
    font-size: 2.4rem;
}
</style>

<!-- _class: lead -->
# Thanks for coming 👋
