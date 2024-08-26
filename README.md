# Ansible

This playbook allow you to deploy Ubuntu 22.04 VMs to Vsphere and configure them as k8s nodes.
Dualstack, IPv6 prefer, keepalived.
RKE2, MetalLB, Rancher.

Upgrade possible, but not tested.
New node addining possible, but not tested.

Partially based on: [/ansible-role-rke2](https://github.com/lablabs/ansible-role-rke2)

## Preparing env to run ansible

1. Clone repository to your local machine
2. Open repository directory and run prepare-environment.pl, like next

    ```shell
    ./prepare-environment.pl
    ```

3. When environment will be ready you will see *Virtual environment successfully prepeared.* in console
4. Run playbook with run_playbook.sh script, like next

    ```shell
    ./run_playbook.sh -i inventory/<inventory file> <playbook yml file>
    ```

## Customization

### Common details

[vmware/secrets.yml](group_vars/vmware/secrets.yml) - vSphere secrets
[ssh_key](ssh_key) - add private and public ansible user keys (by default id_ed25519 and id_ed25519.pub)
[inventories/main/vmware.yml](inventories/main/vmware.yml) - vSphere and ESXi nodes
[inventories/devel/rke2-devel-0.yml](inventories/devel/rke2-devel-0.yml) - contain information about VMs to deploy

### Ubuntu VMs configuration

[roles/ubuntu/vars/users.yml](roles/ubuntu/vars/users.yml) - You can add some additional users
[roles/vmware/vars/local-vars.yml.tmpl](roles/vmware/vars/local-vars.yml.tmpl) - evaluate this template with required VM details

### RKE2 Details

[roles/rke2/vars/common/deployment_version.yml](roles/rke2/vars/common/deployment_version.yml) - rke2 and other version
[roles/rke2/vars/common/domains.yml](roles/rke2/vars/common/domains.yml) - cluster top domain names
[roles/rke2/vars/common/rke2.yml](roles/rke2/vars/common/rke2.yml) - rke2 configuration
[roles/rke2/vars/rke2-devel.yml](roles/rke2/vars/rke2-devel.yml) - cluster IPs, MetalLB BGP/BFD/Pools details

### K8S mainfests

[roles/rke2/templates/server-manifests](roles/rke2/templates/server-manifests) - server manifests
[roles/rke2/templates/agent-manifests](roles/rke2/templates/agent-manifests) - agent manifests

Note: Need to update [roles/rke2/vars/common/rke2.yml](roles/rke2/vars/common/rke2.yml) after adding new manifest

## Run deploymetn

Deploy VMs:

```shell
./run_playbook.sh -i inventories/main/ -i inventories/devel/rke2-devel-0.yml deploy-rke2-cluster-devel.yml
```

Deploy k8s:

```shell
./run_playbook.sh -i inventories/main -i inventories/devel/rke2-devel-0.yml deploy-rke2-nodes-devel.yml
```
