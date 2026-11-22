pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python --version'
            }
        }

        stage('Automated Testing') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pytest tests/'
            }
        }
    }

    post {
        success {
            echo 'Pipeline Successful!'
        }
        failure {
            echo 'Pipeline Failed!'
        }
    }
}
