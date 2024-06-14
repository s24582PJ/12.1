pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                script {

                    sh 'apt update && apt install -y python3'

                    sh 'pip install -r requirements.txt'

                    sh 'python3 -m unittest discover -s . -p "test_*.py"'
                }
            }
        }
    }
    
    post {
        always {

            junit '**/unittest.xml'
        }
    }
}
