test:
	py.test .

clean: clean-test clean-pyc

clean-test:
	find . -name '.hypothesis' -exec rm -fr {} +
	find . -name '.cache' -exec rm -fr {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

# may need
# export PYTHONPATH="path pip is installing things to"
# export PATH="path pip installs bin, near above":$PATH
# sudo apt-get install python3 python3-pip
# easiest:
# python3-pytest python3-hypothesis
# but the latter package is not always available
#
# can also switch to more verbose unittest
install-requirements:
	pip3 install -r requirements.txt
