pipeline {
  agent any
  environment {
      PATH = "/var/lib/jenkins/aws:$PATH"
  }
  parameters {
    string(name: 'ROLE_ARN', description: 'IAM role to assume when calling AWS Lambda API')
    string(name: 'FUNCTION_NAME', description: 'Function name of the Lambda we will update the code for')
    string(name: 'RELEASES_API_URL', description: 'api.github.com releases URL for the GitHub repo where code releases are made (ends in "/releases")')
    string(name: 'RELEASE_VERSION', description: 'Lambda release version to deploy')
    string(name: 'RELEASE_ASSET_NAME', defaultValue: 'main.zip', description: 'Name of the release asset to deploy')
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
