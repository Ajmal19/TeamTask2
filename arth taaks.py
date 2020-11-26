import webbrowser
import subprocess
import getpass
import os
import speech_recognition as sr
# /usr/bin/python3
# print("content-type:text/html")
# print()


def user_audio():
    model = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Start saying")
        audio = model.listen(source)
        print("Processing")

    user_choice = model.recognize_google(audio)
    print(user_choice)
    return user_choice


def ask_user():
    print("Where do you want to login (local/remote)")
    user_login = user_audio()
    print("1st voice check")

    print('''
    aws + partition functionality
    hadoop functionality
    lvm functionality
    docker functionality
    set webser using ansible
    quit
    ''')
    print("check1")
    user_choice = user_audio()
    user_choice = user_choice.lower()
    if "aws" in user_choice or "partition" in user_choice:
        aws_helper(user_login, user_choice)
    elif "hadoop" in user_choice:
        hadoop_helper(user_login, user_choice)

    elif "lvm" in user_choice:
        lvm_helper(user_login, user_choice)
    elif "docker" in user_choice:
        docker_helper(user_login, user_choice)
    elif "webser" in user_choice or "ansible" in user_choice:
        webserver(user_login, user_choice)
    elif "quit" in user_choice or "exit" in user_choice:
        os.system("exit()")
        # break
    else:
        print("We are unable to understand")
    return user_choice, user_login


def webserver(user_login, user_choice):
    if "local" in user_login:
        while True:
            print("""
            check version
            Press 2 to list all hosts
            press 3 to ping all  the hosts
            press 4 to install web server
            press 5 to copy pages to document root
            press 6 to start services
            press 0 to exit
            """)
            # user_choice == input("Enter your choice")
            user_choice = user_audio()
            if "version" in user_choice:
                print("check2")
                os.system("ansible --version")
            elif 'list' in user_choice and "hosts" in user_choice:
                os.system("ansible all --list-hosts")
            elif "ping" in user_choice and "hosts" in user_choice:
                os.system("ansible all -m ping")
            elif "install" in user_choice and "web" in user_choice and "server" in user_choice:
                os.system('ansible all -m package -a "name=httpd state=present"')
            elif "copy" in user_choice and "pages" in user_choice:
                src = input("enter the destination folder")
                dist = input("enter the destination folder")
                os.system(
                    "ansible all -m copy -a 'src={} dest={}'".format(src, dist))
            elif ("start" in user_choice or "execute" in user_choice) and "services" in user_choice:
                os.system('ansible all -m service -a "name=httpd state=running"')
            elif "exit" in user_choice and "quit" in user_choice:
                exit()
                break
            input("Press enter to continue")
    elif 'remote' in user_login:
        while True:
            print("""
            Press 1 to check version
            Press 2 to list all hosts
            press 3 to ping all  the hosts
            press 4 to install web server
            press 5 to copy pages to document root
            press 6 to start services
            quit this fuctionality
            """)
            # user_choice == input("Enter your choice")
            user_choice = user_audio()
            if "version" in user_choice:
                os.system("ansible --version")
            elif 'list' in user_choice and "hosts" in user_choice:
                os.system("ansible all --list-hosts")
            elif "ping" in user_choice and "hosts" in user_choice:
                os.system("ansible all -m ping")
            elif "install" in user_choice and "web" in user_choice and "server" in user_choice:
                os.system('ansible all -m package -a "name=httpd state=present"')
            elif ("start" in user_choice or "execute" in user_choice) and "services" in user_choice:
                os.system('ansible all -m service -a "name=httpd state=running"')
            elif "exit" in user_choice:
                os.system("exit()")
                break
            input("Press enter to continue")
    else:
        print("Kindly try again")


