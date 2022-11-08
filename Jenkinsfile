pipeline{
   agent any
   stages{
      stage('Start container') {
         steps {
            sh 'sudo docker compose up -d --no-color --wait'
            sh 'sudo docker compose ps'
         }
      }
      stage('Deploy container to repo DockerHub') {
         steps {
            sh 'sudo docker image tag swc-pss:latest plamen333/ira:1.0.0'
            sh 'sudo docker image push plamen333/ira:1.0.0'
         }
      }
      stage ('Clean containers') {
         steps{
            sshagent(credentials : ['dcs_1']) {
                  sh 'ssh -o StrictHostKeyChecking=no root@164.128.168.166 uptime'
                  sh 'ssh -v root@164.128.168.166'
                  sh 'ssh -v root@164.128.168.166 "docker stop $(docker ps -q)"'
                  sh 'ssh -v root@164.128.168.166 "docker rm $(docker ps -a -q)"'
            }
         }
      }
      stage ('Deploy container from docker') {
         steps{
            sshagent(credentials : ['dcs_1']) {
                  sh 'ssh -o StrictHostKeyChecking=no root@164.128.168.166 uptime'
                  sh 'ssh -v root@164.128.168.166'
                  sh 'ssh -v root@164.128.168.166 docker pull plamen333/ira:1.0.0'
                  sh 'ssh -v root@164.128.168.166 docker run -d -p 80:80 plamen333/ira:1.0.0'
            }
         }
      }
   }
}

