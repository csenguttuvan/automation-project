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
                sh 'mkdir jenkinstest'
                echo 'Testing code for faults ...'
            }
        }

        stage("Deploy") {

            steps {
                echo "Deploying to staging to ${env.NODE_NAME}"
            }
        }
    }

}
