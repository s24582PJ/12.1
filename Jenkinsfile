pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s . -p "*.py"'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
        }
    }
}
