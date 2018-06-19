# Ansible inventory file and playbooks for managing the PayUpJack infrastructure

## Deployemnts
Now that we've gotten our own man `ubuntu` running things on the box, the deployment is now closer to full automation.
There's no longer a need to manually clone the repo on the deployment target box. There's now only one variable that we need to provide in the vars.yml file - the `deployment_version`, which can be a git tag (going forward), commit SHA (hopefully never), or branch name (the current value). This tells the playbook which version of the code to pull from repo.
(*the 'deployment_dest' variable is still there just in case, but we're not going to be changing it*)
```
---
deployment_version: "finix_api_update"

```

### Fire away

```
ansible-playbook puj_deploy.yml -i inventory.yml -K
```