def hadoop_helper(user_login, user_choice):
    if 'local' in user_login:
        while True:
            print("""
            Press 1 to check hadoop version
            Press 2 to check java version
            Press 3 to configure hdfs file
            Press 4 to configure core file
            Press 5 to configure client core file
            Press 6 to start master services
            Press 7 to start slave services
            Press 8 to view all files on the cluster
            Press 9 to remove a file on the cluster
            Press 10 to upload a files to cluster
            Press 11 to format the namenode
            exit
            """)
            # user_input = int(input("Enter the number \n"))
            user_choice = user_audio()
            if "version" in user_choice or "hadoop" in user_choice:
                os.system("hadoop version")
            elif "java" in user_choice or "version" in user_choice:
                os.system("java --version")
            elif "configure" in user_choice and "hdfs" in user_choice:
                print("panel is upgrading\n")
                os.system("")
            elif "configure" in user_choice and "core" in user_choice:
                print("panel is upgrading\n")
                os.system("")
            elif "configure" in user_choice and "client" in user_choice and "core" in user_choice:
                print("panel is upgrading\n")
                os.system("")
            elif "start" in user_choice and "master" in user_choice and "services" in user_choice:
                os.system("hadoop-daemon.sh start namenode")
            elif "start" in user_choice and "slave" in user_choice and "services" in user_choice:
                os.system("hadoop-daemon.sh start datanode")
            elif ("view" in user_choice and "files" in user_choice) or "all" in user_choice:
                os.system("hadoop fs -ls / ")
            elif "remove" in user_choice and "file" in user_choice:
                file_name = input("Enter the filre name you want to delete\n")
                os.system("hadoop fs -rm {}".format(file_name))
            elif "upload" in user_choice and "file" in user_choice:
                file_to_put = input("Enter the file name to upload\n")
                os.system("hadoop fs -put {} /".format(file_to_put))
            elif ("namenode" in user_choice or "master" in user_choice) and "format" in user_choice:
                os.system("hadoop namenode -format")
            elif "exit" in user_choice:
                os.system("exit()")
                break
            input("Enter to continue")
    else:
        ip_add = input("Plz provide the ip address\n")
        while True:
            print("""
            Press 1 to check hadoop version
            Press 2 to check java version
            Press 3 to configure hdfs file
            Press 4 to configure core file
            Press 5 to configure client core file
            Press 6 to start master services
            Press 7 to start slave services
            Press 8 to view all files on the cluster
            Press 9 to remove a file on the cluster
            Press 10 to upload a files to cluster
            Press 11 to format the namenode
            12 quit the functionality

            """)
            # user_input = int(input("Enter the number \n"))
            user_input = user_audio()
            if ("check" in user_input) and (("hadoop" in user_input) and ("version" in user_input)):
                os.system("ssh {} hadoop version".format(ip_add))
            elif (("check" in user_input) and (("java" in user_input) and ("version" in user_input))):
                os.system("ssh {} java --version".format(ip_add))
            elif ("configure" in user_input and ("hdfs" in user_input) and ("file" in user_input) and ("master" in user_input)):
                os.system("")
            elif ("configure" in user_input) and ("core" in user_input) and ("file" in user_input) and ("master" in user_input):
                os.system("")
            elif ("configure" in user_input) and ("client" in user_input) and ("file" in user_input):
                os.system("")
            elif ("start" in user_input) and ("master" in user_input) and ("services" in user_input):
                os.system(
                    "ssh {} hadoop-daemon.sh start namenode".format(ip_add))
            elif ("start" in user_input) and ("slave" in user_input) and ("services" in user_input):
                os.system(
                    "ssh {} hadoop-daemon.sh start datanode".format(ip_add))
            elif ("view" in user_input) and ("all" in user_input) and ("files" in user_input):
                os.system("ssh {} hadoop fs -ls / ".format(ip_add))
            elif ("file" in user_input) and ("remove" in user_input):
                file_name = input("Enter the filre name you want to delete\n")
                os.system("ssh {} hadoop fs -rm {}".format(ip_add, file_name))
            elif ("upload" in user_input) and ("file" in user_input):
                file_to_put = input("Enter the file name to upload\n")
                os.system(
                    "ssh {} hadoop fs -put {} /".format(ip_add, file_to_put))
            elif ("format" in user_input) and (("namenode" in user_input) or ("master" in user_input)):
                os.system("ssh {} hadoop namenode -format".format(ip_add))

            elif ("exit" in user_input) or ("quit" in user_input):
                os.system("exit()")
                break
            input("Enter to continue")


