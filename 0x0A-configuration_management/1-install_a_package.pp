#!/usr/bin/env puppet
# Install flask from pip3.
# Requirements:
#   We will need to install flask
#   The version must be 2.1.0
package { 'python3-pip':
  ensure => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
