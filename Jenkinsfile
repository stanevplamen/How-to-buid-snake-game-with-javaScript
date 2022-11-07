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
      stage ('Deploy / Get from docker') {
         steps{
            sshagent(credentials : ['dcs_2']) {
                  sh 'ssh -o StrictHostKeyChecking=no root@164.128.168.166 uptime'
                  sh 'docker pull plamen333/ira:1.0.0'
                  sh 'docker run plamen333/ira:1.0.0'
            }
         }
      }
   }
}

