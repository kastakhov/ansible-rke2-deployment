# VMWare VM role

Download OVA (Default: Ubuntu Jammy) file from the internet and deploy it as VM

## Playbook variables

Edit ansible/roles/vmware/vars/user_defined.yml with your favorite editor (like nano or vim) and adjust values inside double quotes

### Credentials to vSphere server

```text
VMWARE_VC_USER: ""
VMWARE_VC_PASSWORD: ""
```

### VM placeholder and name

```text
VMWARE_VM_PARRENT_FOLDER: ""
VMWARE_VM_FOLDER: ""
VMWARE_VM_NAME: ""
```

### VM parameters

```text
VM_RAM_SIZE: 2
VM_CPU_COUNT: 2
VM_DISK_SIZE: 32
```
