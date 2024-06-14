pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
        }
        
    }
}
