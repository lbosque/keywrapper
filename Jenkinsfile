pipeline {
  agent any
  stages {
    stage('s1') {
      steps {
        sh 'echo "HELLO"'
      }
    }
    stage('prepare-env') {
      steps {
        sh '''virtualenv /tmp/keywrapper
        /tmp/keywrapper/bin/pip install redis
'''
      }
    }
    stage('test') {
      steps {
        sh '''/tmp/keywrapper/bin/python tests/unit/test_keywrapper.py
'''
      }
    }
  }
}
