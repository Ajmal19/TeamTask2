#!/usr/bin/python3
print("Content-Type: text/html\n")
print()


import os
import getpass
import speech_recognition


def ask_user():
    user_login = input("Enter where you want to login(local/remote)\n")
    print('''
    Press 1 for aws + partition functionality
    Press 2 for hadoop functionality
    Press 3 for lvm functionality
    Press 4 for docker functionality
    ''')
    user_choice = int(input("Enter your choice\n"))
    if user_choice == 1:
        aws_helper(user_login, user_choice)
    elif user_choice == 2:
        hadoop_helper(user_login, user_choice)

    elif user_choice == 3:
        lvm_helper(user_login, user_choice)
    elif user_choice == 4:
        docker_helper(user_login, user_choice)
    elif user_choice == 0:
        os.system("exit()")
    print(user_choice)
    return user_choice, user_login


def hadoop_helper(user_login, user_choice):
    if user_login == 'local':
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

            """)
            user_input = int(input("Enter the number \n"))
            if user_input == 1:
                os.system("hadoop version")
            elif user_input == 2:
                os.system("java --version")
            elif user_input == 3:
                print("panel is upgrading\n")
                os.system("")
            elif user_input == 4:
                print("panel is upgrading\n")
                os.system("")
            elif user_input == 5:
                print("panel is upgrading\n")
                os.system("")
            elif user_input == 6:
                os.system("hadoop-daemon.sh start namenode")
            elif user_input == 7:
                os.system("hadoop-daemon.sh start datanode")
            elif user_input == 8:
                os.system("hadoop fs -ls / ")
            elif user_input == 9:
                file_name = input("Enter the filre name you want to delete\n")
                os.system("hadoop fs -rm {}".format(file_name))
            elif user_input == 10:
                file_to_put = input("Enter the file name to upload\n")
                os.system("hadoop fs -put {} /".format(file_to_put))
            elif user_input == 11:
                os.system("hadoop namenode -format")
            elif user_input == 0:
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

            """)
            user_input = int(input("Enter the number \n"))
            if user_input == 1:
                os.system("ssh {} hadoop version".format(ip_add))
            elif user_input == 2:
                os.system("ssh {} java --version".format(ip_add))
            elif user_input == 3:
                os.system("")
            elif user_input == 4:
                os.system("")
            elif user_input == 5:
                os.system("")
            elif user_input == 6:
                os.system(
                    "ssh {} hadoop-daemon.sh start namenode".format(ip_add))
            elif user_input == 7:
                os.system(
                    "ssh {} hadoop-daemon.sh start datanode".format(ip_add))
            elif user_input == 8:
                os.system("ssh {} hadoop fs -ls / ".format(ip_add))
            elif user_input == 9:
                file_name = input("Enter the filre name you want to delete\n")
                os.system("ssh {} hadoop fs -rm {}".format(ip_add, file_name))
            elif user_input == 10:
                file_to_put = input("Enter the file name to upload\n")
                os.system(
                    "ssh {} hadoop fs -put {} /".format(ip_add, file_to_put))
            elif user_input == 11:
                os.system("ssh {} hadoop namenode -format".format(ip_add))

            elif user_input == 0:
                os.system("exit")
                break
            input("Enter to continue")


