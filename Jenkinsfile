pipeline{
   agent any
   stages{
      stage ('Deploy') {
         steps{
            sshagent(credentials : ['dcs_1']) {
                  sh 'ssh -o StrictHostKeyChecking=no root@164.128.168.166 uptime'
                  sh 'ssh -v root@164.128.168.166'
                  sh 'scp . root@164.128.168.166:/remotehost/target'
            }
         }
      }
   }
}