def aws_helper(user_login, user_choice):
    if 'local' in user_login:
        while True:
            print('''
                Press 1 to describe all instances
                press 2 to describe all key pairs
                press 3 to describe all the security groups
                press 4 to create key pair
                press 5 to create security group
                press 6 to launch a new instances
                press 7 to terminate instances
                press 8 to stop instanecs
                press 9 to run instances

                Press 10 to make a new bucket in s3
                press 11 to copy file to s3 bucket

                Press 12 to create a new EBS volume
                Press 13 to attach the EBS volume to EC2 instances
                Press 14 to create partition
                press 15 to format partition
                press 16 to mount partition
                press 17 to create mount folder

                Press 18 to create CDN distribution (plz provide origin domain name)
                Press 0 to exit
                ''')
            # user_input = int(input("Enter your AWS choice\n"))
            user_input = user_audio()
            if ("describe" in user_input) and ("instances" in user_input):
                os.system("aws ec2 describe-instances")
            elif ("describe" in user_input) and ("key" in user_input) and ("pairs" in user_input):
                os.system("aws ec2 describe-key-pairs")
            elif ("describe" in user_input) and ("security" in user_input) and ("groups" in user_input):
                os.system("aws ec2 describe-security-groups")
            elif ("create" in user_input) and ("key" in user_input) and ("pair" in user_input):
                key_name = input("enter key name\n")
                os.system(
                    "aws ec2 create-key-pair --key-name {}".format(key_name))
            elif ("create" in user_input) and ("security" in user_input) and ("group" in user_input):
                desc = input("Enter the description for security group ")
                grp_name = input("Enter the security group name")
                os.system(
                    "aws ec2 create security-group --description {} --group-name {}".format(desc, grp_name))
            elif ("create" in user_input) and ("ec2" in user_input) and ("instances" in user_input):
                ami_id = input("Enter the image to use\n")
                in_type = input("Enter instance type to launch\n")
                key_name = input("Enter the key name to use\n")
                sg_id = input("Enter the security group id \n")
                count = input(
                    "Enter the no of instances you would like to launch\n")
                os.system("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --count {}".format(
                    ami_id, in_type, key_name, sg_id, count))
            elif ("terminate" in user_input) and ("instance" in user_input):
                ins_id = input("Enter the instances id to terminate \n")
                os.system(
                    "aws ec2 terminate-instances --instance-ids {}".format(ins_id))

            elif ("start" in user_input) and ("instances" in user_input):
                id1 = input("Enter instance id to be started")
                os.system(
                    "aws ec2  start-instances --instance-ids {}".format(id1))
            elif ("stop" in user_input) and ("instances" in user_input):
                id1 = input("Enter the id to be stopped")
                os.system(
                    "aws ec2 stop start-instances --instances-ids {}".format(id1))
            elif (("make" in user_input) or ("create" in user_input)) and ("bucket" in user_input):
                b_name = input("Enter bucket name to give ")
                os.system("aws s3 mb s3://{}".format(b_name))
            elif ("copy" in user_input) and ("file" in user_input) and ("buket" in user_input):
                c_dir = input("Enter current dir\n")
                o_dir = input("where you want to send \n")
                os.system("aws s3 sync {} {}".format(c_dir, o_dir))
            elif ("create" in user_input) and ("ebs" in user_input) and ("volume" in user_input):
                a_zone = input("Enter the availability zone")
                size = input("Enter the size")
                os.system(
                    "aws ec2 create-volume --availability-zone {} --size {}".format(a_zone, size))
            elif ("attach" in user_input) and ("volume" in user_input) and ("ec2" in user_input):
                device = input("enter the device name \n")
                vol_id = input("Enter the volume to attach\n")
                i_id = input("Enter the instance id to attach\n")
                os.system(
                    "aws ec2 attach-volume --device {} --volume-id {} instance-id {}".format(device, vol_id, i_id))
            elif (("make " in user_input) or ("create" in user_input)) and ("partition" in user_input):
                path = input("Enter the path of disk to create partition\n")
                os.system("fdisk {}".format(path))
            elif ("format" in user_input) and ("partition" in user_input):
                path = input("Enter the path of device to format\n")
                os.system("mkfs.ext4 {}".format(path))
            elif ("mount" in user_input) and ("partiton" in user_input):
                device = input("Enter the path of device to mount\n")
                path = input("Which folder you want to mount to\n")
                os.system("mount {} {}".format(device, path))
            elif ("create" in user_input) and ("mount" in user_input) and ("folder" in user_input):
                path = input("Enter the path of the folder")
                os.system("mkdir {}".format(path))
            elif ("create" in user_input) and ("cdn" in user_input) and ("distribution" in user_input):
                o_name = input("GIVE the name of origin domain name")
                os.system("aws cloudfront create-distribution {}".format(o_name))
            elif ("exit" in user_input) or ("quit" in user_input):
                os.system("exit()")
                break
            input("Enter to continue")
    else:
        while True:
            print('''
                Press 1 to describe all instances
                press 2 to describe all key pairs
                press 3 to describe all the security groups
                press 4 to create key pair
                press 5 to create security group
                press 6 to launch a new instances
                press 7 to terminate instances
                press 8 to stop instanecs
                press 9 to run instances

                Press 10 to make a new bucket in s3
                press 11 to copy file to s3 bucket

                Press 12 to create a new EBS volume
                Press 13 to attach the EBS volume to EC2 instances
                Press 14 to create partition
                press 15 to format partition
                press 16 to mount partition
                press 17 to create mount folder

                Press 18 to create CDN distribution (plz provide origin domain name)
                Press 0 to exit
                ''')
            # user_input = int(input("Enter your AWS choice\n"))
            user_input = user_audio()
            if ("describe" in user_input) and ("instances" in user_input):
                os.system("aws ec2 describe-instances")
            elif ("describe" in user_input) and ("key" in user_input) and ("pairs" in user_input):
                os.system("aws ec2 describe-key-pairs")
            elif ("describe" in user_input) and ("security" in user_input) and ("groups" in user_input):
                os.system("aws ec2 describe-security-groups")
            elif ("create" in user_input) and ("key" in user_input) and ("pair" in user_input):
                key_name = input("enter key name\n")
                os.system(
                    "aws ec2 create-key-pair --key-name {}".format(key_name))
            elif ("create" in user_input) and ("security" in user_input) and ("group" in user_input):
                desc = input("Enter the description for security group ")
                grp_name = input("Enter the security group name")
                os.system(
                    "aws ec2 create security-group --description {} --group-name {}".format(desc, grp_name))
            elif ("create" in user_input) and ("ec2" in user_input) and ("instances" in user_input):
                ami_id = input("Enter the image to use\n")
                in_type = input("Enter instance type to launch\n")
                key_name = input("Enter the key name to use\n")
                sg_id = input("Enter the security group id \n")
                count = input(
                    "Enter the no of instances you would like to launch\n")
                os.system("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --count {}".format(
                    ami_id, in_type, key_name, sg_id, count))
            elif ("terminate" in user_input) and ("instance" in user_input):
                ins_id = input("Enter the instances id to terminate \n")
                os.system(
                    "aws ec2 terminate-instances --instance-ids {}".format(ins_id))

            elif ("start" in user_input) and ("instances" in user_input):
                id1 = input("Enter instance id to be started")
                os.system(
                    "aws ec2  start-instances --instance-ids {}".format(id1))
            elif ("stop" in user_input) and ("instances" in user_input):
                id1 = input("Enter the id to be stopped")
                os.system(
                    "aws ec2 stop start-instances --instances-ids {}".format(id1))
            elif (("make" in user_input) or ("create" in user_input)) and ("bucket" in user_input):
                b_name = input("Enter bucket name to give ")
                os.system("aws s3 mb s3://{}".format(b_name))
            elif ("copy" in user_input) and ("file" in user_input) and ("buket" in user_input):
                c_dir = input("Enter current dir\n")
                o_dir = input("where you want to send \n")
                os.system("aws s3 sync {} {}".format(c_dir, o_dir))
            elif ("create" in user_input) and ("ebs" in user_input) and ("volume" in user_input):
                a_zone = input("Enter the availability zone")
                size = input("Enter the size")
                os.system(
                    "aws ec2 create-volume --availability-zone {} --size {}".format(a_zone, size))
            elif ("attach" in user_input) and ("volume" in user_input) and ("ec2" in user_input):
                device = input("enter the device name \n")
                vol_id = input("Enter the volume to attach\n")
                i_id = input("Enter the instance id to attach\n")
                os.system(
                    "aws ec2 attach-volume --device {} --volume-id {} instance-id {}".format(device, vol_id, i_id))
            elif (("make " in user_input) or ("create" in user_input)) and ("partition" in user_input):
                path = input("Enter the path of disk to create partition\n")
                os.system("fdisk {}".format(path))
            elif ("format" in user_input) and ("partition" in user_input):
                path = input("Enter the path of device to format\n")
                os.system("mkfs.ext4 {}".format(path))
            elif ("mount" in user_input) and ("partiton" in user_input):
                device = input("Enter the path of device to mount\n")
                path = input("Which folder you want to mount to\n")
                os.system("mount {} {}".format(device, path))
            elif ("create" in user_input) and ("mount" in user_input) and ("folder" in user_input):
                path = input("Enter the path of the folder")
                os.system("mkdir {}".format(path))
            elif ("create" in user_input) and ("cdn" in user_input) and ("distribution" in user_input):
                o_name = input("GIVE the name of origin domain name")
                os.system("aws cloudfront create-distribution {}".format(o_name))
            elif ("exit" in user_input) or ("quit" in user_input):
                os.system("exit()")
                break
            input("Enter to continue")


