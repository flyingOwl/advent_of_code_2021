SCRIPTS = $(wildcard *.py)
INPUT = $(patsubst %.py, input_%, $(SCRIPTS))
url = $(shell echo $@ | sed -e "s/input_\([0-9]\+\)_0*\([0-9]\+\)/\1\/day\/\2\/input/g")

input: $(INPUT)

input_%: .session
	curl -H @.session https://adventofcode.com/$(url) > $@

2021_%: input_2021_%
	python $@.py $^
