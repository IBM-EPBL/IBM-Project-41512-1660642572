import ibm_db

connection = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=sxs46868;PWD=e6sL28GSXIPtNJG0;", '', '')

print(f"connection is : {connection}")

print('successfully installed')

#
# # sql query to get details from customer table in bludb database in ibm cloud using ibmdb2 via python
# # sql = "INSERT INTO customers VALUES(3,'vengateshwaran')"
# # ibm_db.exec_immediate(connection, sql)
#
# # sql = "DELETE customers WHERE customers.serial_no=3;"
# # ibm_db.exec_immediate(connection, sql)
#
sql = "SELECT * FROM users"
stmt = ibm_db.exec_immediate(connection, sql)
dictionary = ibm_db.fetch_assoc(stmt)
print(dictionary)
while dictionary != False:
    # print ("The ID is : ", dictionary["NAME"])
    print("FULL Row : ", dictionary)
    dictionary = ibm_db.fetch_assoc(stmt)


print("-------------------------------------")