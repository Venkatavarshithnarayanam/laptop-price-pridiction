pipeline {
    agent any

    environment {
        IMAGE_NAME = "laptop-app"
        CONTAINER_NAME = "laptop-price-prediction"
        PORT = "5000"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo "Cloning repository..."
                // If this is a freestyle project with Jenkins Git configured, this is optional
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Stop Old Container') {
            steps {
                echo "Stopping old container if running..."
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "Running Docker container..."
                sh "docker run -d --name ${CONTAINER_NAME} -p ${PORT}:5000 ${IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo "App running at http://localhost:5000"
        }
        failure {
            echo "Something went wrong!"
        }
    }
}
