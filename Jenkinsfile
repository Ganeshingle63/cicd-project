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
