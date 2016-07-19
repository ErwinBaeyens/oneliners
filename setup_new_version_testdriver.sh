git clone git@gitlab.amplidata.com:product/activescale.git preinstalled-ac-tc-1s1b-ms96
git checkout blackbanner-ms96
cd test-common
./setup_venv.sh
va
cd ..
# edit testdriver.yaml and remove all instances of " legacy_network_private:true
testdriver setup 1s1b
testdriver provision
testdriver show machines
