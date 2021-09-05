import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
  '-v',
  '--verbose',
  help='Increases the verbosity of the output.',
  action='store_true'
  )
parser.add_argument(
  '-c',
  '--count',
  help='Set a maximum number of times to successfully submit to the form.',
  type=int,
  default=None)
parser.add_argument(
  '-g', '--generate', help='Generate GPT2 text from DeepAI API with key set by environment variable or default.', action='store_true'
)
parser.add_argument(
  '-t',
  '--target',
  help='Specify the target\'s IP address. Useful if the domain is not working correctly on it\'s own.',
  type=str,
  default=None
)
parser.add_argument(
  '-d',
  '--domain',
  help='Specify the target\'s fully qualified domain (FQDN). Useful if the target switches domains. Defaults to prolifewhistleblower.com',
  type=str,
  default='prolifewhistleblower.com'
)
parser.add_argument(
  '-n',
  '--nonce',
  help='Specify a nonce to use for the form submission. Skips the request for a nonce.',
  type=str,
  default=None
)
parser.add_argument(
  '-p',
  '--port',
  help='Specify the host\'s port to listen on. Useful if other services conflict on host. Defaults to 8000.',
  type=int,
  default=8000
)
args = parser.parse_args()
