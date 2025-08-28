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
                    image 'Dockerfile'
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
