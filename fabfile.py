from __future__ import with_statement
from fabric.api import *
from fabric.contrib.project import rsync_project

env.gateway = 'linux-bastion-ex.tudelft.nl'
env.user = 'hledoux'
env.hosts = ['3d.bk.tudelft.nl']



def deploy():
    local("jekyll build")
    remotedir = '/var/www/courses/geo2020/'
    rsync_project(local_dir='./_site/', 
                  remote_dir=remotedir,
                  delete=True)
    run('cd %s' % remotedir)
    