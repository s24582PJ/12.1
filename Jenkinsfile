pipeline {
    agent{
        docker{
            image 'python:3.8'
            arg '-u root:root'
        }
    }

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
