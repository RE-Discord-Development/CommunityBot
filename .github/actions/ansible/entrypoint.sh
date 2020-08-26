#!/bin/sh

echo "$VAULT_PASS" > ~/.vault_pass.txt
mkdir ~/.ssh
ansible-vault view --vault-password-file=~/.vault_pass.txt ansible/ssh/ansible_key > ~/.ssh/id_rsa
chmod 0600 ~/.ssh/id_rsa

BOT_VERSION=$(echo "$BOT_VERSION_RAW" | sed -e 's,.*/\(.*\),\1,')

ansible-playbook -e "communitybot_version=$BOT_VERSION" -e "DISCORD_BOT_TOKEN=$DISCORD_BOT_TOKEN" --vault-password-file ~/.vault_pass.txt -i ansible/hosts/hosts.yml ansible/deploy.yml --become