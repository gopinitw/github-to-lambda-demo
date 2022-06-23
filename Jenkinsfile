pipeline {
  agent any
  environment {
      PATH = "/var/lib/jenkins/aws:$PATH"
      ROLE_ARN = "arn:aws:iam::904440666777:role/ecrregistryec2"
      FUNCTION_NAME = "fairilambda"
      RELEASE_ASSET_NAME = "lambda3.zip" 
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
  stage('Update Lambda function code') {
      steps {
        script {
          sh '''
          echo "Deploying to: $FUNCTION_NAME using role: $ROLE_ARN"
          set +x
          STS_SESSION_NAME=$(whoami)-$(date +%s)
          STS=$(aws sts assume-role --role-arn $ROLE_ARN --role-session-name "${STS_SESSION_NAME}")
          export AWS_ACCESS_KEY_ID=$(echo "${STS}" | jq -r .Credentials.AccessKeyId)
          export AWS_SECRET_ACCESS_KEY=$(echo "${STS}" | jq -r .Credentials.SecretAccessKey)
          export AWS_SESSION_TOKEN=$(echo "${STS}" | jq -r .Credentials.SessionToken)
          set -x
          aws lambda update-function-code --function-name $FUNCTION_NAME --zip-file fileb://$RELEASE_ASSET_NAME
          '''
        }
      }
  }
  }
}
