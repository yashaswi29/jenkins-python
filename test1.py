# 11381a182513a3cd0daf1ed13ded596b66

import jenkins
import json
import os

host = "http://localhost:8080"
username = "yashaswi"
password = "11381a182513a3cd0daf1ed13ded596b66"
server = jenkins.Jenkins(host, username, password)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

# creating blank jobs
# server.create_job("job1", jenkins.EMPTY_CONFIG_XML)

#create pre planned jobs using xml and python
# project1_xml = open ("project1.xml", mode ='r', encoding ='utf-8').read()
# server.create_job("job2", project1_xml)

#view jobs
# jobs = server.get_jobs()
# print(jobs)

#updated jobs // this updated means, you should have the updated xml
# project1_xml = open ("project1.xml", mode ='r', encoding ='utf-8').read()

# #trigger jobs
# server.build_job("job1")

#last build number
last_build_number = server.get_job_info('job1')['lastCompletedBuild']['number']
print("Build Number", last_build_number)



