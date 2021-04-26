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

sudo yum install -y git
git clone https://github.com/avelaga/connected_world_api.git
sudo yum install python3.7
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
pip3 install -r requirements.txt

# Usage

Run services in the background:
`docker-compose up -d`

Run services in the foreground:
`docker-compose up --build`

Inspect volume:
`docker volume ls`
and
`docker volume inspect <volume name>`

View networks:
`docker network ls`

Bring services down:
`docker-compose down`


create sym link for init script to find coekr compose:
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose