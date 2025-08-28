pipeline {
    agent any

    stages {
        stage('without docker') {
            steps {
                sh '''
                    echo "without docker"
                    ls -la
                '''
            }
        }
         stage('with docker') {
             agent {
                 docker {
                     image 'python:3.12'
                     reuseNode true
                 }
             }
            steps {
                sh '''
                    echo "with docker"
                    ls -la
                '''
            }
        }
    }
}
