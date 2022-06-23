pipeline {
  agent any
  environment {
      PATH = "/var/lib/jenkins/aws:$PATH"
      ROLE_ARN = "arn:aws:iam::904440666777:role/ecrregistryec2"
      FUNCTION_NAME = "fairi2"
      RELEASE_ASSET_NAME = "lambda5.zip" 
  }
  stages {
    stage('Checkout code') {
      steps {
        checkout scm
      }
    }
    stage('Zip up lambda') {
        steps {
                sh 'zip "lambda5.zip" "lambda_function.py"'
            }
        }
  stage('Update Lambda function code') {
      steps {
        script {
          sh '''
          echo "Deploying to: $FUNCTION_NAME using role: $ROLE_ARN"
          aws lambda update-function-code --function-name $FUNCTION_NAME --zip-file fileb://$RELEASE_ASSET_NAME
          '''
        }
      }
  }
  }
}
