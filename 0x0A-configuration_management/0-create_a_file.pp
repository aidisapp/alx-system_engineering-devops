#!/usr/bin/pup
# creates a file in /tmp
# Requirements:
#   This file path is /tmp/school
#   The file permission is 0744
#   The file owner is www-data
#   The file group is www-data
#   This file contains I love Puppet

file { '/tmp/school':
  content =>'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
