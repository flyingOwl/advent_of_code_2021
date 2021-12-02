# Advent of Code 2021

This repository contains the python code I used to solve the Advent of Code puzzles.

The python file for each day contains the solution for both parts. The scripts will only output two lines: the answer for part 1 and for part 2.

## Makefile and .session

The Makefile can do two things:

- download the input files
- run the python scripts

To download the input files, you need to provide your Cookie in the `.session` file. You can find your session key with the developer tools of your browser.

```
$ cat .session
Cookie: session=abc123abc123...abc123;
```

The Makefile will download the input files as `input_2021_[day]`. To run automatically download the input and run the script for a given day, just call:

```
$ make 2021_[day]
```
