pipeline {

    agent any
    
    stages {

        stage("Build and Compiling") {

            steps {
                echo 'Building and compiling code ...'
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
                echo 'Deploying to staging Env ...'
            }
        }
    }

}
