# connected world api

docker-compose up

aws:
sudo yum install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo reboot
sudo yum install -y git
sudo chkconfig docker on

sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose


sudo systemctl start docker


sudo yum install python3.7
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user