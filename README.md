AWS EC installation with your system:
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

Following instuction is done by ubuntu(Linux)

Key pair:
after sign in your account, click service at left top bar, select compute at left bar then click EC2( or just search EC2 on search bar)
under network security -> key pairs 
create a key and download it


Access key:
click your account icon at right top: it shows Account ID, setting, Organization etc...

select security credentials -> scroll download find access key option, create one you need


Note: you may need enter -O -W your access key every command

after you create access key

Confirgure setup

command: aws configure

document:
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html


in Linux follwing Test your environment by running ec2-describe-regions command


ec2-describe-regions -O [access key] -W [secret key]
output be like: 

REGION  ap-south-1      ec2.ap-south-1.amazonaws.com

REGION  eu-north-1      ec2.eu-north-1.amazonaws.com

REGION  eu-west-3       ec2.eu-west-3.amazonaws.com

REGION  eu-west-2       ec2.eu-west-2.amazonaws.com

REGION  eu-west-1       ec2.eu-west-1.amazonaws.com

...


Create instance:
command: ec2-run-instances ami-22ce4934 -O [access key] -W [secret key] -t t2.micro -k [key pair]
-t is instance type, bigger type will cost money -k is key pair


Check instance information:
ec2-describe-regions [instance id] -O [access key] -W [secret key]


ssh into the newly created instance:
chmod 400 [key location]
example: chmod 400 /mnt/c/Users/Owner/Downloads/test1.pem


ssh -i /path/key-pair-name.pem instance-user-name@instance-IPv6-address
example: ssh -i /mnt/c/Users/Owner/Downloads/test1.pem EC2-user1@ec2-18-234-79-69.compute-1.amazonaws.com

//you many need setup username first for your instance

Create image:


ec2-create-image [instance id] -n [a image name] 
this will return an customized ami id, note it down 
example output: ami-06744560fd4ad78ad


Create an instance of this new image and terminate all your instances -- record time of each operation:
 ec2-terminate-instances [instance-id] 
 
 
 Now you can start another instance from your customized AMI!


 ec2-run-instances new-ami-id -k [key] -t [instance type]
 
 example: ec2-run-instances ami-06744560fd4ad78ad -k test1.pem -t t2.micro
 
deregister your newly created AMI by
 ec2-deregister ami-id-here 
 example:  ec2-deregister ami-06744560fd4ad78ad
 
 
 ec2-describe-snapshots | grep ami-06744560fd4ad78ad


example: ec2-describe-snapshots -O AKIAUGLUZ76IJAR3NE5Y -W 80le9Wc3Z5wWBWHS/oAcI2aJMot/mWkwZ4I41Ssd
| grep ami-06744560fd4ad78ad


good video reference:
https://www.youtube.com/watch?v=PWAnY-w1SGQ

