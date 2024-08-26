# Ansible

## Preparing

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

## Playbooks

### VMWare

First of all, read [README.md](roles/vmware/README.md)

To execute playbook run next command:

```shell
./run_playbook.sh -i inventory/infra vmware.yml
```