def aws_helper(user_login, user_choice):
    if user_login == "local":
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

                Press 18 to create CDN distribution plz provide origin domain name
                Press 0 to exit
                ''')
            user_input = int(input("Enter your AWS choice\n"))
            if user_input == 1:
                os.system("aws ec2 describe-instances")
            elif user_input == 2:
                os.system("aws ec2 describe-key-pairs")
            elif user_input == 3:
                os.system("aws ec2 describe-security-groups")
            elif user_input == 4:
                key_name = input("enter key name\n")
                os.system(
                    "aws ec2 create-key-pair --key-name {}".format(key_name))
            elif user_input == 5:
                desc = input("Enter the description for security group ")
                grp_name = input("Enter the security group name")
                os.system(
                    "aws ec2 create security-group --description {} --group-name {}".format(desc, grp_name))
            elif user_input == 6:
                ami_id = input("Enter the image to use\n")
                in_type = input("Enter instance type to launch\n")
                key_name = input("Enter the key name to use\n")
                sg_id = input("Enter the security group id \n")
                count = input(
                    "Enter the no of instances you would like to launch\n")
                os.system("aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --count {}".format(
                    ami_id, in_type, key_name, sg_id, count))
            elif user_input == 7:
                ins_id = input("Enter the instances id to terminate \n")
                os.system(
                    "aws ec2 terminate-instances --instance-ids {}".format(ins_id))

            elif user_input == 8:
                os.system("aws ec2 stop start-instances")
            elif user_input == 9:
                os.system("aws ec2 stop start-instances")
            elif user_input == 10:
                b_name = input("Enter bucket name to give ")
                os.system("aws s3 mb s3://{}".format(b_name))
            elif user_input == 11:
                c_dir = input("Enter current dir\n")
                o_dir = input("where you want to send \n")
                os.system("aws s3 sync {} {}".format(c_dir, o_dir))
            elif user_input == 12:
                a_zone = input("Enter the availability zone")
                size = input("Enter the size")
                os.system(
                    "aws ec2 create-volume --availability-zone {} --size {}".format(a_zone, size))
            elif user_input == 13:
                device = input("enter the device name \n")
                vol_id = input("Enter the volume to attach\n")
                i_id = input("Enter the instance id to attach\n")
                os.system(
                    "aws ec2 attach-volume --device {} --volume-id {} instance-id {}".format(device, vol_id, i_id))
            elif user_input == 14:
                path = input("Enter the path of disk to create partition\n")
                os.system("fdisk {}".format(path))
            elif user_input == 15:
                path = input("Enter the path of device to format\n")
                os.system("mkfs.ext4 {}".format(path))
            elif user_input == 16:
                device = input("Enter the path of device to mount\n")
                path = input("Which folder you want to mount to\n")
                os.system("mount {} {}".format(device, path))
            elif user_input == 17:
                path = input("Enter the path of the folder")
                os.system("mkdir {}".format(path))
            elif user_input == 18:
                o_name = input("GIVE the name of origin domain name")
                os.system("aws cloudfront create-distribution {}".format(o_name))
            elif user_input == 0:
                os.system("exit")
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

                Press 18 to create CDN distribution plz provide origin domain name
                Press 0 to exit
                ''')
            user_input = int(input("Enter your AWS choice\n"))
            user_ip = input("Enter the ip")
            if user_input == 1:
                os.system("ssh {}aws ec2 describe-instances".format(user_ip))
            elif user_input == 2:
                os.system("ssh {} aws ec2 describe-key-pairs".format(user_ip))
            elif user_input == 3:
                os.system(
                    "ssh {} aws ec2 describe-security-groups".format(user_ip))
            elif user_input == 4:
                key_name = input("enter key name\n")
                os.system(
                    "ssh {}aws ec2 create-key-pair --key-name {}".format(user_ip, key_name))
            elif user_input == 5:
                desc = input("Enter the description for security group ")
                grp_name = input("Enter the security group name")
                os.system(
                    "ssh {} aws ec2 create security-group --description {} --group-name {}".format(user_ip, desc, grp_name))
            elif user_input == 6:
                ami_id = input("Enter the image to use\n")
                in_type = input("Enter instance type to launch\n")
                key_name = input("Enter the key name to use\n")
                sg_id = input("Enter the security group id \n")
                count = input(
                    "Enter the no of instances you would like to launch\n")
                os.system("ssh {} aws ec2 run-instances --image-id {} --instance-type {} --key-name {} --security-group-ids {} --count {}".format(
                    user_ip, ami_id, in_type, key_name, sg_id, count))
            elif user_input == 7:
                ins_id = input("Enter the instances id to terminate \n")
                os.system(
                    "ssh {} aws ec2 terminate-instances --instance-ids {}".format(user_ip, ins_id))

            elif user_input == 8:
                os.system("ssh {} aws ec2 stop start-instances")
            elif user_input == 9:
                os.system("ssh {} aws ec2 stop start-instances")
            elif user_input == 10:
                b_name = input("Enter bucket name to give ")
                os.system("ssh {} aws s3 mb s3://{}".format(user_ip, b_name))
            elif user_input == 11:
                c_dir = input("Enter current dir\n")
                o_dir = input("where you want to send \n")
                os.system("ssh {} aws s3 sync {} {}".format(
                    user_ip, c_dir, o_dir))
            elif user_input == 12:
                a_zone = input("Enter the availability zone")
                size = input("Enter the size")
                os.system(
                    "ssh {} aws ec2 create-volume --availability-zone {} --size {}".format(user_ip, a_zone, size))
            elif user_input == 13:
                device = input("enter the device name \n")
                vol_id = input("Enter the volume to attach\n")
                i_id = input("Enter the instance id to attach\n")
                os.system("ssh {} aws ec2 attach-volume --device {} --volume-id {} instance-id {}".format(
                    user_ip, device, vol_id, i_id))
            elif user_input == 14:
                path = input("Enter the path of disk to create partition\n")
                os.system("ssh {} fdisk {}".format(user_ip, path))
            elif user_input == 15:
                path = input("Enter the path of device to format\n")
                os.system("ssh {} mkfs.ext4 {}".format(user_ip, path))
            elif user_input == 16:
                device = input("Enter the path of device to mount\n")
                path = input("Which folder you want to mount to\n")
                os.system("ssh {} mount {} {}".format(user_ip, device, path))
            elif user_input == 17:
                path = input("Enter the path of the folder")
                os.system("ssh {} mkdir {}".format(user_ip, path))
            elif user_input == 18:
                o_name = input("GIVE the name of origin domain name")
                os.system(
                    "ssh {} aws cloudfront create-distribution {}".format(user_ip, o_name))
            elif user_input == 0:
                os.system("exit()")
                break
            input("Enter to continue")

