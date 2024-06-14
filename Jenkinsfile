pipeline {
    agent any

    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3.8'
                    args '-u root:root'
                }
            }
            steps {
                sh 'python3 -m unittest discover -s . -p "*.py"'
            }
        }
    }

    post {
        always {
            junit '**/test-results.xml'
        }
    }
}
