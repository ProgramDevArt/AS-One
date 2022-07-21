# ASOne

#### Table of Contents  
- [Docker Installation on Ubuntu](#docker-installation-on-ubuntu)  
- [Setting Up detectron2](#setting-up-detectron2)
- [Docker Building](#docker-building)


## Docker Installation on Ubuntu

### Install using Shell Script

```
chmod a+x docker-installation.sh
./docker-installation.sh 
```

### Manuall Install
1. Run following command to remove all old versions on docker

```
sudo apt-get remove docker docker-engine docker.io containerd runc
```

2. Set up Repository

- Update the apt package index and install packages to allow apt to use a repository over HTTPS:

```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```
- Add Docker’s official GPG key:

```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

- Use the following command to set up the repository:

```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
3. Install Docker Engine

- Update the apt package index, and install the latest version of Docker Engine, containerd, and Docker Compose:

```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```




## Setting Up detectron2
1. Clone the Repo
```
git clone https://github.com/facebookresearch/detectron2.git
```
2. Goto the detectron2 directory
```
cd detectron2
```
3. Download some sample images in this folder

## Docker Building

1. Build docker contanier
```
docker build -t [IMAGE_NAME]:[TAG]
```

- IMAGE_NAME = Asign a name to image
- TAG = Asign a tag to image

2. Run Docker Contaner

```
docker run --gpus all --env="DISPLAY" --net=host -v [PATH_TO_LOCAL_DIR]:/workspace/  -it [IMAGE_NAME]:[TAG]
```
- PATH_TO_LOCAL_DIR = Path to detectron2 directory or use `${PWD}` if already in that directory

3. In Docker terminal run demo.py file

```
python demo/demo.py --input [PATH_TO_TEST_IMAGE]  --output [PATH_TO_OUTPUT_IMAGE] \
  --opts MODEL.DEVICE [DEVICE] \ 
  MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl
```

- PATH_TO_TEST_IMAGE = Path of test image
- PATH_TO_OUTPUT_IMAGE = Path of Results
- DEVICE = device to use i.e. cpu or gpu