# docker


def docker_helper(user_login, user_choice):
    if user_login == 'local':
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
            user_input = int(input("Enter the choice :\n"))
            if user_input == 1:
                os.system("docker info")
            elif user_input == 2:
                os.system("docker images")
            elif user_input == 3:
                os.system("docker ps")
            elif user_input == 4:
                os.system("docker pa -a")
            elif user_input == 5:
                user_inp = input("Enter os name with version")
                os.system("docker run -it {}".format(user_inp))
            elif user_input == 6:
                con_name = input("Enter the conatiner name to be removed")
                os.system("docker rm {}".format(con_name))
            elif user_input == 7:
                img_name = input("Enter image name to be removed")
                os.system("docker rmi {}".format(img_name))
            elif user_input == 8:
                os.system("docker rm `docker ps -q`")
            elif user_input == 9:
                path1 = input("ENter the path of local file ")
                path2 = input(
                    "Enter where you want to copy file with container name(wb1:/root) ")
                os.system("docker cp {} {}".format(path1, path2))
            elif user_input == 10:
                p1 = input("Enter the container path like wb:/root/filename")
                p2 = input("Enter the local path")
                os.system("docker cp {} {}".format(p1, p2))
            elif user_input == 0:
                os.system("exit()")
                break
            input("Enter to continue")
    else:
        user_ip = input("Enter the IP to connect to")
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
            user_input = int(input("Enter the choice :\n"))
            if user_input == 1:
                os.system("ssh {} docker info".format(user_ip))
            elif user_input == 2:
                os.system("ssh {} docker images".format(user_ip))
            elif user_input == 3:
                os.system("ssh {} docker ps".format(user_ip))
            elif user_input == 4:
                os.system("ssh {} docker ps -a".format(user_ip))
            elif user_input == 5:
                user_inp = input("Enter os name with version")
                os.system("ssh {} docker run -i {}".format(user_ip, user_inp))
            elif user_input == 6:
                con_name = input("Enter the conatiner name to be removed")
                os.system("ssh {} docker rm {}".format(user_ip, con_name))
            elif user_input == 7:
                img_name = input("Enter image name to be removed")
                os.system("ssh {} docker rmi {}".format(user_ip, img_name))
            elif user_input == 8:
                os.system("ssh {} docker rm `docker ps -q`".format(user_ip))
            elif user_input == 9:
                path1 = input("ENter the path of local file ")
                path2 = input(
                    "Enter where you want to copy file with container name(wb1:/root) ")
                os.system("ssh {} docker cp {} {}".format(
                    user_ip, path1, path2))
            elif user_input == 10:
                p1 = input("Enter the container path like wb:/root/filename")
                p2 = input("Enter the local path")
                os.system("ssh {} docker cp {} {}".format(user_ip, p1, p2))
            elif user_input == 0:

                os.system("exit()")
                break

            input("Enter to continue")


# login = input("Where you want to login(local or remote)\n")


