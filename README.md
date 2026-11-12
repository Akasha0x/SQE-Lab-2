# Software Quality Engineering Labs: White-Box and Pairwise Testing

Lab work for the Software Quality Engineering course at Mirpur University of Science & Technology (MUST), covering **white-box testing**, **code coverage** and **pairwise (combinatorial) testing** in Python.

## What this repo covers
**1. White-box testing with Coverage.py**
- Tested an authentication module ([auth.py or your file name]).
- Used **Coverage.py** to measure which statements and branches the tests reached.
- Added tests for the uncovered code until coverage improved.

**2. Pairwise testing with allpairspy**
- Generated test cases that cover every pair of input values.
- Compared the number of pairwise tests with exhaustive testing: [e.g. 12 pairwise cases vs 48 exhaustive].

## Key concepts
White-box testing · Statement and branch coverage · Combinatorial testing · Test design

## Project structure
```
SQE-Lab-2/
├── [auth.py]            # code under test
├── [test_auth.py]       # unit tests
├── [pairwise.py]        # pairwise test generation
└── README.md
```

## What I learned
- How coverage reports show untested branches
- How pairwise testing reduces the number of tests while still covering all two-way combinations

## Author
**Akasha Abbasi**, Software Engineering student at MUST
GitHub: [Akasha0x](https://github.com/Akasha0x)
