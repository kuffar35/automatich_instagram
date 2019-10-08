import sqlite3 # Sqlite'yı dahil ediyoruz
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
import time


class database():
    def __init__(self,database="boş",tablename="boş",attributes="boş"):
        self.database = database
        self.tablename = tablename
        self.attributes =attributes

        self.createdatabase()
    def createdatabase(self):
        self.con = sqlite3.connect(self.database)  # Tabloya bağlanıyoruz
        self.cursor = self.con.cursor()  # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

        def tablo_oluştur():
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS {} {}".format(self.tablename, self.attributes, ))  # Sorguyu çalıştırıyoruz.
            self.con.commit()  # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.
        tablo_oluştur()
        self.con.close()  # Bağlantıyı koparıyoruz

class databaseInsertOperation():
    def __init__(self,databasename="bos",attributes="bos"):
        self.databasename = databasename
        self.attributes = attributes
        self.insertOperation()
    def insertOperation(self):
        con = sqlite3.connect(self.databasename)
        cursor = con.cursor()
        cursor.execute(self.attributes)
        con.commit()
        con.close()

class databaseUpdateOperation():
    def __init__(self,databasename="bos",attributes1="bos"):
        self.databasename = databasename
        self.attributes1 = attributes1


        self.updateOperation()
    def updateOperation(self):
        con = sqlite3.connect(self.databasename)
        cursor = con.cursor()
        print("işlem1")
        cursor.execute(self.attributes1)
        print("işlem2")
        con.commit()
        print(self.attributes1)
        con.close()

class sendMessageClass():
    def __init__(self,message = "empty",databasename="bos",tablename="bos"):
        self.message = message
        self.databasename = databasename
        self.tablename = tablename
        self.sendMessageFunction()


    def sendMessageFunction(self):
        self.con = sqlite3.connect(self.databasename)
        self.cursorUsername = self.con.cursor()

        self.cursorCustomerName = self.con.cursor()
        self.cursorCustomerName.execute("Select _USERNAME From customerInformation")
        customerName = self.cursorCustomerName.fetchall()
        #**********
        i=0
        for cName in customerName:
          print(i)
          i+=1
        #************
        while(i>0):
         i-=1
         print(customerName[i][0])
         #**************

         self.cursorUsername.execute("Select _USERNAME From {} where _ID = {}".format(self.tablename,1))
         username = self.cursorUsername.fetchone()

         self.cursorPassword = self.con.cursor()
         self.cursorPassword.execute("Select _PASSWORD From {} where _ID = {}".format(self.tablename,1))
         password = self.cursorPassword.fetchone()

         print(username)
         print(password)
         mesaj = MIMEMultipart()  # Mail yapımızı oluşturuyoruz.

         mesaj["From"] = username[0]  # Kimden Göndereceğimiz

         mesaj["To"] = customerName[i][0]  # Kime Göndereceğimiz

         mesaj["Subject"] = "kurum içi mail gönderme"  # Mailimizin Konusu

         mesaj_govdesi = MIMEText(self.message, "plain")  # Mailimizin gövdesini bu sınıftan oluşturuyoruz.

         mesaj.attach(mesaj_govdesi)  # Mailimizin gövdesini mail yapımıza ekliyoruz.

         try:
            mail = smtplib.SMTP("smtp.gmail.com",
                                587)  # SMTP objemizi oluşturuyoruz ve gmail smtp server'ına bağlanıyoruz.

            mail.ehlo()  # SMTP serverına kendimizi tanıtıyoruz.

            mail.starttls()  # Adresimizin ve Parolamızın şifrelenmesi için gerekli

            mail.login(username[0],
                       password[0])  # SMTP server'ına giriş yapıyoruz. Kendi mail adresimizi ve parolamızı yapıyoruz.

            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())  # Mailimizi gönderiyoruz.
            print("Mail başarıyla gönderildi....")
            mail.close()  # Smtp serverımızın bağlantısını koparıyoz.

         except:
            sys.stderr.write(
                "Mail göndermesi başarısız oldu...")  # Herhangi bir bağlanma sorunu veya mail gönderme sorunu olursa
            sys.stderr.flush()
        self.con.close()


#datagraidview
class datagraidview():
    pass

#selenium_operations
class selenium_instagramAddFollewer():
 def __init__(self,goalName = "kuffar35",instgramDatabase ="bos",instagramName = "bos",buttonOperation = "boş"):
   self.goalName = goalName
   self.instagramDatabase = instgramDatabase
   self.instagramName = instagramName
   self.buttonOperation = buttonOperation

   self.seleniumView()
 def seleniumView(self):


  con = sqlite3.connect(self.instagramDatabase)
  cursor = con.cursor()
  cursor.execute(self.instagramName)
  liste = cursor.fetchall()
  i = 0
  browser = webdriver.Firefox()
  for list in liste:
      name = liste[i][0]
      if name == "berebere914" or name == "berebere299":
          print("name")
      print(name)
      url = "https://www.instagram.com/"

      browser.get(url)
      time.sleep(2)
      enterInstagram = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
      enterInstagram.click()

      username = browser.find_element_by_name("username")
      password = browser.find_element_by_name("password")

      username.send_keys(name)
      password.send_keys("181172561121")
      time.sleep(2)
      loginButton = browser.find_element_by_xpath(
          "/html/body/span/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
      loginButton.click()
      time.sleep(2)

      profilePageUrl = "https://www.instagram.com/{}/".format(self.goalName)
      browser.get(profilePageUrl)

      time.sleep(2)
      follewerButton = browser.find_element_by_xpath(self.buttonOperation)
      follewerButton.click()
      time.sleep(2)

      profileExit = browser.find_element_by_xpath(
          "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span")
      profileExit.click()
      time.sleep(2)
      profileExit2 = browser.find_element_by_xpath(
          "//*[@id='react-root']/section/main/div/header/section/div[1]/div/button/span")
      profileExit2.click()
      time.sleep(2)
      profileExit3 = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/button[7]")
      profileExit3.click()
      time.sleep(2)
      print(liste[i][0])
      i += 1
  browser.close()
  con.close()