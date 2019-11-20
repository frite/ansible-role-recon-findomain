recon_findomain
=========

[![Build Status](https://travis-ci.com/frite/ansible-role-recon-findomain.svg?branch=master)](https://travis-ci.com/frite/ansible-role-recon-findomain)

Ansible role to install findomain. 

Role Variables
--------------

Download and install the latest findomain release and setup the required tokens.

Dependencies
------------
The following variables can be used.
* `recon_findomain_username: root`. Sets the username
* `recon_findomain_home_dir: /root`. The path to user's home.
* `recon_findomain_fb_token: fb_token`. The Facebook Token. Requires username to be set.
* `recon_findomain_spyse_token: spyse`. The Spyse token. Requires username to be set.
* `recon_findomain_virustotal_token: vt`. The VirusTotal token. Requires username to be set.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-role-recon-findomain }

License
-------

BSD
