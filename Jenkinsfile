pipeline {
    agent any
    tools{
        git 'Default'
    }
    
    
    
    post {
        always {
            echo "dziala zawsze"
            junit '**/unittest.xml'
        }
    }
}
