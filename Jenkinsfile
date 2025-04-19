pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t laptop-price-prediction .'
            }
        }

        stage('Stop Old Container') {
            steps {
                echo 'Stopping old container...'
                bat '''
                docker stop laptop-price-container || exit 0
                docker rm laptop-price-container || exit 0
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                bat 'docker run -d -p 5000:5000 --name laptop-price-container laptop-price-prediction'
            }
        }
    }

    post {
        failure {
            echo 'Something went wrong!'
        }
    }
}
