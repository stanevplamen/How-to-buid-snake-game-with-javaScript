pipeline{
   agent any
   stage ('Deploy') {
      steps{
         sshagent(credentials : ['use-the-id-from-credential-generated-by-jenkins']) {
               sh 'ssh -o StrictHostKeyChecking=no root@164.128.168.166 uptime'
               sh 'ssh -v root@164.128.168.166'
               sh 'scp . root@164.128.168.166:/remotehost/target'
         }
      }
   }
}