def docker_helper(user_login, user_choice):
    if 'local' in user_login:
        print("docker check")
        while True:
            print('''
                Press 1 to know docker system info
                Press 2 to know images
                Press 3 to know running images
                Press 4 to know all containers
                Press 5 to launch a container
                Press 6 to remove the container
                Press 7 to remove the image
                Press 8 to remove all containers
                Press 9 to copy a local file to conatiner
                Press 10 to copy from conatiner to local system
                Press 0 to quit
                ''')
            # user_input = int(input("Enter the choice :\n"))
            user_input = user_audio()
            if "docker" in user_input and "info" in user_input:
                os.system("docker info")
            elif "images" in user_input:
                os.system("docker images")
            elif "running" in user_input and "images" in user_input:
                os.system("docker ps")
            elif "know" in user_input and "container" in user_input:
                os.system("docker pa -a")
            elif ("launch" in user_input or "create" in user_input) and "container" in user_input:
                user_inp = input("Enter os name with version")
                os.system("docker run -it {}".format(user_inp))
            elif "remove" in user_input and "container" in user_input:
                con_name = input("Enter the conatiner name to be removed")
                os.system("docker rm {}".format(con_name))
            elif "remove" in user_input and "images" in user_input:
                img_name = input("Enter image name to be removed")
                os.system("docker rmi {}".format(img_name))
            elif "remove" in user_input and "all" in user_input and "container" in user_input:
                os.system("docker rm `docker ps -q`")
            elif "copy" in user_input and "local" in user_input and "file" in user_input and "container" in user_input:
                path1 = input("ENter the path of local file ")
                path2 = input(
                    "Enter where you want to copy file with container name(wb1:/root) ")
                os.system("docker cp {} {}".format(path1, path2))
            elif "copy" in user_input and "from container" in user_input and "local " in user_input:
                p1 = input("Enter the container path like wb:/root/filename")
                p2 = input("Enter the local path")
                os.system("docker cp {} {}".format(p1, p2))
            elif "exit " in user_input and "quit " in user_input:
                os.system("exit()")
                break
            input("Enter to continue")
    else:
        user_ip = user_audio()
        while True:
            print('''
                Press 1 to know docker system info
                Press 2 to know images
                Press 3 to know running images
                Press 4 to know all containers
                Press 5 to launch a container
                Press 6 to remove the container
                Press 7 to remove the image
                Press 8 to remove all containers
                Press 9 to copy a local file to conatiner
                Press 10 to copy from conatiner to local system
                Press 0 to quit
                ''')
            user_input = user_audio()
            if "docker" in user_input and "info" in user_input:
                os.system("ssh {} docker info".format(user_ip))
            elif "images" in user_input:
                os.system("ssh {} docker images".format(user_ip))
            elif "running" in user_input and "images" in user_input:
                os.system("ssh {} docker ps".format(user_ip))
            elif "all" in user_input and "containers" in user_input:
                os.system("ssh {} docker pa -a".format(user_ip))
            elif "launch" in user_input and "container" in user_input:
                user_inp = input("Enter os name with version")
                os.system("ssh {} docker run -it {}".format(user_ip, user_inp))
            elif "remove" in user_input and "container" in user_input:
                con_name = input("Enter the conatiner name to be removed")
                os.system("ssh {} docker rm {}".format(user_ip, con_name))
            elif "remove" in user_input and "images" in user_input:
                img_name = input("Enter image name to be removed")
                os.system("ssh {} docker rmi {}".format(user_ip, img_name))
            elif "remove" in user_input and "all container" in user_input:
                os.system("ssh {} docker rm `docker ps -q`".format(user_ip))
            elif "copy" in user_input and "from local" in user_input and "container" in user_input:
                path1 = input("ENter the path of local file ")
                path2 = input(
                    "Enter where you want to copy file with container name(wb1:/root) ")
                os.system("ssh {} docker cp {} {}".format(
                    user_ip, path1, path2))
            elif "copy" in user_input and "from container" in user_input and "local" in user_input:
                p1 = input("Enter the container path like wb:/root/filename")
                p2 = input("Enter the local path")
                os.system("ssh {} docker cp {} {}".format(user_ip, p1, p2))
            elif "quit" in user_input and "exit" in user_input:
                os.system("exit()")
                break
            input("Enter to continue")


