# Ansible inventory file and playbooks for managing the PayUpJack infrastructure

## Deployemnts
While we're waiting on admin access to PayUpJack repo on Bitbucket, where we would configure *ssh* access, the deployments process isn't fully automated yet. There are two steps:

### Create your own copy of the PUJ repo on the destination box
(this needs to be done only once)
e.g.,
```
> git clone https://alexakarpov@bitbucket.org/teampuj/payupjack.git
```
NOTE: this is done over https and will require you to authenticate (i.e. if you're not me, edit the URL according ;) ).

### Record the path to the created folder in vars.yml
e.g.,
```
---
deployment_dest: "/opt/PUJ"
deployment_src: "/home/akarpov/payupjack" # specific to the user performing the deployment

```

### Fire away

```
ansible-playbook puj_deploy.yml -i inventory.yml -K
```
