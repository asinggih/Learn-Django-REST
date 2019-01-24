# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|    # "2" is the API version

  config.vm.box = "ubuntu/xenial64"   # which image we wanna use for our vm
                                      # It's a good idea to match the OS image with the
                                      # OS on the prod server

  # --------------------------------------------------------
  #                 Network Configuration
  # --------------------------------------------------------
  # 
  # Basically we're just remapping guest OS' ip and port
  # We can change it according to our need
  #
  # Current setting:
  # guest OS IP:8080 --------> TO OUR 127.0.0.1:8080
  #
  config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 8080, host: 8080
  

  # --------------------------------------------------------
  #                 Provisioning Script
  # --------------------------------------------------------
  # 
  # Just some initial scripts to run on our vm image,
  # to prepare the environment for our project
  #
  config.vm.provision "shell", inline: <<-SHELL
    # Update and upgrade the server packages.
    sudo apt-get update
    sudo apt-get -y upgrade
    # Set Ubuntu Language
    sudo locale-gen en_GB.UTF-8
    # Install Python, SQLite and pip
    sudo apt-get install -y python3-dev sqlite python-pip
    # Upgrade pip to the latest version.
    sudo pip install --upgrade pip
    # Install and configure python virtualenvwrapper.
    sudo pip install virtualenvwrapper
    if ! grep -q VIRTUALENV_ALREADY_ADDED /home/vagrant/.bashrc; then
        echo "# VIRTUALENV_ALREADY_ADDED" >> /home/vagrant/.bashrc
        echo "WORKON_HOME=~/.virtualenvs" >> /home/vagrant/.bashrc
        echo "PROJECT_HOME=/vagrant" >> /home/vagrant/.bashrc
        echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.bashrc
    fi
  SHELL

end