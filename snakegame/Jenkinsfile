pipeline{
   agent any
   stages{
      stage('login server'){
         steps{
            sshagent(credentials:['dcs_server']){
               sh 'ssh  -o StrictHostKeyChecking=no  root@164.128.168.166 uptime "whoami"'
          }
        echo "success lgoin"
         }
       }
   }
}