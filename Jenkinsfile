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
          dir('aws_lambda'){
                sh 'zip "lambda3.zip" "lambda_function.py" "requirements.txt"'
            }
        }
    }
    stage('Upload to AWS') {
        steps {
          dir('lambda/testJenkins') {
            sh '''function does_lambda_exist() {
              aws lambda get-function --function-name $1 > /dev/null 2>&1
              if [ 0 -eq $? ]; then
                echo "Lambda '$1' exists"
              else
                echo "Lambda '$1' does not exist"
              fi
            } && does_lambda_exist testJenkins && does_lambda_exist testJenkins2'''
            sh 'aws lambda create-function --zip-file fileb://testJenkins.zip --function-name testJenkins --runtime python3.7 --role <role> --handler testJenkins.lambda_handler'
          }
        }
    }
  }
}
