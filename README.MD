Steps on how I executed the assignment:

1. I installed and configured Jenkins based on the Jenkins documentation. Additionally, I created a socket between the Jenkins container and my local Docker daemon so it could run Docker inside Docker.

2. I installed and configured JFrog based on the JFrog Docker documentation.

3. I created a Docker network and joined both containers to it. If I didn't create a network, the containers could not communicate with each other.

4. I installed the Artifactory plugin and configured it for my JFrog container, using the credentials that I had been given.

5. I wrote the Python script and created the Dockerfile that the Jenkins agent will run on.

6. I created a declarative pipeline and configured it for my GitHub repo.