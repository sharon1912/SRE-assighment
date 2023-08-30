node('zip-job-docker') {
    def image_name = "sharon-py:latest"
    def container_name = "zip-job-container"

    stage('Build') {
        docker.image(image_name).inside("--privileged --name ${container_name}") {
            sh "python3 /tmp/zip_job.py"
        }
    }

    stage('Cleanup') {
        steps {
            sh "docker rm -f ${container_name}"
            cleanWs()
        }
    }
}
