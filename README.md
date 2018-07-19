# Ansible inventory file and playbooks for managing the PayUpJack infrastructure

## Deploying users
```
**ansible-playbook puj_users.yml -i hosts.yml -vv --extra-vars "puj_hosts=staging"**
```
note that the group of servers is provided in extra-args; if nothing is provided, it will default to my test/dev server

## Deploying *everythong*
(this will deploy users too)

```
ansible-playbook provision..yml -i hosts.yml -K --extra-vars "puj_hosts=staging"
```
