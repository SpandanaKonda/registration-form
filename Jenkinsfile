pipeline{
    agent any
        stages{
            stage("Build"){
                steps{
                echo " Build docker image"
                bat "docker build -t mypythonflaskapp ."
                }
            }
            stage("Run"){
                steps{
                    echo "run application in container"
                    bat "docker rm -f mycontainer|| exit 0"
                    bat "docker run -d -p 5000:5000 --name mycontainer mypythonflaskapp"
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
