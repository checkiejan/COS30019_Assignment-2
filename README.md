# COS30019 - Assignment 2 - Inference Engine

Welcome to the GitHub repository for the COS30019 Inference Engines assignment. This assignment focuses on creating an inference engine that supports backward chaining, forward chaining, truth table, and WalkSAT algorithms. The inference engine is capable of handling both horn and generic clauses, with backward and forward chaining specifically designed for horn clauses.

## Table of Contents
- [Introduction](#introduction)
- [Algorithms](#algorithms)
- [Automated Test Cases](#automated-test-cases)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Inference engines play a vital role in automated reasoning and logical deduction. This assignment aims to implement four different inference algorithms: backward chaining, forward chaining, truth table, and WalkSAT. The backward and forward chaining algorithms are limited to handling horn clauses, while truth table and WalkSAT can handle both horn and generic clauses.

## Algorithms
The repository contains separate files for each inference algorithm implemented as a class. The following algorithms are included:

1. `BC.py`: Implements the backward chaining algorithm for horn clauses.
2. `FC.py`: Implements the forward chaining algorithm for horn clauses.
3. `TT.py`: Implements the truth table algorithm for both horn and generic clauses.
4. `WSAT.py`: Implements the WalkSAT algorithm for both horn and generic clauses.

Each class provides the necessary methods and functionality to perform the corresponding inference algorithm.

## Automated Test Cases
The repository includes an automated test case generator `testGenerator.py` that tests all the implemented algorithms. The test generator creates test cases for both horn and generic clauses, unlike backward and forward chaining which only support horn clauses. To run the automated test cases, execute the `testGenerator.py` file. If any test case fails, the program will stop and print the corresponding knowledge base and query to the `error.txt` file.

## Usage
To run the inference engine with a specific algorithm and input file, use the following syntax:
`python iengine.py <method> <filename>`

- `<method>`: Specifies the algorithm to use (`backward`, `forward`, `truth_table`, or `walksat`).
- `<filename>`: Specifies the name of the text file containing the knowledge base and query to determine if the knowledge base entails the query.

Make sure to have Python installed on your system before running the inference engine.

## Contributing
Contributions to the repository are welcome! If you have any improvements, bug fixes, or additional features to add, feel free to open an issue or submit a pull request on the GitHub repository.

## License
The code in this repository is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code according to the terms of the license.

---

Thank you for your interest in the COS30019 Inference Engines assignment. We hope you find the implementation and test cases informative and helpful. If you have any further questions or inquiries, please feel free to reach out.

