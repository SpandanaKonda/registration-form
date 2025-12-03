pipeline{
    agent any
        stages{
            stage("Build"){
                steps{
                echo " Build docker image"
                bat "docker build -t myimg"
                }
            }
            stage("Run"){
                steps{
                    echo "run application in container"
                    bat "docker rm -f mycontainer|| exit 0"
                    bat "docker run -d -p 5000:5000 --name mycontainer myimg"
                }

            }
        }
        post{
            success{
                echo "success"
            }
            failure{
                echo "faillll"
            }
        }
    
}