def lvm_helper(user_login, user_choice):
    if "local" in user_login:
        while True:
            # if login == 'local'
            print(""" We support following option
                Press 1 for cal command
                Press 2 for date command
                Press 3 for df - h command
                Press 4 for fdisk -l command
                Press 5 To create a physical volume
                Press 6 To confirm the Physical volume
                Press 7 to craete a volume group
                Press 8 to display volume group
                Press 9 to create a logical volume
                Press 10 to display logical volume
                Press 11 to format the logical volume
                Press 12 to mount the logical volume
                Press 13 to extend the logical volume size
                Press 14 to resize the partition
                Press 15 to extend vg
                Press 0 to quit

                        """)

            # ch = int(input("Enter your choice "))
            ch = user_audio()
            print(ch)
            if ("run" in ch or "execute" in ch) and "cal" in ch:
                os.system("cal")
            elif ("run" in ch or "execute" in ch) and "date" in ch:
                os.system("date")
            elif ("run" in ch or "execute" in ch) and "df -h" in ch:
                os.system("df -h")
            elif ("run" in ch or "execute" in ch) and "fdisk -l" in ch:
                os.system("fdisk -l")
            elif ("create" in ch or "make" in ch) and ("pv" in ch or ("physical" in ch and "volume" in ch)):
                pv = input("Enter pv name ")
                os.system("pvcreate {}".format(pv))

            elif "display" in ch and ("physical" in ch and "volume" in ch) or "pv" in ch:
                pv = input("Enter pv name ")
                os.system("pvdisplay {}".format(pv))

            elif "create" in ch and ("volume" in ch and "group" in ch) or ("pv" in ch):
                vg = input("Enter the volume group name")
                pv1 = input("Enter the physical volume  name")
                pv2 = input("Enter the physical volume  name")
                os.system("vgcreate {} {} {}".format(vg, pv1, pv2))

            elif "display" in ch and "volume" in ch and "group" in ch:
                vg = input("Enter the volume group name")

                os.system("vgdisplay {}".format(vg))

            elif "create" in ch and "logical" in ch and "volume" in ch:
                size = input("Enter the size")
                name = input("Enter the name")
                vg = input("Enter the vg created")
                os.system(
                    "lvcreate --size {} --name {} {}".format(size, name, vg))

            elif "display" in ch and "logical" in ch and "volume" in ch:
                name = input("Enter the LV name(vg/lv)")
                os.system("lvdisplay {}".format(name))

            elif "format" in ch and "logical" in ch and "volume" in ch:
                name = input(
                    """Enter the path of logical volume to format(/dev/vg/lv)""")
                os.system("mkfs/ext4 {}".format(name))

            elif "mount" in ch and "logical" in ch and "volume" in ch:
                mdir = input("Enter the dir name ")
                name = input(
                    """Enter the path of logical volume to format(/dev/vg/lv)""")
                os.system("mount {} {}".format(name, mdir))

            elif "extend" in ch and "logical" in ch and "volume" in ch and "size" in ch:
                size = input("Enter size to extend eg +5G")
                path = input("ENter the lv path (/dev/vg/lv)")
                os.system("lvextend --size {} {}".format(size, path))

            elif "resize" in ch and "partition" in ch:
                name = input("Enter the name for lv to resize(/dev/vg/lv)")
                os.system("resize2fs {}".format(name))

            elif "extend" in ch and "volume" in ch and "group" in ch:
                name = input("Enter the name of vg")
                hd = input("ENter the name of new hd")

                os.system("vgextend {} {}".format(name, hd))

            elif "quit" in ch and "exit" in ch:
                os.system("exit()")
                break

            input("Press enter to continue")
    else:
        while True:

            print(""" We support following option
                Press 1 for cal command
                Press 2 for date command
                Press 3 for df - h command
                Press 4 for fdisk -l command
                Press 5 To create a physical volume
                Press 6 To confirm the Physical volume
                Press 7 to create a volume group
                Press 8 to display volume group
                Press 9 to create a logical volume
                Press 10 to display logical volume
                Press 11 to format the logical volume
                Press 12 to mount the logical volume
                Press 13 to extend the logical volume size
                Press 14 to resize the partition
                Press 15 to extend vg
                Press 0 to quit

                        """)

            ch = user_audio()
            # ch = int(input("Enter your choice "))
            user_ip = input("Enter the ip to connect")
            print(ch)
            if ("run" in ch or "execute" in ch) and "cal" in ch:
                os.system("ssh {} cal".format(user_ip))
            elif ("run" in ch or "execute" in ch) and "date" in ch:
                os.system("ssh {} date".format(user_ip))
            elif ("run" in ch or "execute" in ch) and "df -h" in ch:
                os.system("ssh {} df -h".format(user_ip))
            elif ("run" in ch or "execute" in ch) and "fdisk -l" in ch:
                os.system("ssh {} fdisk -l".format(user_ip))
            elif ("create" in ch or "make" in ch) and ("pv" in ch or ("physical" in ch and "volume" in ch)):
                pv = input("Enter pv name ")
                os.system("ssh {} pvcreate {}".format(user_ip, pv))

            elif "display" in user_input and ("pv" in user_input or "physical volume" in user_input):
                pv = input("Enter pv name ")
                os.system("ssh {} pvdisplay {}".format(user_ip, pv))

            elif "create" in user_input and "volume group" in user_input:
                vg = input("Enter the volume group name")
                pv1 = input("Enter the physical volume  name")
                pv2 = input("Enter the physical volume  name")
                os.system("ssh {} vgcreate {} {} {}".format(
                    user_ip, vg, pv1, pv2))

            elif "display" in user_input and "volume group" in user_input:
                vg = input("Enter the volume group name")
                os.system("ssh {} vgdisplay {}".format(user_ip, vg))

            elif "create" in user_input and ("logical volume" in user_input and "lv" in user_input):
                size = input("Enter the size")
                name = input("Enter the name")
                vg = input("Enter the vg created")
                os.system(
                    "ssh {} lvcreate --size {} --name {} {}".format(user_ip, size, name, vg))

            elif "display" in user_input and ("lv" in user_input and "logical volume" in user_input):
                name = input("Enter the LV name(vg/lv)")
                os.system("ssh {} lvdisplay {}".format(user_ip, name))

            elif "format" in user_input and ("logical volume" in user_input or "lv" in user_input):
                name = input(
                    """Enter the path of logical volume to format(/dev/vg/lv)""")
                os.system("ssh {} mkfs/ext4 {}".format(user_ip, name))

            elif "mount" in user_input and "logical volume" in user_input:
                mdir = input("Enter the dir name ")
                name = input(
                    """Enter the path of logical volume to format(/dev/vg/lv)""")
                os.system("ssh {} mount {} {}".format(user_ip, name, mdir))

            elif "extend" in user_input and "logical volume" in user_input and "size" in user_input:
                size = input("Enter size to extend eg +5G")
                path = input("ENter the lv path (/dev/vg/lv)")
                os.system(
                    "ssh {} lvextend --size {} {}".format(user_ip, size, path))

            elif "resize" in user_input and "partition" in user_input:
                name = input("Enter the name for lv to resize(/dev/vg/lv)")
                os.system("ssh {} resize2fs {}".format(user_ip, name))

            elif "extend" in user_input and "volume group" in user_input:
                name = input("Enter the name of vg")
                hd = input("ENter the name of new hd")

                os.system("ssh {} vgextend {} {}".format(user_ip, name, hd))

            elif "exit" in user_input and "quit" in user_input:
                os.system("exit()")

                break
            input("Press enter to continue")


#######################################################################
#######################################################################
#######################################################################
# main
os.system("tput setaf 7")
print("\t\t\tWelcome to my menu")

passwd = getpass.getpass("Enter the password to continue\n")
if passwd != 'lala':
    exit()
model = sr.Recognizer()
while True:
    user_choice, user_login = ask_user()

print("do you want to exit from the main proram?")
user_input = user_audio()
if 'yes' in user_input:
    exit
else:
    ask_user()
