import ibm_db
class Storage():
    cnt = ibm_db.connect(
        "DATABASE=bludb;HOSTNAME=8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30120;SECURITY=SSl;SSL=true;UID=zsb20612;PWD=jZKZAs5ou1zHS6IO", "", "")

    def check(self, Mobile):
        sql = "SELECT MOBILE FROM USER"
        cur = ibm_db.exec_immediate(self.cnt, sql)
        res=ibm_db.fetch_tuple(cur)
        while res!=False:
            if res[0]==Mobile:
                return 1
            res=ibm_db.fetch_tuple(cur)
        return 0
    def store(self,uname,mobile,email,psw):
        ob2=Storage()
        if ob2.check(mobile)==0:
            sql="INSERT INTO USER (SNAME,MOBILE,EMAIL,PASS) VALUES('{}','{}','{}','{}')".format(uname,mobile,email,psw)
            cur=ibm_db.exec_immediate(self.cnt,sql)
            print("Success")
            return 1
        else:
            return 1