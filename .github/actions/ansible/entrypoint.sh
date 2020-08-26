#!/bin/sh

echo "$VAULT_PASS" > ~/.vault_pass.txt
mkdir ~/.ssh
ansible-vault view --vault-password-file=~/.vault_pass.txt ansible/ssh/ansible_key > ~/.ssh/id_rsa
chmod 0600 ~/.ssh/id_rsa

ansible-playbook -e "communitybot_version=$BOT_VERSION" --vault-password-file ~/.vault_pass.txt -i ansible/hosts/hosts.yml ansible/deploy.yml --become