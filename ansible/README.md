Ansible playbooks for Raspi deployments

- Lighttpd
- SQLite
- PIP (to install Paho Mqtt, ...)
- Systemd (to start Python scripts at boot)

Use APT dependencies in vars to install a needed packages:
Example of a usage:

Content of ansible/roles/fv/tasks/main.yml :
---
- name: install dependencies
  include: dependencies.yml

- name: sudo access for specific tasks
  include: sudo.yml

- name: add credentials
  include: credentials.yml

Content of ansible/roles/fv/tasks/dependencies.yml :
---
- name: install dependencies
  apt: pkg={{item}} state=latest
  with_items: fv_env.dependencies
  tags: fv-deps

Content of ansible/roles/fv/vars/main.yml :
---
fv_env:
  dependencies:
    - libpython-dev
    - nmap


These are called fromnsible/fv.yml :
---
- name: prepare FV VMs as jenkins slaves
  hosts: fv
  gather_facts: no
  sudo: yes

  vars_files:
    - vars/common.yml

  roles:
    - vm
    - swap-disabled
    - fv
