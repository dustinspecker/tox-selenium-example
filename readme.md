# tox-selenium-example

## Mac Setup

1. `brew install python@2` to install `python` and `pip`
1. `pip install --upgrade pip`
1. `pip install tox`
1. `brew install geckodriver`
1. `brew cask install firefox`

## Ubuntu Setup

1. `sudo apt install python`
1. `sudo apt install python-pip`
1. `sudo apt install python-tox`
1. `wget https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz`
1. `tar -xvzf geckodriver-v0.20.1-linux64.tar.gz`
1. `sudo mv geckodriver /usr/local/bin`

## Usage

- Use `tox` to run the single Selenium test in Firefox
- Use `tox -e headless` to run the single Selenium test in headless Firefox
