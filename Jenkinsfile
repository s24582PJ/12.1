pipeline {
    agent any
    tools{
        git 'Default'
    }
    
    stages {
        stage('Test') {
            steps {
                script {

                    sh 'python -m unittest discover -s . -p "test_*.py"'
                }
            }
        }
    }
    
    post {
        always {
            echo "dziala zawsze"
            junit '**/unittest.xml'
        }
    }
}
