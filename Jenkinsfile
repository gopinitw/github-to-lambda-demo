pipeline {
  agent any
  environment {
      PATH = "/var/lib/jenkins/aws:$PATH"
  }

  stages {
    stage('Checkout code') {
      steps {
        checkout scm
      }
    }
    stage('Zip up lambda') {
        steps {
                sh 'zip "lambda3.zip" "lambda_function.py" "requirements.txt" "iam-policy.json"'
            }
        }
    
  }
}
