# Ansible inventory file and playbooks for managing the PayUpJack infrastructure

## Deploying users
```
ansible-playbook puj_users.yml -i hosts.yml -vv --extra-vars "puj_hosts=staging"
```
note that the group of servers is provided in extra-args; if nothing is provided, it will default to my test/dev server (which you don't have private keys to access anyway =)

also note: the names (like "staging") depend on your .ssh/config to be set up correctly. E.g., my has this stanza:

```
Host puj-staging
     Hostname dev.payupjack.com
     User akarpov
```

You'd need your own 'User' with sudo access (e.g., 'martin', who does have it, and Martin's public key has been deployed to the staging box)

## Deploying *everything*
(this will deploy users too)
this will install all the dependencies, both system and Python packages; and will set up all the configuration for Nginx and UWSGI, as well as the start script and /opt/PUJ/puj_run.sh, and will register it with systemd to run on reboot.
```
ansible-playbook provision.yml -i hosts.yml -K --extra-vars "puj_hosts=staging"
```
## manual deployment of code ##

if you don't have Ansible chops to run the playbooks here, you can perform a manual deployment, once you checked the changes into our Bitbucket repo. It's very simple:

```
cd /opt/PUJ
sudo -u ubuntu
git pull
```
