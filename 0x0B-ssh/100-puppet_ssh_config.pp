#!/usr/bin/env bash
#using puppet to configure ssh requirements

file { '/etc/ssh/sshd_config':
  ensure => present,
  owner => 'root',
  group => 'root',
  mode => '0644',
  content => "
    # SSH client configuration
    Host school
    HostName <server_hostname>
    User <username>
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  ",
}
