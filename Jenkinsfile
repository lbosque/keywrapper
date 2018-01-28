pipeline {
  agent any
  stages {
    stage('s1') {
      steps {
        sh 'echo "HELLO"'
      }
    }
    stage('test') {
      steps {
        sh '''python tests/unit/test_keywrapper.py
'''
      }
    }
  }
}