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
                    filename 'Dockerfile'
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
