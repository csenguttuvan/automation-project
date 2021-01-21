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
                sh 'apt-get update && apt-get upgrade'
                sh 'cd /home/ubuntu && mkdir pipeline && cd pipeline && touch sucess'
                sh "echo ${env.BUILD_ID} on ${env_JENKINS_URL} is successful"
                echo "Test succesfully run on ${env.BUILD_URL}"

            }
        }

        stage("Deploy") {

            steps {
                echo "Deploying to staging to ${env.NODE_NAME}"
            }
        }
    }
}