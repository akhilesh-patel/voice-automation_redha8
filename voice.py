import os
import pyttsx3
import getpass
import subprocess as sp
import webbrowser as wb
import speech_recognition as sr



x = "0"



print()
print("\t\t\t\t\t\t\t  --------------------- ")
print("\t\t\t\t\t\t\t  WELCOME TO RATHI MENU \t\t")
print("\t\t\t\t\t\t\t  --------------------- ")
pyttsx3.speak("\n\n\n Welcome to RATHI Menu \n\n\n")
pyttsx3.speak("\n\n Now Please enter your password ")


passwd = getpass.getpass("Enter your Password : ")
if passwd != "lw":
    print("password id incorrect...")
    exit()


while (True):
    print()
    print("""
     --------------------------------------------------------------------------
    |                            Rathi Menu Choice                             |  
     --------------------------------------------------------------------------
          --------------------                    ---------------------
         | 1. Using MENU Card |                  | 2. Using OWN CMD    | 
          --------------------                    ---------------------
                             -----------------------
                            |  3. Terminate Program |
                             -----------------------
    """)
    print("\n\n")
    print("Enter your requirements .....we r listiening ...." , end='')
    pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
    #r = sr.Recognizer()
    #with sr.Microphone() as source:
    #    print("\nstart saying...")
    #    audio = r.listen(source)
    #    print("wait we got it")
    #u = r.recognize_google(audio)
    #u = u.lower()
    #print(u)
    u = input()
    u = u.lower()
    print(u)



    if(("not" in u) or ("cannot" in u) or ("exit" in u) or ("terminate " in u) or ("dont" in u) or ("did not" in u)):
        print("Have A Nice Day")
        pyttsx3.speak("\n Have A Nice Day \n")
        break


    elif("2" in u):
        print("~~ ~~ ~~ ~~ ~~ ~~ ~~ W h a t  C a n  I  Do  For You ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~")   
        print("\n \t N O T E :- If You Want To Terminate The program Type exit \n")
        while(True):
            print("Enter your requirements .....we r listiening ...." , end='')
            pyttsx3.speak("\n\n Enter your requirements we r listiening . \n")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("\nstart saying...")
                audio = r.listen(source)
                print("wait we got it")
            p = r.recognize_google(audio)
            p = p.lower()
            print(p)



            if (("run" in p) or ("start" in p) or ("open" in p) or ("chalukaro" in p)) and ("chrome"in p):
                os.system("chrome")
            elif (("run" in p) or ("start" in p) or ("open"in p) or ("chalukaro" in p)) and ("firefox"in p):
                os.system("firefox")
            elif (("stop" in p)or("band" in p)or("close"in p)or("terminate" in p)or("exit" in p))and("firefox"in p):                                         os.system("TASKKILL /IM chrome.exe /F")                
            elif (("open" in p) or ("start" in p) or ("chalukaro" in p)) and ("gmail" in p):
                os.system("chrome www.gmail.com")
            elif (("send"in p) or ("bejo" in p) or ("janedo" in p)) and (("mail" in p) or ("gmail" in p)):
                os.system("python mail.py")                
            elif (("run" in p)or("start" in p)or("play" in p)or("chalukaro" in p))and(("music" in p)or("player"in p)):
                os.system("wmplayer")
            elif  (("open" in p) or ("start" in p) or ("chalukaro" in p)) and ("vscode" in p):
                os.system("code")
            elif(("run"in p)or("execute" in p)or("open" in p)or("chalukaro" in p))and(("notepad" in p)or("editior"in p)):
                os.system("notepad")
            elif ("exit" in p) or ("out" in p) or ("bandkaro" in p):
                break                


            elif (("make" in p) or ("create" in p) or ("bnao" in p)) and (("folder"in p) or ("dir" in p)):
                print("Enter your requirements .....we r listiening .... : " , end='')
                pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("\nstart saying...")
                    audio = r.listen(source)
                    print("wait we got it")
                fdir = r.recognize_google(audio)
                fdir = fdir.lower()
                print(fdir)
                os.system("mkdir "+fdir)
                print("created successfully")


            elif (("search" in p) or ("about" in p)):
                print("Enter your requirements .....we r listiening .... : " , end='')
                pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("\nstart saying...")
                    audio = r.listen(source)
                    print("wait we got it")
                s = r.recognize_google(audio)
                s = s.lower()
                print(s)
                os.system("start chrome google.com/search?q=" + s)
            else:
                print("wrong entry")
                pyttsx3.speak("Wrong Entry")



    elif("1" in u):
        while True:
            print("""
                -------------------------------------------------------------------------
               |                  M e n u  C a r d   F o r  U s e r                      |
                -------------------------------------------------------------------------
                """)
            pyttsx3.speak("\n\n Menu Card for User :\n")   
            print("""\n
                ----------------------------
               | Window  Tools    : Press 1 |
                ----------------------------
                                                            -----------------------------
                                                           | CGI Service       : Press 2 |
                                                            -----------------------------
                ----------------------------
               |HADOOP            : Press 3 |
                ----------------------------
                                                            -----------------------------
                                                           | AWS               : Press 4 |
                                                            ----------------------------
                ----------------------------
               |LVM               : Press 5 |
                -----------------------------
                                                            ----------------------------
                                                           | DOCKER           : Press 6 |
                                                            ----------------------------
            """)
            print("Enter your requirements .....we r listiening ...." , end='')
            #pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
            #r = sr.Recognizer()
            #with sr.Microphone() as source:
            #    print("\nstart saying...")
            #    audio = r.listen(source)
            #    print("wait we got it")
            #m = r.recognize_google(audio)
            #m = m.lower()
            m = input()
            m = m.lower()
            print(m)


            if("1" in m):
                print("""
                 --------------------------------------------------------------
                |                        Window Tools                           |
                 ---------------------------------------------------------------         
                |\t Press 1 : For Chrome   |        | \t Press 5 : For Calender |
                 --------------------------          --------------------------
                |\t Press 2 : For Firefox  |        | \t Press 6 : For Zoom     |
                 --------------------------          ---------------------------
                |\t Press 3 : For NotePad  |        | \t Press 7 : For Whatsapp |
                 --------------------------          ---------------------------
                |\t Press 4 : For W-Player |        | \t Press 8 : For Mail     |
                 --------------------------          ---------------------------
                 ---------------------------------------------------------------
                |                        Press 9 : Exit                         |
                 ---------------------------------------------------------------
                """)
                pyttsx3.speak("\n\n Enter your requirements .....we r listiening ....  \n\n\n")
                while True:
                    print("Enter your requirements .....we r listiening ...." , end='')
                    pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("\nstart saying...")
                        audio = r.listen(source)
                        print("wait we got it")
                    h = r.recognize_google(audio)
                    h = h.lower()
                    print(h)
                    if("1" in h):
                        os.system("chrome")
                        break
                    elif("2" in h):
                        os.system("firefox")
                        break
                    elif("3" in h):
                        os.system("notepad")
                        break
                    elif("4" in h):
                        os.system("wmplayer")
                        break
                    elif("5" in h):
                        os.system("calc")
                        break
                    elif("6" in h):
                        os.system("zoom")
                        break
                    elif("7" in h):
                        os.system("Whatsapp")
                        break
                    elif("8" in h):
                        os.system("python mail.py")
                        break
                    elif("9" in m):
                        print("Enter your requirements .....we r listiening .... : " , end='')
                        pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("\nstart saying...")
                            audio = r.listen(source)
                            print("wait we got it") 
                        fname = r.recognize_google(audio)
                        fname = fname.lower()
                        print(fname)
                        os.system("mkdir "+fname)
                        print("succesfully created")
                        break
                    else:
                        print("Not in Menu")
                        break


            elif("2" in m) or ("to" in m):
                print("Welcome to CGI Services \n\n")
                pyttsx3.speak("\n\n\n Welcome to CGI Service Menu \n\n\n")
                print(""""
                 ----------------------------------------------------------------------
                |                           Welcome to CGI service                      |
                 ----------------------------------------------------------------------
                 ----------------------------          ---------------------------------
                | \t Press 1 : For System CMD |       | \t Press 2 : For Docker         |
                 -----------------------------         ---------------------------------
                
                """)
                while True:
                    print("Enter your requirements .....we r listiening ...." , end='')
                    pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                    #r = sr.Recognizer()
                    #with sr.Microphone() as source:
                    #    print("\nstart saying...")
                    #    audio = r.listen(source)
                    #     print("wait we got it")   
                    #ch = r.recognize_google(audio)
                    #ch = ch.lower()
                    #print(ch)
                    ch = input()
                    ch=ch.lower()
                    print(ch)
                    if ("1" in ch):
                        print("""
                        \n\t\t\t date
                        \n\t\t\t cal
                        \n\t\t\t gui-terminal
                        """)
                        print("Enter your requirements .....we r listiening ....u r inside" , end='')
                        #pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                        #r = sr.Recognizer()
                        #with sr.Microphone() as source:
                        #    print("\nstart saying...")
                        #    audio = r.listen(source)
                        #    print("wait we got it")   
                        #ch1 = r.recognize_google(audio)
                        #ch1 = ch1.lower()
                        #print(ch1)
                        ch1 = input()
                        ch1 = ch1.lower()
                        print(ch1)
                        if ("date" in ch1) and (("run" in ch1) or ("execute" in ch1)):
                            wb.open("http://192.168.43.64/cgi-bin/iiec.py?x=date")
                        elif "calendar" in ch1:
                            wb.open("http://192.168.43.64/cgi-bin/iiec.py?x=cal")
                        elif("webbrowser" in ch1) or ("gui" in ch1) and ("terminal" in ch1):
                            wb.open("http://192.168.43.64/index.html") 
                        else:
                            print("nothing")
                    elif ("2" in ch):
                        print("""
                         --------------------------------------------------------------------
                        |                       DOCKER WEBSERVER                             |
                        ---------------------------------------------------------------------
                        ---------------------------------------------------------------------
                        | Use   |       --docker run--         |     to launch a docker      |
                         ------- ------------------------------ -----------------------------
                        | Use   |      --docker stop--         |     to stop the docker      |
                         ------- ------------------------------ -----------------------------
                        | Use   |     --docker terminate--     |     to terminate docker     |
                         --------------------------------------------------------------------
                        """)
                        print("Enter your requirements .....we r listiening ...." , end='')
                        pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                        #r = sr.Recognizer()
                        #with sr.Microphone() as source:
                        #    print("\nstart saying...")
                        #    audio = r.listen(source)
                        #    print("wait we got it")    
                        #ch2 = r.recognize_google(audio)
                        #ch2 = ch2.lower()
                        #print(ch2)
                        ch2 = input()
                        ch2 = ch2.lower()
                        print(ch2)
                        if ("docker" in ch2) and (("run" in ch2) or ("start" in ch2) or ("launch" in ch2)):
                            wb.open("http://192.168.43.64/drun.html")
                        elif ("docker" in ch2) and (("stop" in ch2) or ("band" in ch2)):
                            wb.open("http://192.168.43.64/dstop.html")
                        elif ("docker" in ch2) and (("remove" in ch2) or ("terminate" in ch2)):
                            wb.open("http://192.168.43.64/dter.html")
                        else:
                            print("nothing in docker")
                            break
                    else:
                        print("nothing in cgi-service")
                        break
                        
                        
                        
            elif ("3" in m):
                while True:
                    print("""
                     --------------------------------------------------------------------------------------
                    |                               Welcome to Hadoop Section                               |
                     ---------------------------------------------------------------------------------------
                     ------------------------------------------     ----------------------------------------
                    |     Press 0 : Setup Hadoop Cluster       |   | Press 1 : For Starting/Stoping NN /DN  |   
                     ------------------------------------------     ----------------------------------------
                    |     Press 2 : For checking NN report     |   | Press 3 : For checking NN/DN use jps   |
                     ------------------------------------------     ----------------------------------------
                    | Press 4 : Open WebUI ofHadoop FileSystem |   |                                        |
                     ------------------------------------------     ----------------------------------------
                    """)
                    def sta():
                        status = output[0]
                        if (status == 0):
                            print("All okkk....")
                        else:
                            print("An Error occured...Please check")
                        out = output[1]
                        if (out == 1):
                            print("\n\t\t\t",out)
                    print("Enter your requirements .....we r listiening ...." , end='')
                    pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                    #r = sr.Recognizer()
                    #with sr.Microphone() as source:
                    #    print("\nstart saying...")
                    #    audio = r.listen(source)
                    #    print("wait we got it")
                    #cha = r.recognize_google(audio)
                    #cha = cha.lower()
                    #print(cha)
                    cha = input("\n\n\t\t\t\t Enter your choice : ")
                    print(cha)
                    if ("0" in cha):
                        print(""""
                        \n\t\t For Hadoop Setup First we need Java and Hadoop software 
                        \n\t\t So we can tranfer it from our window to linux via winscp at /root/Desktop location
                        \n\t\t now go to  location and then install java and hadoop respectively and then configure hdfs and core-site file
                        \n\t\t Format the /mounted folder and then start its service 
                        \n\t\t For now we have to do manually all the setup but in future we can automate it with ansible 
                        """)
                    if ("1" in cha):
                        print("\n\t\t\t Enter Your IP : " , end='')
                        ipp = input()
                        print("\n\t\t\t Enter your requirement Either **namenode / datanode** : " , end='')
                        req_name = input()
                        print("\n\t\t\t Enter your status for hadoop either **start or stop** : " , end='')
                        sta_name = input()
                        cmd = "ssh -l root {} hadoop-daemon.sh {} {}".format(ipp,sta_name,req_name)
                        output = sp.getstatusoutput(cmd)
                        print(cmd)
                        sta()
                    if ("2" in cha):
                        print("\n\t\t\t Enter your IP:", end='')
                        ipp = input()
                        cmd = "ssh -l root {} hadoop dfsadmin -report".format(ipp)
                        output = sp.getstatusoutput(cmd)
                        print(output)
                        sta()
                    if ("3" in cha):
                        print("\n\t\t\t Enter your IP : ", end='')
                        ipp = input()
                        cmd = "ssh -l root {} jps ".format(ipp)
                        output = sp.getstatusoutput(cmd)
                        print(output)
                        sta()
                    if ("4" in cha):
                        wb.open("http://192.168.43.196:50070")

                    

            elif ("4" in m):
                while True:
                    print("""
                     --------------------------------------------------------------------------------
                    |                             Welcome to AWS Section                              |
                     ---------------------------------------------------------------------------------                 
                     ---------------------------------        ---------------------------------------
                    | Press 1 : Creating key-pairs    |      | Press 5 : Creating EBS Volume         |
                     ---------------------------------        ---------------------------------------
                    |Press 2 : Creating securitygroup |      | Press 6 :Attaching EBS to Running VM  | 
                     ---------------------------------        ---------------------------------------
                    |Press 3 : For Add inbound rule   |      | Press 7 : For Creating S3 Bucket      |
                     ---------------------------------        ---------------------------------------
                    | Press 4 : Launching Instances   |      | Press 8 : Uploading Image to S3bucket |
                     ---------------------------------        ---------------------------------------
                    | Press 9 : Creating CF Distribut |      | Press 10: High availablityarchitecture|
                     ---------------------------------        ---------------------------------------                     
                     --------------------------------------------------------------------------------
                    |                               Press 11: For Exit                               |
                     --------------------------------------------------------------------------------
                    """)

                    def sts():
                        print(output)
                        status=output[0]
                        if(status==0):
                            print("\n\t\t\t\t\t\tAll_okk")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print("\n\t\t\t\t\t\tAn error occured.........please check")
                    out=output[1]
                    print("\n\t\t\t",out)

                    print("\n\t\t\t Enter Your choice from aws menu", end='')
                    print("Enter your requirements .....we r listiening .... : " , end='')
                    pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                    #r = sr.Recognizer()
                    #with sr.Microphone() as source:
                    #    print("\nstart saying...")
                    #    audio = r.listen(source)
                    #    print("wait we got it")
                    #chb = r.recognize_google(audio)
                    #chb = chb.lower()
                    #print(chb)
                    chb = input()
                    chb = chb.lower()
                    print(chb)
                    if ("1" in chb):
                        print("Enter the name of key : " , end='')
                        key_name = input()
                        cmd = "aws ec2 create-key-pair  --key-name {} --query KeyMaterial --output text > {}.pem".format(key_name,key_name)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif ("2" in chb):
                        print("\t\t\t Enter the name of security_group : " , end='')
                        sec_n = input()
                        print("\t\t\t Enter the description of security_group : " , end='')
                        sec_des = input()
                        cmd = "aws ec2 create-security-group --description {0} --group-name {1}_sg --vpc-id vpc-38739d53".format(sec_des,sec_n)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif ("3" in chb):
                        print("\n\t\t Enter the ip u want to add for ingress :  ",end= ' ')
                        ip1= input()
                        print("\n\t\t Enter the name of security_group : " , end='')
                        sec_n = input()
                        print("\n\t\t Enter your netmask either 0 8 16 32 : ",end='')
                        ne = int(input())
                        cmd='aws ec2 authorize-security-group-ingress  --group-name {}_sg   --protocol tcp   --port 22    --cidr {}/{}'.format(sec_n,ip1,ne)
                        output=sp.getstatusoutput(cmd)
                        sts()
                        cmd='aws ec2 authorize-security-group-ingress  --group-name {}_sg   --protocol tcp   --port 80    --cidr {}/{}'.format(sec_n,ip1,ne)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("4" in chb):
                        print("\n\t\t\t Enter the security group id sg- : ",end= ' ')
                        sg=input()
                        print("\n\t\t\t Enter the key name : ",end= ' ')
                        kn=input()
                        cmd='aws ec2 run-instances  --image-id ami-0a9d27a9f4f5c0efc    --instance-type t2.micro    --count 1   --subnet-id  subnet-b6c8dfde   --security-group-ids sg-01e1d2e50162b409f  --key-name arth --tag-specifications ResourceType=instance,Tags=[{Key=Name,Value=Task_3_Instance}]'
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("5" in chb):
                        print("\n\t\t\t Enter the size in GB : ",end= ' ')
                        si=input()
                        cmd='aws ec2 create-volume --availability-zone ap-south-1a   --size {}'.format(si)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("6" in chb):
                        print("\n\t\t\t Enter the Instance-id : ", end='')
                        is1 = input()
                        print("\n\t\t\t  Enter the Volume-id : ",end='')
                        vid=input()
                        cmd = "aws ec2 attach-volume --device /dev/xvdb --instance-id {} --volume-id{}".format(is1,vid)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif ("7" in chb):
                        print("\n\t\t\t Enter the name s3 bucket : ",end='')
                        s3_name = input()
                        cmd = "aws s3 mb s3://{}".format(s3_name)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("8" in chb):
                        print("\n\t\t\t Enter the bucket Name : ",end= ' ')
                        s3=input()
                        print("\n\t\t\t Enter the folder Path : ",end= ' ')
                        s=input()
                        cmd=r'aws s3 cp  E:\user data   s3://{}/ --recursive --exclude "*" --include "*.jpg"'.format(s3)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("9" in chb):
                        print("\n\t\t\t Enter the Bucket Name : ",end= ' ')
                        s3=input()
                        cmd="aws cloudfront create-distribution   --origin-domain-name {}.s3.amazonaws.com   --default-root-object index.html".format(s3)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("10" in chb):
                        print("comming soon")
                        print("\t\t\t\t\t ---------------------------")
                        print("\t\t\t\t\t Welcome to Rathi CloudFront")
                        print("\t\t\t\t\t ---------------------------")
                        pyttsx3.speak("\n\n\n\n\n Welcome to Rathi CloudFront")
                        pyttsx3.speak("\n\n\n\n\n Please Enter Your Password")

                        while True:
                            print("""
                            ---------------------------------------------------------------------------------------------------------------------
                            |                                             High Availabilty Architecture                                           |
                            ---------------------------------------------------------------------------------------------------------------------
                                        -------------------------------                            ---------------------------------
                                       | Press 1 : Create Key-Pair     |                          | Press 2 : Create Security-Group |
                                        -------------------------------                            ---------------------------------
                                                                       ------------------------------
                                                                      | Press 3 : ingress rule to sg |
                                                                       ------------------------------
                                        -------------------------------                            ---------------------------------------
                                       | Press 4 : Run/Launch Instance |                          | Press 5 : Install&Start HTTPD Service |
                                        -------------------------------                            ---------------------------------------
                                                                       ~------------------------------------------
                                                                      | Press 7 : Fomat&Mount Partition to folder |
                                                                       -------------------------------------------
                                        ---------------------------------------                    ---------------------------------------                    
                                       | Press 6 : Create EBS & attach to inst  |                 | Press 8 : Creating S3 Bucket&Uploading |                   
                                        ----------------------------------------                   ---------------------------------------- 
                                                                    -------------------------------------------------
                                                                   | Press 9 :  Create CFDistribution & Update Folder |
                                                                    --------------------------------------------------
                            """)
                            print("\n\t\t\t Enter Your choice from aws menu", end='')
                            print("Enter your requirements .....we r listiening .... : " , end='')
                            pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                            r = sr.Recognizer()
                            with sr.Microphone() as source:
                                print("\nstart saying...")
                                audio = r.listen(source)
                                print("wait we got it")  
                            chb1 = r.recognize_google(audio)
                            chb1 = chb1.lower()
                            print(chb1)
                            #chb = input()
                            if ("1" in chb1):
                                print("Enter the name of key: " , end='')
                                key_name = input()
                                cmd = "aws ec2 create-key-pair  --key-name {} --query KeyMaterial --output text > {}.pem".format(key_name,key_name)
                                output=sp.getstatusoutput(cmd)
                                sts()
                            elif ("2" in chb or "to" in chb):
                                print("\n\t\t Enter the name of security_group : " , end='')
                                sec_n = input()
                                print("\n\t\t Enter the description of security_group : " , end='')
                                sec_des = input()        
                                cmd = "aws ec2 create-security-group --description {0} --group-name {1}_sg --vpc-id vpc-38739d53".format(sec_des,sec_n)
                                output=sp.getstatusoutput(cmd)
                                sts()
                            elif("3" in chb1):
                                print("\n\t\t Enter the ip u want to add for ingress :  ",end= ' ')
                                ip1= input()
                                print("\n\t\t Enter the name of security_group : " , end='')
                                sec_n = input()
                                print("\n\t\t Enter your netmask either 0 8 16 32 : ",end='')
                                ne = int(input())
                                cmd='aws ec2 authorize-security-group-ingress  --group-name {}_sg   --protocol tcp   --port 22    --cidr {}/{}'.format(sec_n,ip1,ne)
                                output=sp.getstatusoutput(cmd)
                                sts()
                                cmd='aws ec2 authorize-security-group-ingress  --group-name {}_sg   --protocol tcp   --port 80    --cidr {}/{}'.format(sec_n,ip1,ne)
                                output=sp.getstatusoutput(cmd)
                                sts()
                            elif ("4" in chb1):        
                                cmd='aws ec2 run-instances  --image-id ami-0a9d27a9f4f5c0efc    --instance-type t2.micro    --count 1   --subnet-id  subnet-b6c8dfde   --security-group-ids sg-01e1d2e50162b409f  --key-name arth --tag-specifications ResourceType=instance,Tags=[{Key=Name,Value=Task_3_Instance}]'
                                output=sp.getstatusoutput(cmd)
                                sts()
                            elif ("5" in chb1):
                                print("\n\n\n\t\t\t\t\t\t\t\t\thttpd Service\n\t")
                                print("\n\t\t\t\t\t\tEnter the ip of instance : ",end= ' ')
                                ip1=input()
                                print("\n\t\t\t\t\t\tEnter the key_name of instance : ",end= ' ')
                                keye_name = input()
                                cmd=r"ssh -l ec2-user {0}  -i C:\Users\Admin\Downloads\{1} sudo yum install httpd -y".format(ip1,keye_name)
                                output=sp.getstatusoutput(cmd)
                                sts()
                                cmd=r"ssh -l ec2-user {0}  -i C:\Users\Admin\Downloads\{1}.pem sudo systemctl start httpd".format(ip1,keye_name)
                                output=sp.getstatusoutput(cmd)
                                sts()
                            elif("6" in chb1):
                                print("\n\n\n\t\t\tEBS Volume")
                                print("\n\t\t\t\t Enter the size in GB : ",end= ' ')
                                si=input()
                                cmd='aws ec2 create-volume --availability-zone ap-south-1a   --size {}'.format(si)
                                output=sp.getstatusoutput(cmd)
                                sts() 
                                print("\n\t\t\tEnter the instance id : ",end= ' ')
                                id1=input()
                                print("\n\t\t\t Enter the volume id : " ,end= ' ')
                                vol=input()
                                cmd='aws ec2 attach-volume  --device /dev/xvdb  --instance-id {}  --volume-id {}'.format(id1,vol)
                                output=sp.getstatusoutput(cmd)
                                sts()
                            elif("7" in chb1):
                                print("\n\n\t\t\t Linux Partitions\n\t\t\t")
                                print("\n\t\t\t Format parition\n\t\t\t")
                                print("\n\t\t\t Mount partition\n\t\t\t")
                                print("\n\t\t\t S3 Bucket\n\t\t\t")
                                print("\n\t\t\t Enter the ip of instance : ",end= ' ')
                                ip2=input()
                                print("\n\t\t\t Enter the key_name : ",end='')
                                k_name= input()
                                cmd=r"ssh -l ec2-user {}  -i C:\Users\Admin\Downloads\{}.pem  sudo fdisk -l".format(ip2,k_name)
                                #cmd=r"ssh  root@13.233.31.13 fdisk /dev/xvdf"
                                output=sp.getstatusoutput(cmd)
                                sts()
                                cmd=r"ssh -l ec2-user {}	  -i C:\Users\Admin\Downloads\{}.pem sudo mkfs.ext4                /dev/xvdf1	".format(ip2,k_name)
                                output=sp.getstatusoutput(cmd)
                                sts()

                                cmd=r"ssh -l ec2-user {}	  -i C:\Users\Admin\Downloads\{}.pem sudo mount /dev/xvdf1    /var/www/html".format(ip2,k_name)
                                output=sp.getstatusoutput(cmd)
                                sts()
                            elif("8" in chb1):
                                print("\n\t\t\t Enter Bucket Name : ",end= ' ')
                                s3=input()
                                cmd="aws s3 mb s3://{}".format(s3)
                                output=sp.getstatusoutput(cmd)
                                sts()
                                print("\n\n\n\t\t\t\t\tUploading image to s3 bucket\n\t\t\t")
                                cmd=r'aws s3 cp  E:\user data   s3://{}/ --recursive --exclude "*" --include "*.jpg"'.format(s3)
                                output=sp.getstatusoutput(cmd)
                                sts()
                            elif("9" in chb1):
                                print("\n\t\t\tEnter the bucket name ",end= ' ')
                                s3=input()
                                print("\n\n\n\t\t\t Create CloudFront Distribution\n\t\t\t")
                                cmd="aws cloudfront create-distribution   --origin-domain-name {}.s3.amazonaws.com   --default-root-object index.html".format(s3)
                                output=sp.getstatusoutput(cmd)
                                sts()
                                print("\n\n\n\t\t\t Uploading the file\n\t\t\t")
                                print("\n\t\t\t Enter the ip of instance : ",end= ' ')
                                ip2=input()
                                print("\n\t\t\t Enter the key_name : ",end='')
                                k_name= input()
                                cmd=r" ssh -l ec2-user {}	  -i C:\Users\Admin\Downloads{}.pem sudo  echo Hello > index.html	".format(ip2,k_name)
                                output=sp.getstatusoutput(cmd)
                                sts()
                            else:
                                print("nothing")
                                break   

                    elif("11" in chb):
                        pyttsx3.speak("Returing back")
                        print("\n\t\t\t Returing back")
                        break
                    else:
                        print("nothing in aws")
                        break
                        
            elif("5" in m):
                while(True):
                    print("""
                     ----------------------------------------------------------------------------------------
                    |                                  Welcome to LVM Partition                              |
                     ----------------------------------------------------------------------------------------
                             ----------------------------             -------------------------------
                            | 1 : Create physical volume |           | 6 : Format                    |
                             ----------------------------             -------------------------------
                            | 2 : Create volume group    |           | 7 : Create the dir and mount  |
                             ----------------------------             -------------------------------
                            | 3 : Display vg             |           | 8 : Extend Logical Volume     |
                             ----------------------------             -------------------------------
                            | 4 : Create Logical volume  |           | 9 : Format extended volume    |
                             ----------------------------             -------------------------------
                            | 5: Display Logical Volume  |           | 10 : Reduce Logical Volume    |
                             ----------------------------             -------------------------------
                     -----------------------------------------------------------------------------------------
                     |                                  11 : Return Back                                       |
                      -----------------------------------------------------------------------------------------             
                    """)
                    #pyttsx3.speak("Please..Enter your..choice")
                    print("Enter your requirements .....we r listiening .... : " , end='')
                    pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                    #r = sr.Recognizer()
                    #with sr.Microphone() as source:
                    #    print("\nstart saying...")
                    #    audio = r.listen(source)
                    #    print("wait we got it")
                    #ch5 = r.recognize_google(audio)
                    #ch5 = ch5.lower()
                    #print(ch5)
                    ch5=input("\n\n\t\t\t\t\t\t\t\tEnter Your Choice : ")
                    print(ch5)
                    if("1" in ch5):
                        print("\n\t\t\t Enter the first Hard-Disk Name : ",end= ' ')
                        hd12=input()
                        print("\n\t\t\t\ Enter the IP : ",end= ' ')
                        ipp=input()
                        cmd='ssh -l root {}	sudo pvcreate {}'.format(ipp,hd12)
                        output=sp.getstatusoutput(cmd)
                        sts()
                        print("\n\t\t\t Enter the second Hard-Disk Name : ",end= ' ')
                        hd13=input()
                        cmd='ssh -l root {}	sudo pvcreate {}'.format(ipp,hd13)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("2" in ch5):
                        print("\n\t\t\t Enter the Volume Group(VG) Name : ",end= ' ')
                        vg=input()
                        cmd='ssh -l root {}	sudo vgcreate {}  {}    {}'.format(ipp,vg,hd12,hd13)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("3" in ch5):
                        print("\n\t\t\t Enter the Volume Group (VG) Name : ",end= ' ')
                        vg=input()
                        cmd='ssh -l root {}	sudo vgdisplay {}'.format(ipp,vg)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("4" in ch5):
                        print("\n\t\t\t Enter the Logical Volume (LV) Name : ",end= ' ')
                        lv=input()
                        print("\n\t\t\t Enter the Logical Volume (LV) Size in GB : ",end= ' ')
                        size=input()
                        print("\n\t\t\t Enter the Volume Goup (VG) Name : ",end= ' ')
                        vg=input()
                        cmd='ssh -l root {}	sudo lvcreate --size {}G --name {} {}'.format(ipp,size,lv,vg)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("5" in ch5):
                        print("\n\t\t\t Enter the Logical Volume (LV) Name ",end= ' ')
                        lv=input()
                        print("\n\t\t\t Enter the Volume Group (VG) Name : ",end= ' ')
                        vg=input()
                        cmd='ssh -l root {}	sudo lvdisplay {} {}'.format(ipp,vg,lv)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("6" in ch5):
                        print("\n\t\t\t Enter the Logical Volume (LV) Name : ",end= ' ')
                        lv=input()
                        print("\n\t\t\t Enter the Volume-Group (VG) Name : ",end= ' ')
                        vg=input()
                        cmd='ssh -l root {}	sudo mkfs.ext4  /dev/{}/{}'.format(ipp,vg,lv)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("7" in ch5):
                        print("\n\t\t\t Enter the Directory Name : ",end= ' ')
                        fil=input()
                        cmd='ssh -l root {}	sudo mkdir /{}'.format(ipp,fil)
                        output=sp.getstatusoutput(cmd)
                        sts()
                
                        print("\n\t\t\t Enter the Logical Volume (LV) Name : ",end= ' ')
                        lv=input()
                        cmd='ssh -l root {}	sudo mount /dev/{}/{}    /{}'.format(ipp,vg,lv,fil)
                        output=sp.getstatusoutput(cmd)
                        sts()

                    elif("8" in ch5):
                        print("\n\t\t\t Enter the Logical Volume (LV) Name : ",end= ' ')
                        lv=input()
                        print("\n\t\t\t Enter the Volume-Group (VG) Name : ",end= ' ')
                        vg=input()
                        print("\n\t\t\t Enter the size by which you want to EXtend LV : ",end= ' ')
                        size=input()
                        cmd='ssh -l root {}	sudo lvextend  --size +{}G  /dev/{}/{}'.format(ipp,size,vg,lv)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("9" in ch5):
                        print("\n\t\t\t Enter the Logical Volume (LV) Name :",end= ' ')
                        lv=input()
                        print("\n\t\t\t Enter the Volume-Group (VG) Name : ",end= ' ')
                        vg=input()
                        cmd='ssh -l root {}	sudo resize2fs /dev/{}/{}'.format(ipp,vg,lv)
                        output=sp.getstatusoutput(cmd)
                        sts()
               
                    elif("10" in ch5):

                        print("\n\t\t\t Enter the Folder Location : ",end='')
                        f_loc = input()
                        cmd='ssh -l root {} umount {}'.format(ipp,f_loc)
                        output=sp.getstatusoutput(cmd)
                        sts()
                        
                        print("\n\t\t\t Enter the Volume-Group (VG) Name : ",end= ' ')
                        vg=input()
                        print("\n\t\t\t Enter the Logical Volume (LV) Name :",end= ' ')
                        lv=input()
                        cmd ='ssh -l root {} e2fsck -f /dev/{}/{}'.format(ipp,vg,lv)
                        output=sp.getstatusoutput(cmd)
                        sts()

                        cmd='ssh -l root {} resize2fs /dev/mapper/{}-{}'.format(ipp,vg,lv)
                        output=sp.getstatusoutput(cmd)
                        sts()
                        
                        print("\n\t\t\t Enter the Size that u want to Decrease : ",end='')
                        size_d = int(input())
                        cmd='ssh -l root {} lvreduce -L {}G /dev/mapper/{}-{}'.format(ipp,size_d,vg,lv)
                        output=sp.getstatusoutput(cmd)
                        sts()

                        cmd ='ssh -l root {} e2fsck -f /dev/{}/{}'.format(ipp,vg,lv)
                        output=sp.getstatusoutput(cmd)
                        sts()

                        print("\n\t\t\t Enter the folder Location that u Mount : ",end='')
                        fi_loc = input()
                        cmd='ssh -l root {} mount {}'.format(ipp,fi_loc)
                        output=sp.getstatusoutput(cmd)
                        sts()

                        print("\n\t\t\t Check is everything is correct or not ")
                        cmd='ssh -l root {} df -hT'.format(ipp)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("11" in ch5):
                        pyttsx3.speak("Returing back")
                        print("\n\t\t\tReturing back")
                        break
                    else:
                        print("nothing in lvm partition")
                        break

            elif("6" in m):
                while(True):
                    print("""
                     ----------------------------------------------------------------------------------------
                    |                                  Welcome to DOCKER Secion                              |
                     ----------------------------------------------------------------------------------------
                             ----------------------------             -------------------------------
                            | 1 : Check Software  |      |           | 6: Launch Container           |
                             ----------------------------             -------------------------------
                            | 2 : CHECK VERSION/INFO     |           | 7 : Stop Container            |
                             ----------------------------             -------------------------------
                            | 3 : DOCKER IMAGES          |           | 8 : Remove Container          |
                             ----------------------------             -------------------------------
                            | 4 : Check all Container    |           | 9 : remove Images             |
                             ----------------------------             -------------------------------
                            | 5 : Check Running Container |          | 10 : Return back              |
                             ----------------------------             -------------------------------
                    """)
                    
                    def sts():
                        print(output)
                        status=output[0]
                        if(status==0):
                            print("\n\t\t\t\t\t\tAll_okk")
                        else:
                            pyttsx3.speak("An error occured.........please check")
                            print("\n\t\t\t\t\t\tAn error occured.........please check")
                        out=output[1]
                        print("\n\t\t\t",out)

                    print("Enter your requirements .....we r listiening .... : " , end='')
                    pyttsx3.speak("\n\n Enter your requirements .we r listiening . \n")
                    #r = sr.Recognizer()
                    #with sr.Microphone() as source:
                    #    print("\nstart saying...")
                    #    audio = r.listen(source)
                    #    print("wait we got it")
                    #chd = r.recognize_google(audio)
                    #chd = chd.lower()
                    #print(chd)
                    chd =input("Enter : ")
                    chd=chd.lower()
                    print(chd)
                    if("1" in chd):
                        print("\n\t\t\t CHECKING DOCKER SOFTWARE INSTALLED OR NOT ")
                        print("\n\t\t\t Enter the IP :  ",end= ' ')
                        ipp=input()
                        cmd='ssh -l root {}	rpm -q docker-ce'.format(ipp)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("2" in chd):
                        print("\n\t\t\t CHECKING DOCKER Version and Docker Info ")
                        print("\n\t\t\t Enter the IP :  ",end= ' ')
                        ipp=input()
                        cmd='ssh -l root {}	docker --version'.format(ipp)
                        output=sp.getstatusoutput(cmd)
                        sts()
                        cmd='ssh -l root {}	docker info'.format(ipp)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("3" in chd):
                        print("\n\t\t\t CHECKING All Docker Images ")
                        print("\n\t\t\t Enter the IP : ",end= ' ')
                        ipp=input()
                        cmd='ssh -l root {}	docker images'.format(ipp)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("4" in chd):
                        print("\n\t\t\t CHECKING All  Docker Container ")
                        print("\n\t\t\t Enter the ip : ",end= ' ')
                        ipp=input()
                        cmd='ssh -l root {}	docker ps -a '.format(ipp)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("5" in chd):
                        print("\n\t\t\t CHECKING All Running Docker Container : ")
                        print("\n\t\t\t Enter the ip : ",end= ' ')
                        ipp=input()
                        cmd='ssh -l root {}	docker ps '.format(ipp)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    
                    elif("6" in chd):
                        print("\n\t\t\t Launching Doker Container ")
                        print("\n\t\t\t Enter the ip : ",end= ' ')
                        ipp=input()
                        print("\n\t\t\t Enter the Name of Container : ",end= ' ')
                        d_name=input()
                        print("\n\t\t\t Enter the image name : ",end= ' ')
                        d_image=input()
                        cmd='ssh -l root {}	docker run -dit --name {} {}'.format(ipp,d_name,d_image)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("7" in chd):
                        print("\n\t\t\t Stop Doker Container ")
                        print("\n\t\t\tEnter the ip : ",end= ' ')
                        ipp=input()
                        print("\n\t\t\t Enter the Name of Container : ",end= ' ')
                        d_name=input()
                        cmd = 'ssh -l root {} docker stop {} '.format(ipp,d_name)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("8" in chd):
                        print("\n\t\t\t Removeing Doker Container : ",end= ' ')
                        print("\n\t\t\t\t\t\tEnter the ip ",end= ' ')
                        ipp=input()
                        print("\n\t\t\t\Enter the Name of Container :",end= ' ')
                        d_name=input()
                        cmd = 'ssh -l root {} docker rm -f {} '.format(ipp,d_name)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("9" in chd):
                        print("\n\t\t\t Removing Doker Container Images : ",end= ' ')
                        print("\n\t\t\t\t\t\tEnter the ip ",end= ' ')
                        ipp=input()
                        print("\n\t\t\tEnter the Name of Container : ",end= ' ')
                        d_image=input()
                        cmd = 'ssh -l root {} docker rmi {} '.format(ipp,d_image)
                        output=sp.getstatusoutput(cmd)
                        sts()
                    elif("10" in chd):
                        print("return")
                        break
                    else:
                        print("wrong ")
            else:
                print("have a nice day from openingMenu-tools")
                break
    elif("3" in u):
        print("byy")
        break
    else:
            print("wronh Entry")
