# a puppet file 

file { '/root/.ssh/config':
    ensure => present,
    content => "
        Host server
        HostName 52.91.151.130
        User ubuntu
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
    ",
}