def lvm_helper(user_login, user_choice):
    if user_login == 'local':
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

            ch = int(input("Enter your choice "))
            print(ch)
            if ch == 1:
                os.system("cal")
            elif ch == 2:
                os.system("date")
            elif ch == 3:
                os.system("df -h")
            elif ch == 4:
                os.system("fdisk -l")
            elif ch == 5:
                pv = input("Enter pv name ")
                os.system("pvcreate {}".format(pv))

            elif ch == 6:
                pv = input("Enter pv name ")
                os.system("pvdisplay {}".format(pv))

            elif ch == 7:
                vg = input("Enter the volume group name")
                pv1 = input("Enter the physical volume  name")
                pv2 = input("Enter the physical volume  name")
                os.system("vgcreate {} {} {}".format(vg, pv1, pv2))

            elif ch == 8:
                vg = input("Enter the volume group name")

                os.system("vgdisplay {}".format(vg))

            elif ch == 9:
                size = input("Enter the size")
                name = input("Enter the name")
                vg = input("Enter the vg created")
                os.system(
                    "lvcreate --size {} --name {} {}".format(size, name, vg))

            elif ch == 10:
                name = input("Enter the LV name(vg/lv)")
                os.system("lvdisplay {}".format(name))

            elif ch == 11:
                name = input(
                    """Enter the path of logical volume to format(/dev/vg/lv)""")
                os.system("mkfs/ext4 {}".format(name))

            elif ch == 12:
                mdir = input("Enter the dir name ")
                name = input(
                    """Enter the path of logical volume to format(/dev/vg/lv)""")
                os.system("mount {} {}".format(name, mdir))

            elif ch == 13:
                size = input("Enter size to extend eg +5G")
                path = input("ENter the lv path (/dev/vg/lv)")
                os.system("lvextend --size {} {}".format(size, path))

            elif ch == 14:
                name = input("Enter the name for lv to resize(/dev/vg/lv)")
                os.system("resize2fs {}".format(name))

            elif ch == 15:
                name = input("Enter the name of vg")
                hd = input("ENter the name of new hd")

                os.system("vgextend {} {}".format(name, hd))

            elif ch == 0:
                exit()
                break
            input("Press enter to continue")
    else:
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

            ch = int(input("Enter your choice "))
            user_ip = input("Enter the ip to connect")
            print(ch)
            if ch == 1:
                os.system("ssh {} cal".format(user_ip))
            elif ch == 2:
                os.system("ssh {} date".format(user_ip))
            elif ch == 3:
                os.system("ssh {} df -h".format(user_ip))
            elif ch == 4:
                os.system("ssh {} fdisk -l".format(user_ip))
            elif ch == 5:
                pv = input("Enter pv name ")
                os.system("ssh {} pvcreate {}".format(user_ip, pv))

            elif ch == 6:
                pv = input("Enter pv name ")
                os.system("ssh {} pvdisplay {}".format(user_ip, pv))

            elif ch == 7:
                vg = input("Enter the volume group name")
                pv1 = input("Enter the physical volume  name")
                pv2 = input("Enter the physical volume  name")
                os.system("ssh {} vgcreate {} {} {}".format(
                    user_ip, vg, pv1, pv2))

            elif ch == 8:
                vg = input("Enter the volume group name")
                os.system("ssh {} vgdisplay {}".format(user_ip, vg))

            elif ch == 9:
                size = input("Enter the size")
                name = input("Enter the name")
                vg = input("Enter the vg created")
                os.system(
                    "ssh {} lvcreate --size {} --name {} {}".format(user_ip, size, name, vg))

            elif ch == 10:
                name = input("Enter the LV name(vg/lv)")
                os.system("ssh {} lvdisplay {}".format(user_ip, name))

            elif ch == 11:
                name = input(
                    """Enter the path of logical volume to format(/dev/vg/lv)""")
                os.system("ssh {} mkfs/ext4 {}".format(user_ip, name))

            elif ch == 12:
                mdir = input("Enter the dir name ")
                name = input(
                    """Enter the path of logical volume to format(/dev/vg/lv)""")
                os.system("ssh {} mount {} {}".format(user_ip, name, mdir))

            elif ch == 13:
                size = input("Enter size to extend eg +5G")
                path = input("ENter the lv path (/dev/vg/lv)")
                os.system(
                    "ssh {} lvextend --size {} {}".format(user_ip, size, path))

            elif ch == 14:
                name = input("Enter the name for lv to resize(/dev/vg/lv)")
                os.system("ssh {} resize2fs {}".format(user_ip, name))

            elif ch == 15:
                name = input("Enter the name of vg")
                hd = input("ENter the name of new hd")

                os.system("ssh {} vgextend {} {}".format(user_ip, name, hd))

            elif ch == 0:
                break
            input("press enter to continue")


#######################################################################
#######################################################################
#######################################################################
# main
print("\t\t\tWelcome to my menu")

passwd = getpass.getpass("Enter the password to continue\n")
if passwd != 'lala':
    exit()
while True:
    user_choice, user_login = ask_user()
    exi = input("do youyb want to exit from the program :type (yes/no)")
    if exi == 'yes':
        break
