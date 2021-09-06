- [AbBOT](#abbot)
  * [Discord Server](#discord-server)
  * [FAQ](#faq)
  * [Overview](#overview)
    + [Files](#files)
  * [How to use the project](#how-to-use-the-project)
    + [Install Git if you dont already have it installed](#install-git-if-you-dont-already-have-it-installed)
    + [Clone the repo](#clone-the-repo)
    + [Windows](#windows)
      - [Running the program](#running-the-program)
    + [Linux](#linux)
      - [Running the program](#running-the-program-1)
    + [macOS](#macos)
      - [Running the program](#running-the-program-2)
    + [Docker Compose](#docker-compose)
      - [Setting up Your Machine](#setting-up-your-machine)
    + [Building the Container](#building-the-container)
    + [Running the Container](#running-the-container)
    + [Docker Container (without docker-compose)](#docker-container--without-docker-compose-)
      - [Setting up Your Machine](#setting-up-your-machine-1)
      - [Building the container](#building-the-container)
      - [Running the Program](#running-the-program)
  * [How it looks in action](#how-it-looks-in-action)
    + [Generating text dynamically](#generating-text-dynamically)
  * [Usage](#usage)
  * [Using a Virtual Environment](#using-a-virtual-environment)
    + [Setup for Linux and MacOS](#setup-for-linux-and-macos)
    + [Setup for Windows](#setup-for-windows)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# AbBOT

Credit to SeanDaBlack for the basis of the script.

## Discord Server

https://discord.gg/PrAWWCCpDg

## FAQ

If you have a question, before dropping into the Discord, check out our [FAQ page](https://github.com/SeanDaBlack/AbBOT/blob/main/FAQ.md) and see if your question has already been answered.

## Overview

### Files

- `main.py` is the entrypoint for the program.
- `bot/server.py` creates a local web server that serves up a reCaptcha checkbox and passes the reCaptcha token to the `forms.py` file.
- `bot/forms.py` contains the functions used to interact with the forms on the target's website.
- `bot/data.py` contains generators for realistic randomized data.
- `bot/redirection.py` is used to redirect `prolifewhistleblower.com` to `127.0.0.1`
- `bot/static/captcha.html` is our simple reCaptcha checkbox page.
- `bot/logger.py` file for setting up `logging` package.
- `bot/arguments.py` file for getting arguments from the commandline.
- `requirements.txt` contains the required Python3 packages to be installed
- `.style.yapf` is the configuration file for the yapf formatter. Please run `yapf -ri ./bot/` when contributing.
- `FAQ.md` is a list of frequently asked questions and their answers.

## How to use the project

### Install Git if you dont already have it installed

Instructions can be found here
https://git-scm.com/downloads


### Clone the repo
use powershell or cmd.exe on Windows
terminal if on MacOS
if on Linux, your terminal of choice

```bash
git clone https://github.com/ramblingjordan/AbBOT-python.git

cd AbBOT-python
```

### Windows

If you don't already have `python3.exe` and `pip3.exe` installed on Windows, you can install them from the Microsoft Store.

https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7

Now we can install the required Python 3 packages for this project. Before you install the packages, consider [setting up a virtual environment for development](#using-a-virtual-environment).

```powershell
pip3.exe install -r .\requirements.txt
```

#### Running the program

Please ensure you're running the script with Adminsitrator rights, or someone with read and write access to `C:\Windows\System32\drivers\etc\hosts`.

```
python3.exe .\main.py
```

Then, you will see the following message, "Starting the web server at http://prolifewhistleblower.com:8000/". You will want to open this URL in your browser (works with browsers' Incognito mode if you want to use it). From there you will see a reCaptcha checkbox. Click or solve the reCaptcha and then submit the form.

If you see a message exactly like the following the following in your terminal, then it was successful. If it was not successful, let us know so we can try to fix the issue.

```text
Form submitted successfully.
21:17:31 bot.logger - [INFO] 1 success, 0 failures
```

To exit the program, please hit <kbd>Ctrl</kbd>+<kbd>C</kbd>.

### Linux

If you don't have `python3` or `pip3` installed, you can install the `python3` package with your preferred package manager.

```bash
sudo apt install python3
```

If you already have `python3` installed, make sure your have the latest version of `pip3` installed. You can update your `pip3` installation as follows.

```bash
python3 -m pip install --user --upgrade pip
```

Now we can install the required Python 3 packages for this project. Before you install the packages, consider [setting up a virtual environment for development](#using-a-virtual-environment).

```bash
python3 -m pip install -r ./requirements.txt
```

#### Running the program

Please ensure you're running the script with sudo, or a user with read and write access to `/etc/hosts`.

```bash
sudo python3 ./main.py
# or
sudo ./main.py
```

If you installed `python3`/`pip3` to your account and not to the system, you will want to keep your `PATH` when using `sudo`.

```bash
sudo env "PATH=$PATH" python3 ./main.py
# or
sudo env "PATH=$PATH" ./main.py
```

Then, you will see the following message, "Starting the web server at http://prolifewhistleblower.com:8000/". You will want to open this URL in your browser (works with browsers' Incognito mode if you want to use it). From there you will see a reCaptcha checkbox. Click or solve the reCaptcha and then submit the form.

If you see a message exactly like the following the following in your terminal, then it was successful. If it was not successful, let us know so we can try to fix the issue.

```text
Form submitted successfully.
21:17:31 bot.logger - [INFO] 1 success, 0 failures
```

To exit the program, please hit <kbd>Ctrl</kbd>+<kbd>C</kbd>.

### macOS

If you don't have `python3` or `pip3` installed you can either download the installer from the [Python 3.9.7 release page](https://www.python.org/downloads/release/python-397/) or install it with `brew`.

```bash
brew install python3
```

If you already have `python3` installed, make sure your have the latest version of `pip3` installed. You can update your `pip3` installation as follows.

```bash
python3 -m pip install --user --upgrade pip
```

Now we can install the required Python 3 packages for this project. Before you install the packages, consider [setting up a virtual environment for development](#using-a-virtual-environment).

```bash
pip3 install -r ./requirements.txt
```

#### Running the program

Please ensure you're running the script with sudo, or someone with read and write access to `/etc/hosts`.

```bash
sudo python3 ./main.py
# or
sudo ./main.py
```

If you installed `python3`/`pip3` with `brew` (or installed Python to your account and not to the system in another way), you will want to keep your `PATH` when using `sudo`.

```bash
sudo env "PATH=$PATH" python3 ./main.py
# or
sudo env "PATH=$PATH" ./main.py
```

Then, you will see the following message, "Starting the web server at http://prolifewhistleblower.com:8000/". You will want to open this URL in your browser (works with browsers' Incognito mode if you want to use it). From there you will see a reCaptcha checkbox. Click or solve the reCaptcha and then submit the form.

If you see a message exactly like the following the following in your terminal, then it was successful. If it was not successful, let us know so we can try to fix the issue.

```text
Form submitted successfully.
21:17:31 bot.logger - [INFO] 1 success, 0 failures
```

To exit the program, please hit <kbd>Ctrl</kbd>+<kbd>C</kbd>.

### Docker Compose

- First, [install Docker](https://docs.docker.com/get-docker/).

#### Setting up Your Machine

You'll need to edit your `hosts` file to point `prolifewhistleblower.com` to `127.0.0.1`.

### Building the Container

- Clone this repository
- Go to the root directory of the repository
- Run `docker-compose build` to build the container

### Running the Container

- Run `docker-compose up`

### Docker Container (without docker-compose)

- First, [install Docker](https://docs.docker.com/get-docker/).

#### Setting up Your Machine

You'll need to edit your `hosts` file to point `prolifewhistleblower.com` to `127.0.0.1`.

#### Building the container

- Clone this repository
- Go to the root directory of the repository
- Run `docker build -t abbot .` to build the container

#### Running the Program

Run `docker run -p 8000:8000 --name abbot abbot`

This will start the web server.
## How it looks in action

![reCaptcha in Chrome on the left side. Terminal running main.py and denoting a successful POST request on the right side.](https://cdn.discordapp.com/attachments/883159187666919549/883350251833028668/unknown.png)


### Generating text dynamically

To make use of a feature that will generate the text of your tip dynamically on each submission, set the --generate option on the command line. This will make it harder to automatically filter out these tips.

By default this will use a generic API key, which may be disabled if used excessively. If you'd like to use your own key, make a free account at [DeepAI](https://deepai.org/machine-learning-model/text-generator) and use the API key generated for you found on your profile page. Set the environment variable 'DEEP_AI_KEY' to this value by running `export DEEP_AI_KEY=your AI key goes here` (you may need to do this every time you start the program). 

## Usage

```text
usage: main.py [-h] [-v] [-c COUNT]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Increases the verbosity of the output.
  -c COUNT, --count COUNT
                        Set a maximum number of times to successfully submit to the form.
  -g, --generate
                        Generate GPT2 text from DeepAI API with key set by environment variable or default.
```

## Using a Virtual Environment

A virtual environment creates a local installation of Python, where the installed packages will be isolated from the packages installed by the main Python installation, which allows you to better keep track of what packages are used. For example, if your program requires a new module during development, you could update the requirements file via `pip freeze > requirements.txt` on Linux and macOS. This is recommended, especially if you are planning to help develop the bot. The package `venv` is shipped with Python 3.3 or later.

### Setup

#### Setup for Linux and MacOS

To create a virtual environment, make sure you are in the `AbBOT-python` directory, then execute:

```bash
python3 -m venv .env
```

This creates a directory `AbBOT-python/.env`, which contains the virtual Python installation, and will not to uploaded to GitHub during commits. Then source the activate file to use the virtual environment.

```bash
source ./.env/bin/activate
```

To check that you are in virtual environment, the command `which python3` should return a path that ends in `.../AbBOT-python/.env/bin/python3`. Now you could install the required packages *inside* the virtual environment. To leave the virtual environment and return to your main Python installation, simply use `deactivate`.

#### Setup for Windows

To create a virtual environment, make sure you are in the `AbBOT-python` directory, then execute:

```
python3.exe -m venv .env
```

This creates a directory `AbBOT-python\.env`, which contains the virtual Python installation, and will not to uploaded to GitHub during commits. Then source the activate file to use the virtual environment (again, making sure that you are in the `AbBOT-python` directory).

```
.\env\Scripts\activate
```

To check that you are in virtual environment, the command `which python3` should return a path that ends in `...\AbBOT-python\.env\Scripts\python.exe`. Now you could install the required packages *inside* the virtual environment. To leave the virtual environment and return to your main Python installation, simply use `deactivate`.
