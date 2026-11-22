
pipeline {
    agent any

    environment {
        PATH = "C:\\Users\\adity\\AppData\\Local\\Programs\\Python\\Python314;${env.PATH}"
    }

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
  