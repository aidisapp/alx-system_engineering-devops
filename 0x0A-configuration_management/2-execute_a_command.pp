#!/usr/bin/pup
# This creates a manifest that kills a process named killmenow
# Requirements:
#   We must use the exec Puppet resource
#   We must use pkill

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
