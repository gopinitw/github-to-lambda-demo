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
                sh 'zip "lambda3_${BUILD_NUMBER}.zip" "lambda_function.py" "requirements.txt" "iam-policy.json"'
            }
        }
     stage('Upload to AWS') {
        steps {
            sh '''function does_lambda_exist() {
              aws lambda get-function --function-name $1 > /dev/null 2>&1
              if [ 0 -eq $? ]; then
                echo "Lambda '$1' exists"
              else
                echo "Lambda '$1' does not exist"
              fi
            } && does_lambda_exist testJenkins && does_lambda_exist testJenkins2'''
            sh 'aws lambda create-function --zip-file fileb://lambda3.zip --function-name fairilambda --runtime python3.7 --role arn:aws:iam::904440666777:role/ecrregistryec2 --handler lambda_function.lambda_handler'
          }
        }
    }
  }
