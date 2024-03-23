# Configuring SSH client to refuse to authenticate using a password.
file { '/etc/ssh/sshd_config':
  ensure  => present,
  content => template('0x0B-ssh/templates/sshd_config_template.erb'),
  replace => true,
}

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => template('0x0B-ssh/templates/ssh_config_template.erb'),
  replace => true,
}
