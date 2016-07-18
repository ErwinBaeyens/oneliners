virtualenv venv
source venv/bin/activate
pip install -r requirements.txt --no-deps
python venv/var/hw_support/generate_testdriver_preinstalled_yaml.py 172.16.1.1 -y testdriver_newflow.yaml
testdriver setup -c preinstalled_testdriver_newflow.yaml -o "distro=activescale__blackbanner-ms88,upgrade_to_distro=activescale__blackbanner-ms90,os_install_branch=blackbanner-ms90,upgrade_health_check=false,update_marvin_model=false,product_version_name='ActiveScale 5.0.90',downgrade_to_distro="
testdriver provision


testdriver test -t "test_newflow" --ignore-runner-args -- -sv tests/test_newflow/test_newflow.py:TestNewFlow.test_002_upgrade
