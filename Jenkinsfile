pipeline {
    agent any
      
    stages {

        stage("Build and Compiling") {

            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"  //echoes build number and Jenkins URl with the given Evniromental variables
            }
        }

        stage("Test") {

            steps {
                echo 'Testing code for faults ...'
                sh 'sudo apt-get update && sudo apt-get upgrade'
                sh 'sudo rm -rf /home/ubuntu/pipeline2' //removes the dir if dir exists
                sh 'cd /home/ubuntu && sudo mkdir pipeline2 && cd pipeline2 && sudo touch sucess'
               

                echo "${env.BUILD_ID} on ${env.JENKINS_URL}"
                    
                echo "Test succesfully run on ${env.BUILD_URL}"

            }
        }

        stage("Deploy") {

            steps {
                echo "${env.NODE_NAME} has been deployed successfully after ${env.BUILD_ID} tries" 
                sh '''#!/bin/bash
                echo "Deployment was successful > /home/ubuntu/pipeline2/sucess"
                '''
            }
        }
    }
}