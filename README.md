# Collatz Conjecture Visualizer

## Overview

This Python script visualizes the Collatz sequence for a given positive integer. The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows: start with any positive integer `n`. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of `n`, the sequence will always reach 1.

## Installation

Before running the script, make sure you have Python installed on your system. You also need to install the required dependencies.

### Dependencies

The script requires `matplotlib` for plotting the sequence. You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

To run the script, use the command line and provide a positive integer as an argument. For example:

```bash
python3 main.py 6
```

This will generate a plot showing the Collatz sequence starting from 6.

### Script Features

- Generates the Collatz sequence for the given integer.
- Visualizes the sequence in a plot, showing each step's value.
- Provides information about the highest value in the sequence and the number of steps taken to reach 1.

### Output

Upon running the script, it will display a plot of the Collatz sequence and print the following information in the console:
- The highest value in the sequence.
- The total number of steps taken to reach 1.