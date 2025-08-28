// pipeline {
//     agent any

//     stages {
//         stage('without docker') {
//             steps {
//                 sh '''
//                     echo "without docker"
//                 '''
//             }
//         }
//          stage('Build') {
//              agent {
//                 //  docker {
//                 //     image 'python:3.12'
//                 //     reuseNode true
//                 //  }
//                 dockerfile {
//                     filename 'Dockerfile'
//                     dir '.'
//                 }
//              }  
//             steps {
//                 sh '''
//                     ls -la
//                     python --version
//                 '''
//             }
//         }
//     }
// }

pipeline {
    agent any

    environment {
        PROJECT_ID = 'shaped-aegis-387005'
        REGION = 'us-east1'
        REPO_NAME = 'cicd-project'
        IMAGE_NAME = 'my-python-app'
        IMAGE_TAG = 'latest'
        FULL_IMAGE_PATH = "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Authenticate with GCP') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GCLOUD_KEY')]) {
                    sh """
                        gcloud auth activate-service-account --key-file=$GCLOUD_KEY
                        gcloud config set project $PROJECT_ID
                        gcloud auth configure-docker ${REGION}-docker.pkg.dev --quiet
                    """
                }
            }
        }

        stage('Tag & Push to Artifact Registry') {
            steps {
                script {
                    sh """
                        docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${FULL_IMAGE_PATH}
                        docker push ${FULL_IMAGE_PATH}
                    """
                }
            }
        }
    }
}

