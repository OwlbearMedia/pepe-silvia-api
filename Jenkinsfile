pipeline {
    agent any 

    stages {
        stage("Clone Code") {
            steps {
                echo "Cloning the code"
                git url:"https://github.com/OwlbearMedia/pepe-silvia-api", branch: "main"
            }
        }
        stage("Build") {
            steps {
                echo "Building the image"
                sh "docker build -t pepe-silvia ."
            }
        }
        stage("Push to Amazon ECR") {
            steps {
                echo "Pushing the image to ECR"
                withAWS(region: 'us-west-2', credentials: 'pepe-silva') {
                    sh "aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 640550388417.dkr.ecr.us-west-2.amazonaws.com"
                    sh "docker tag pepe-silvia:latest 640550388417.dkr.ecr.us-west-2.amazonaws.com/pepe-silvia:latest"
                    sh "docker push 640550388417.dkr.ecr.us-west-2.amazonaws.com/pepe-silvia:latest"
                }
            }
        }
        stage("Deploy") {
            steps {
                echo "Deploying the container"
                withAWS(region: 'us-west-2', credentials: 'pepe-silva') {
                    sh "docker pull 640550388417.dkr.ecr.us-west-2.amazonaws.com/pepe-silvia:latest"
                    sh "docker run -v ~/.aws:/root/.aws -p 5328:5328 640550388417.dkr.ecr.us-west-2.amazonaws.com/pepe-silvia"
                }
            }
        }
    }
}
