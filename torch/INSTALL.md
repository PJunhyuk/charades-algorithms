Torch ResNet Installation
=========================

This is the suggested way to install the Torch ResNet dependencies on [Ubuntu 14.04+](http://www.ubuntu.com/):
* NVIDIA CUDA 7.0+
* NVIDIA cuDNN v4
* Torch
* ImageNet dataset

## Requirements
* NVIDIA GPU with compute capability 3.5 or above

## Install CUDA
1. Install the `build-essential` package:
 ```bash
 sudo apt-get install build-essential
 ```

2. If you are using a Virtual Machine (like Amazon EC2 instances), install:
 ```bash
 sudo apt-get update
 sudo apt-get install linux-generic
 ```

3. Download the CUDA .deb file for Linux Ubuntu 14.04 64-bit from: https://developer.nvidia.com/cuda-downloads.
The file will be named something like `cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb`

4. Install CUDA from the .deb file:
 ```bash
 sudo dpkg -i cuda-repo-ubuntu1404-7-5-local_7.5-18_amd64.deb
 sudo apt-get update
 sudo apt-get install cuda
 echo "export PATH=/usr/local/cuda/bin/:\$PATH; export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:\$LD_LIBRARY_PATH; " >>~/.bashrc && source ~/.bashrc
 ```

4. Restart your computer

## Install cuDNN v4
1. Download cuDNN v4 from https://developer.nvidia.com/cuDNN  (requires registration).
  The file will be named something like `cudnn-7.0-linux-x64-v4.0-rc.tgz`.

2. Extract the file to `/usr/local/cuda`:
 ```bash
 tar -xvf cudnn-7.0-linux-x64-v4.0-rc.tgz
 sudo cp cuda/include/*.h /usr/local/cuda/include
 sudo cp cuda/lib64/*.so* /usr/local/cuda/lib64
 ```

## Install Torch
1. Install the Torch dependencies:
  ```bash
  curl -sk https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash -e
  ```

2. Install Torch in a local folder:
  ```bash
  git clone https://github.com/torch/distro.git ~/torch --recursive
  cd ~/torch; ./install.sh
  ```

If you want to uninstall torch, you can use the command: `rm -rf ~/torch`

## Install the Torch cuDNN v4 bindings
```bash
git clone -b R4 https://github.com/soumith/cudnn.torch.git
cd cudnn.torch; luarocks make
```

