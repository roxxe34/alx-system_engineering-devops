# install_flask.pp

package { 'python3-pip':
  ensure => installed,
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/usr/local/bin'],
  require => [Package['python3-pip'], Package['werkzeug']],
}

