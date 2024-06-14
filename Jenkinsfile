pipeline {
    agent any
    tools{
        git 'Default'
    }
    
    stages {
        stage('Test') {
            steps {
                script {
                    // Aktualizacja pakietów apt z uprawnieniami sudo
                    sh 'sudo apt update'
                    // Instalacja Pythona
                    sh 'sudo apt install -y python3'
                    // Instalacja zależności
                    sh 'pip install -r requirements.txt'
                    // Uruchomienie testów jednostkowych
                    sh 'python3 -m unittest discover -s . -p "test_*.py"'
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
