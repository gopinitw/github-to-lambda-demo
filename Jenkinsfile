pipeline {
  agent any
  environment {
      PATH = "/var/lib/jenkins/aws:$PATH"
      awscred = "awscr"
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
    stage("Upload"){
        steps{
                sh  'withAWS(region:"useast-1", credentials:"${awscred})'{
                    s3Upload(file:"lambda3_${BUILD_NUMBER}.zip", bucket:"${bucket}", path:"lambda3_${BUILD_NUMBER}.zip/")
                }    
        }
      }
                        
  }
