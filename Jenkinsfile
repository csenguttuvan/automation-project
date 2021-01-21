pipeline {
    environment {
        process1 = "sudo apt-get update && sudo apt-get upgrade" //defining the variable

    }

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
                sh ${process1}
                sh 'exit 1'
                sh 'cd /home/ubuntu && sudo mkdir pipeline2 && cd pipeline2 && sudo touch sucess'
                sh 'echo "${env.BUILD_ID} on ${env.JENKINS_URL} is successful" >> /home/ubuntu/pipeline2/sucess'
                    
                echo "Test succesfully run on ${env.BUILD_URL}"

            }
        }

        stage("Deploy") {

            steps {
                echo "Deploying to staging to ${env.NODE_NAME}"
            }
        }
    }
}git 