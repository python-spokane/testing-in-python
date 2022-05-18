---
title: "Journey to the Pythonic Peak 🗻"
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
Testing is the act of verifying that the code you write runs the way you expect it to.

---

<!-- _class: lead -->
> Code without tests is bad code. It doesn’t matter how well-written it is; it doesn’t matter how pretty or object-oriented or well-encapsulated it is. With tests, we can change the behavior of our code quickly and verifiably. Without them, we really don’t know if our code is getting better or worse.

<small>  - _Working Effectively with Legacy Code_ by Michael Feathers.</small>

---

<!-- _class: lead -->
> Code without tests is bad code. It doesn’t matter how well-written it is; it doesn’t matter how pretty or object-oriented or well-encapsulated it is. With tests, we can <mark>**change the behavior of our code quickly and verifiably**</mark>. Without them, we really don’t know if our code is getting better or worse.

<small>  - _Working Effectively with Legacy Code_ by Michael Feathers.</small>

---

# The **[Kevin Bost](https://github.com/Keboo)** Slide
  - Think about what you're testing and why
  - Naming, Naming, Naming

---

# Thinking about testing
Questions to ask yourself:
- Am I testing boiler-plate code (the framework, stdlib, etc.)?
- Am I testing implementation logic?

---

# Naming, Naming, Naming
- `UnitOfWork_StateUnderTest_ExpectedBehavior`

```python
def test_

```

- `sut = ...`
- `actual = ...`
- Arrange, Act, Assert

---

# How to write readable tests

---

## `unittest`
- writing a unit test using `unittest`
- Class style tests

---

## `pytest`
- function style tests
- writing a unit test using `pytest`
- fixtures
- pytest extensions
- marks
- CLI options
  - verbose
- debugging with VS Code

---

<style scoped>
h1 {
    font-size: 2.4rem;
}
</style>

<!-- _class: lead -->
# Thanks for coming 👋
