#!/usr/bin/env python3
import os
from .logger import logger
from .arguments import args

hosts_filename = ''
if os.name == 'nt':
  hosts_filename = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
else:
  hosts_filename = '/etc/hosts'

logger.debug('hosts filename is ' + hosts_filename)


# Returns the contents of the OS specific hosts file without any redirects
# regarding the domain specified in cmdline arguments
def get_hosts_without_redirection():
  # Get the hosts file without the redirect
  logger.debug(f'Getting the hosts file without the redirect to {args.domain}')
  try:
    with open(hosts_filename, 'r') as hosts_file:
      return ''.join([line for line in hosts_file.readlines() if not args.domain in line]).rstrip() + '\n'
  except IOError:
    logger.critical('Unable to read {}'.format(hosts_filename))
    print('Please run again but with sudo, as Administrator, or a user with write access to the hosts file.')
    exit(1)


# Opens OS specific hosts file and redirects the domain specified in cmdline arguments to localhost
def redirect_to_localhost():
  logger.debug(f'Redirecting {args.domain} to 127.0.0.1')
  try:
    with open(hosts_filename, 'a') as hosts_file:
      hosts_file.write(f'127.0.0.1 {args.domain}\n')
  except IOError:
    logger.critical('Unable to append to {}'.format(hosts_filename))
    print('Please run again but with sudo, as Administrator, or a user with write access to the hosts file.')
    exit(1)


# Opens OS specific hosts file and redirects the domain specified in cmdline arguments to the IP address
# specified in the cmdline arguments. If no IP address is specified, the redirect is removed.
def redirect_to_target():
  logger.debug('Redirecting {} to {}'.format(args.domain, args.target if args.target is not None else 'target'))
  hosts_data = get_hosts_without_redirection()
  try:
    with open(hosts_filename, 'w') as hosts_file:
      hosts_file.write(hosts_data)
      if args.target is not None:
        hosts_file.write(f'{args.target} {args.domain}\n')
  except IOError:
    logger.critical('Unable to redirect back to the target {}'.format(hosts_filename))
    print('Please remove it yourself or run me with sudo, as Administrator, or a user with write access to the hosts file.')
    exit(1)
