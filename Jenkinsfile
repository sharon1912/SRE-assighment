pipeline {
    agent {
        docker { image '212620447/sre-assighment:1'
                 args '--privileged'  
                 label 'zip-job-docker' 
         }
    }

    stages {
        stage('Build') {
            steps {
                // run the python script
                sh 'python3 /tmp/zip_job.py'
            }
        }
    
        stage('Publish') {
            steps {
                
                // parsing the VERSION env to jenkins pipeline env
                script {
                    env.VERSION = sh(script:'echo $VERSION', returnStdout: true).trim()
                }

                // coping the created files (artifactory plugin does not reconize them on tmp)
                sh 'mkdir zipped_files'
                sh 'cp -r /tmp/zipped_files .'

                
                rtUpload (
                    serverId: 'artifactory',
                    failNoOp: true,
                    spec: """{
                        "files": [
                         {
                            "pattern": "zipped_files/*.zip",
                            "target": "binary-storage/z${VERSION}/"
                          }
                        ]
                    }""",)
            }
        }
    }

    post {
        success {
            echo 'sending success job email'
            emailext body: ' Declarative pipeline succeeded ',
                subject: 'pipeline succeeded',
                to: 'sharonku.second@gmail.com'
        }
        failure {
            echo 'sending failure job email'
            emailext body: 'Declarative pipeline failed',
                subject: 'pipeline failed',
                to: 'sharonku.second@gmail.com'
        }
        always {
            echo 'cleaning workspace'
            deleteDir() 
        }
    }
}