#!/bin/bash
java -jar jenkins-cli.jar -s  http://13.201.70.135:8080/ -auth @creds who-am-i
set -x
for plugin in $(cat plugins.txt); do
    java -jar jenkins-cli.jar \
    -s http://13.201.70.135:8080/ \
    -auth @creds \
    install-plugin "$plugin"
done
# java -jar jenkins-cli.jar \
#     -s http://3.109.5.227:8080/ \
#     -auth @creds \
#     safe-restart
