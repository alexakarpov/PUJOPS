# Ansible inventory file and playbooks for managing the PayUpJack infrastructure

## Deployemnts
While we're waiting on admin access to PayUpJack repo on Bitbucket, where we would configure *ssh* access, the deployments process isn't fully automated yet. There are two steps:
### Create your local repo on the destination box
e.g.,
```
> git clone git@bitbucket.org:teampuj/payupjack.git
```
### Record the path to the created folder in vars.yml
e.g.,
```
---
deployment_dest: "/opt/PUJ" # same for everyone
deployment_src: "/home/akarpov/payupjack" # specific to the user performing the deployment

```

### Fire away

```
ansible-playbook puj_deploy.yml -i inventory.yml -K
```
