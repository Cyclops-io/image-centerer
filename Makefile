init:
	pip install -r requirements.txt
#test:
#	python3 -m nose
#test-coverage:
#	python3 -m nose --with-coverage --cover-erase --cover-html-dir=./coverage-html --cover-html --cover-package=upgradesdowngrades
clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf
