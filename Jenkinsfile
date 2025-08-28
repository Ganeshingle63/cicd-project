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
                //  docker {
                //     image 'python:3.12'
                //     reuseNode true
                //  }
                dockerfile {
                    filename 'Dockerfile'
                    dir '.'
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
