pipeline {
    agent any

    stages {
        stage('without docker') {
            steps {
                sh '''
                    echo "without docker"
                '''
            }
        }
         stage('Build') {
             agent {
                 docker {
                     image 'python:3.12'
                     reuseNode true
                 }
             }
            steps {
                sh '''
                    ls -la
                    python --version
                '''
            }
        }
    }
}
