pipeline {
	agent any
	stages {
		stage ("Git checkout"){
			steps {
				git branch: "master",
					url: "https://github.com/leman-os/otus_python_project.git"
				sh "ls"
			}
		}
		stage ("Python Flask Prepare"){
			steps {
				sh "pip3 install -r requirements.txt"
			}

		}
		stage ("Unit Test"){
			steps{
				sh "python3 test_basic.py"
			}
		}
		stage ("Python Bandit Security Scan"){
			steps{
				sh "docker run --rm --volume \$(pwd) secfigo/bandit:latest"
			}
		}
		stage("Dependency Check with Python Safety") {
			steps {
				script {
					try {
						sh "docker run --rm --volume \$(pwd) pyupio/safety:latest safety check"
						sh "docker run --rm --volume \$(pwd) pyupio/safety:latest safety check --json > report.json"
					} catch (Exception e) {
						currentBuild.result = 'UNSTABLE'
						echo "Dependency Check failed, but the pipeline will continue"
						echo "Error details: ${e.getMessage()}"
					}
				}
			}
		}
		stage ("Static Analysis with python-taint"){
			steps{
				sh "docker run --rm --volume \$(pwd) vickyrajagopal/python-taint-docker pyt ."
			}
		}					
	}
}
