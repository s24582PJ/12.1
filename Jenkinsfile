pipeline {
    agent any

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
