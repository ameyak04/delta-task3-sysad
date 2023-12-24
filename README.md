# delta-task3-sysad
#####Following steps were followed to creat tar file with inputfiles on source Machine######
#in home directory use :-
sudo tar -cvf /tmp/sysAdtask1inputfiles.tar ./inputfiles
################## For Extracting the file on Target Machine Follow following instructions ####
#Please login  user account with Sudo previledges.
sudo -i ( to Root) 
Assuming the home directory of root is /root 
#Please extract tar file 
tar -xvf /tmp/sysAdtask1inputfiles.tar
#The Tar file has all the input files 
/root/inputfiles has all the inputfiles

#######Following steps were followed to creat tar file with scripts on source Machine######
#in home directory use :-
sudo tar -cvf /tmp/sysAdtask1scripts.tar ./scripts
################## For Extracting the file on Target Machine Follow following instructions ####
#Please login  user account with Sudo previledges.
sudo -i ( to Root) 
Assuming the home directory of root is /root 
Please extract tar file 
tar -xvf /tmp/sysAdtask1scripts.tar
#The Tar file has all the scripts
/root/scripts has all the scripts

Similarly store serverscripts, Dockerfile.Sysad.task3.db, Dockerfile.Sysadmtask3myapp and docker-compose-sysadtask3.yaml into /root directory


#####running server docker in the system##########
cp Dockerfile.Sysadmtask3myapp Dockerfile
docker pull ghcr.io/ameyak04/sysadmtask3myapp:latest
docker run -d -t --name task3server ghcr.io/ameyak04/sysadmtask3myapp:latest
##########to go into the root of docker##########
docker exec -it task3server bash

#####running database docker in the system##########
cp Dockerfile.Sysad.task3.db Dockerfile
docker pull ghcr.io/ameyak04/sysadmtask3mydb:latest
docker run -d -t --name mydbcontainer ghcr.io/ameyak04/sysadmtask3mydb:latest
##########to go into the root of docker##########
docker exec -it mydbcontainer bash








