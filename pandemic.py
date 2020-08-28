# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:51:39 2020

@author: swanuja
"""

import sqlite3

conn = sqlite3.connect('pandemicdb.db')

def create_tables():
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("CREATE TABLE IF NOT EXISTS ward(w_no INTEGER PRIMARY KEY NOT NULL, w_name VARCHAR(20) NOT NULL)")
    conn.execute("CREATE TABLE IF NOT EXISTS person(p_id TEXT PRIMARY KEY NOT NULL, f_name VARCHAR(20) NOT NULL, l_name VARCHAR(20) NOT NULL, p_dob DATE NOT NULL, p_sex VARCHAR(1) NOT NULL, p_phno VARCHAR(10) NOT NULL CHECK(p_phno NOT LIKE '%[^0-9]%'), p_address VARCHAR(100) NOT NULL, w_no INTEGER, FOREIGN KEY(w_no) REFERENCES ward(w_no) ON DELETE SET NULL)")
    conn.execute("CREATE TABLE IF NOT EXISTS hospital(h_id TEXT PRIMARY KEY NOT NULL, h_name VARCHAR(20) NOT NULL, h_address VARCHAR(100) NOT NULL, w_no INTEGER, FOREIGN KEY(w_no) REFERENCES ward(w_no) ON DELETE SET NULL)")
    conn.execute("CREATE TABLE IF NOT EXISTS location(l_id TEXT PRIMARY KEY NOT NULL, l_name VARCHAR(20), l_address VARCHAR(100) NOT NULL, w_no INTEGER, FOREIGN KEY(w_no) REFERENCES ward(w_no) ON DELETE SET NULL)")
    conn.execute("CREATE TABLE IF NOT EXISTS country(cy_id TEXT PRIMARY KEY NOT NULL, cy_name VARCHAR(20) NOT NULL)")
    conn.execute("CREATE TABLE IF NOT EXISTS patient(pat_id TEXT PRIMARY KEY NOT NULL, tested_pdate DATE NOT NULL, discharge_date DATE, p_id TEXT, h_id TEXT, i_id TEXT, FOREIGN KEY(i_id) REFERENCES patient(pat_id), FOREIGN KEY(p_id) REFERENCES person(p_id) ON DELETE CASCADE, FOREIGN KEY(h_id) REFERENCES hospital(h_id) ON DELETE SET NULL)")
    conn.execute("CREATE TABLE IF NOT EXISTS contact(c_id TEXT PRIMARY KEY NOT NULL, p_id TEXT NOT NULL, FOREIGN KEY(p_id) REFERENCES person(p_id))")
    conn.execute("CREATE TABLE IF NOT EXISTS travel_from(pat_id TEXT NOT NULL, cy_id TEXT NOT NULL, arrival_date DATE, PRIMARY KEY(pat_id,  cy_id))")
    conn.execute("CREATE TABLE IF NOT EXISTS visited(pat_id TEXT NOT NULL, l_id TEXT NOT NULL, visited_date DATE NOT NULL, PRIMARY KEY(pat_id, l_id, visited_date))")
    conn.execute("CREATE TABLE IF NOT EXISTS interactions(pat_id TEXT NOT NULL, c_id TEXT NOT NULL, contacted_on DATE NOT NULL, toc VARCHAR(1) NOT NULL)")
    conn.execute("CREATE TABLE IF NOT EXISTS trigger_test (message VARCHAR(100))")
    
def insert_sample_ward():
    conn.execute("INSERT INTO ward(w_no, w_name) VALUES (1, 'Jayanagar'),(2, 'JP Nagar'),(3, 'Banashankari'),(4, 'Basavanagudi'),(5, 'Bannerghatta'),(6, 'MG Road'),(7, 'Peenya'),(8, 'Majestic')")
    conn.commit()
        
def insert_sample_country():
    conn.execute("INSERT INTO country(cy_id, cy_name) VALUES ('CY1', 'UAE'),('CY2', 'USA'),('CY3', 'Italy'),('CY4', 'South Korea'),('CY5','UK')")
    conn.commit()
    
def insert_sample_person():
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P1','Maya','Sarabhai','1957-03-17','F','9988776655','#34,Gandhi Road,JP Nagar,Bangalore-78',2)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P2','Indravadhan','Sarabhai','1957-05-10','M','9956745655','#34,Gandhi Road,JP Nagar,Bangalore-78',2)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P3','Rosesh','Sarabhai','1980-08-23','M','9688576855','#34,Gandhi Road,JP Nagar,Bangalore-78',2)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P4','Sahil','Sarabhai','1978-11-5','M','9582378655','#37,Gandhi Road,JP Nagar,Bangalore-78',2)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P5','Monisha','Sarabhai','1960-03-17','F','9763498654','#37,Gandhi Road,JP Nagar,Bangalore-78',2)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P6','Naina','Talwar','1980-05-03','F','9886716297','A-412,Rose Aptmts,Bannerghatta,Bangalore-62',5)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P7','Kabir','Thapar','1980-12-28','M','9458159359','A-412,Rose Aptmts,Bannerghatta,Bangalore-62',5)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P8','Gabbar','Singh','1945-06-15','M','9458258379','#33,Ramgad Nivas,Banashankari,Bangalore-57',3)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P9','Veeru','Dharmendra','1955-10-20','M','9458259457','#22,Ramgad Nivas,Banashankari,Bangalore-57',3)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P10','Jay','Bachchan','1955-05-10','M','8457259658','#22,Ramgad Nivas,Banashankari,Bangalore-57',3)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P11','Ranchod Das','Chanchad','1985-07-18','M','8256279758','#12,IIT-JEE Layout,Jayanagar,Bangalore-48',1)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P12','Raju','Rastogi','1985-09-30','M','8455273953','#17,IIT-JEE Layout,Jayanagar,Bangalore-48',1)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P13','Farhan','Qureshi','1985-01-05','M','9256378758','#20,IIT-JEE Layout,Jayanagar,Bangalore-48',1)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P14','Viru','Sahastrabuddhe','1955-03-02','M','9457253759','#1,IIT-JEE Layout,Jayanagar,Bangalore-48',1)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P15','Geet','Kaur','1990-04-05','F','9367386925','B-101,Brigade Aptmts,Basavanagudi,Bangalore-85',4)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P16','Rahul','Sharma','1970-10-22','M','8368388985','#5,DDLJ Layout,Basavanagudi,Bangalore-85',4)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P17','Anjali','Singh','1972-05-20','F','9589508047','#10,DDLJ Layout,Basavanagudi,Bangalore-85',4)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P18','Tina','Khanna','1970-04-05','F','8145164703','#15,KH Nagar,Basavanagudi,Bangalore-85',4)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P19','Bagvati','Pursoon','1999-02-27','F','8256275814','#7,Patel Marg,Basavanagudi,Bangalore-85',4)")
    conn.commit()
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES ('P20','Rajnikanth','Ganapathy','1950-04-18','M','9478497296','A-001,Brigade Aptmts,Basavanagudi,Bangalore-85',4)")
    conn.commit()
    
def insert_sample_locations():
    conn.execute("INSERT INTO location(l_id, l_name, l_address, w_no) VALUES ('L1','Manyata Tech Park','#2,Vajpayee Road, Bannerghatta,Bangalore-62',5)")
    conn.commit()
    conn.execute("INSERT INTO location(l_id, l_name, l_address, w_no) VALUES ('L2','Innisfree House School','#8,Ranga Shankara Layout,JP Nagar,Bangalore-78',2)")
    conn.commit()
    conn.execute("INSERT INTO location(l_id, l_name, l_address, w_no) VALUES ('L3','Everfine Supermarket','#3,Kothanur Dinne Main Road,JP Nagar,Bangalore-78',2)")
    conn.commit()
    conn.execute("INSERT INTO location(l_id, l_name, l_address, w_no) VALUES ('L4','Bikaneri Sweets','#7,Arekere Layout,Bannerghatta,Bangalore-62',5)")
    conn.commit()
    conn.execute("INSERT INTO location(l_id, l_name, l_address, w_no) VALUES ('L5','Banashankari Bus Stand','Temple Circle, Banashankari,Bangalore-57',3)")
    conn.commit()
    
def insert_sample_hospital():
    conn.execute("INSERT INTO hospital(h_id, h_name, h_address, w_no) VALUES ('H1','St.Johns Hospital','#45,Bannerghatta Main Road,Bannerghatta,Bangalore-62',5)")
    conn.commit()
    conn.execute("INSERT INTO hospital(h_id, h_name, h_address, w_no) VALUES ('H2','Apollo Hospital','#5,Marenahalli,Jayanagar,Bangalore-48',1)")
    conn.commit()
    conn.execute("INSERT INTO hospital(h_id, h_name, h_address, w_no) VALUES ('H3','Hindustan Hospital','#4,Patel Marg,Basavanagudi,Bangalore-85',4)")
    conn.commit()

def insert_sample_patient():
    conn.execute("INSERT INTO patient(pat_id, tested_pdate, discharge_date, p_id, h_id, i_id) VALUES ('PAT1','2020-03-15',NULL,'P3','H2',NULL)")
    conn.commit()
    conn.execute("INSERT INTO patient(pat_id, tested_pdate, discharge_date, p_id, h_id, i_id) VALUES ('PAT2','2020-03-22',NULL,'P8','H3',NULL)")
    conn.commit()
    conn.execute("INSERT INTO patient(pat_id, tested_pdate, discharge_date, p_id, h_id, i_id) VALUES ('PAT3','2020-03-29',NULL,'P14','H2',NULL)")
    conn.commit()
    conn.execute("INSERT INTO patient(pat_id, tested_pdate, discharge_date, p_id, h_id, i_id) VALUES ('PAT4','2020-04-05',NULL,'P18','H3',NULL)")
    conn.commit()
    conn.execute("INSERT INTO patient(pat_id, tested_pdate, discharge_date, p_id, h_id, i_id) VALUES ('PAT5','2020-04-3',NULL,'P1','H2',NULL)")
    conn.commit()
    conn.execute("INSERT INTO patient(pat_id, tested_pdate, discharge_date, p_id, h_id, i_id) VALUES ('PAT6','2020-03-25',NULL,'P7','H1',NULL)")
    conn.commit()
    conn.execute("INSERT INTO patient(pat_id, tested_pdate, discharge_date, p_id, h_id, i_id) VALUES ('PAT7','2020-04-10',NULL,'P16','H3',NULL)")
    conn.commit()
    conn.execute("INSERT INTO patient(pat_id, tested_pdate, discharge_date, p_id, h_id, i_id) VALUES ('PAT8','2020-04-17',NULL,'P15','H3',NULL)")
    conn.commit()
    
def update_sample_patient():
    conn.execute("UPDATE patient SET i_id='PAT1' WHERE pat_id='PAT5'")
    conn.commit()
    conn.execute("UPDATE patient SET i_id='PAT3' WHERE pat_id='PAT1'")
    conn.commit()
    conn.execute("UPDATE patient SET i_id='PAT3' WHERE pat_id='PAT2'")
    conn.commit()
    conn.execute("UPDATE patient SET i_id='PAT4' WHERE pat_id='PAT7'")
    conn.commit()
    conn.execute("UPDATE patient SET i_id='PAT4' WHERE pat_id='PAT8'")
    conn.commit()
    
def insert_sample_contacts():
    conn.execute("INSERT INTO contact(c_id, p_id) VALUES ('C1','P2'),('C2','P4'),('C3','P5'),('C4','P6'),('C5','P9'),('C6','P10'),('C7','P11'),('C8','P12'),('C9','P13'),('C10','P17')")
    conn.commit()
    
def insert_sample_travelfrom():
    conn.execute("INSERT INTO travel_from(pat_id, cy_id, arrival_date) VALUES ('PAT3','CY2','2020-03-15')")
    conn.commit()
    conn.execute("INSERT INTO travel_from(pat_id, cy_id, arrival_date) VALUES ('PAT4','CY5','2020-03-20')")
    conn.commit()
    conn.execute("INSERT INTO travel_from(pat_id, cy_id, arrival_date) VALUES ('PAT6','CY3',NULL)")
    conn.commit()
    conn.execute("INSERT INTO travel_from(pat_id, cy_id, arrival_date) VALUES ('PAT6','CY5',NULL)")
    conn.commit()
    conn.execute("INSERT INTO travel_from(pat_id, cy_id, arrival_date) VALUES ('PAT6','CY1','2020-03-25')")
    conn.commit()
    
def insert_sample_visited():
    conn.execute("INSERT INTO visited(pat_id, l_id, visited_date) VALUES ('PAT1','L3','2020-03-07')")
    conn.commit()
    conn.execute("INSERT INTO visited(pat_id, l_id, visited_date) VALUES ('PAT5','L2','2020-03-20')")
    conn.commit()
    conn.execute("INSERT INTO visited(pat_id, l_id, visited_date) VALUES ('PAT5','L2','2020-03-21')")
    conn.commit()
    conn.execute("INSERT INTO visited(pat_id, l_id, visited_date) VALUES ('PAT5','L2','2020-03-22')")
    conn.commit()
    conn.execute("INSERT INTO visited(pat_id, l_id, visited_date) VALUES ('PAT3','L1','2020-03-16')")
    conn.commit()
    conn.execute("INSERT INTO visited(pat_id, l_id, visited_date) VALUES ('PAT3','L1','2020-03-17')")
    conn.commit()
    conn.execute("INSERT INTO visited(pat_id, l_id, visited_date) VALUES ('PAT6','L5','2020-03-25')")
    conn.commit()
    
def insert_sample_interaction():
    conn.execute("INSERT INTO interactions(pat_id, c_id, contacted_on, toc) VALUES ('PAT5','C1','2020-03-10','P')")
    conn.commit()
    conn.execute("INSERT INTO interactions(pat_id, c_id, contacted_on, toc) VALUES ('PAT1','C2','2020-03-10','S')")
    conn.commit()
    conn.execute("INSERT INTO interactions(pat_id, c_id, contacted_on, toc) VALUES ('PAT1','C3','2020-03-10','S')")
    conn.commit()
    conn.execute("INSERT INTO interactions(pat_id, c_id, contacted_on, toc) VALUES ('PAT6','C4','2020-03-25','P')")
    conn.commit()
    conn.execute("INSERT INTO interactions(pat_id, c_id, contacted_on, toc) VALUES ('PAT2','C5','2020-03-20','P')")
    conn.commit()
    conn.execute("INSERT INTO interactions(pat_id, c_id, contacted_on, toc) VALUES ('PAT2','C6','2020-03-20','P')")
    conn.commit()
    conn.execute("INSERT INTO interactions(pat_id, c_id, contacted_on, toc) VALUES ('PAT3','C7','2020-03-23','P')")
    conn.commit()
    conn.execute("INSERT INTO interactions(pat_id, c_id, contacted_on, toc) VALUES ('PAT3','C8','2020-03-24','S')")
    conn.commit()
    conn.execute("INSERT INTO interactions(pat_id, c_id, contacted_on, toc) VALUES ('PAT3','C9','2020-03-24','S')")
    conn.commit()
    conn.execute("INSERT INTO interactions(pat_id, c_id, contacted_on, toc) VALUES ('PAT7','C10','2020-04-01','S')")
    conn.commit()
    
def trigger():
    conn.execute("CREATE TRIGGER person_table_updated2 BEFORE INSERT ON person FOR EACH ROW BEGIN INSERT INTO trigger_test VALUES ('added new person'); END;")
    conn.commit()

def insert_person():
    print("")
    new_p_id=input("Enter the new person's ID : ")
    while(not new_p_id.startswith("P")):
        new_p_id=input("Please enter a valid ID : ")
    new_f_name=input("Enter the person's first name : ")
    new_l_name=input("Enter the person's last name : ")
    new_p_dob=input("Enter the person's date of birth (YYYY-MM-DD) : ")
    new_p_sex=input("Enter the person's sex (F/M) : ")
    new_p_phno=input("Enter the person's phone number : ")
    while(len(new_p_phno)!=10):
        new_p_phno=input("Please enter a valid phone number : ")
    new_p_address=input("Enter the person's address : ")
    new_w_no=input("Enter the ward number the person resides in : ")
    conn.execute("INSERT INTO person(p_id, f_name, l_name, p_dob, p_sex, p_phno, p_address, w_no) VALUES (?,?,?,?,?,?,?,?)",(new_p_id,new_f_name,new_l_name,new_p_dob,new_p_sex,new_p_phno,new_p_address,new_w_no))
    conn.commit()
    print("New person inserted successfully")
    conn.execute("SELECT * FROM trigger_test")
    conn.commit()
    start()
    
def queries():
    #List of wards where patients are residing
1    data1=list(conn.execute("SELECT ward.w_name FROM ward WHERE ward.w_no IN (SELECT person.w_no FROM person WHERE person.p_id IN (SELECT patient.p_id FROM patient))"))
    conn.commit()
    print("Names of wards where patients are residing : \n")
    for i in data1:
        print(i)
    print("")
    #List of wards where contacts are residing
    data2=list(conn.execute("SELECT ward.w_name FROM ward WHERE ward.w_no IN (SELECT person.w_no FROM person WHERE person.p_id IN (SELECT contact.p_id FROM contact))"))
    conn.commit()
    print("Names of wards where primary and secondary contacts are residing : \n")
    for i in data2:
        print(i)
    #List of locations visited by the affected patients
    data3=list(conn.execute("SELECT location.l_name FROM location WHERE location.l_id IN (SELECT visited.l_id FROM visited)"))
    conn.commit()
    print("Names of locations visited by the patient before tested positive : \n")
    for i in data3:
        print(i)
    print("")
    #Countries visited by affected patients
    data4=list(conn.execute("SELECT country.cy_name FROM country WHERE country.cy_id IN (SELECT travel_from.cy_id FROM travel_from)"))
    conn.commit()
    print("Countries travelled to by the patients : \n")
    for i in data4:
        print(i)
    start()
    
def hospital_query():
    hospital=input("Enter the hospital name : ")
    data5=list(conn.execute("SELECT COUNT(pat_id) FROM patient WHERE patient.h_id=(SELECT hospital.h_id FROM hospital WHERE hospital.h_name=?)",(hospital,)))
    conn.commit()
    print(data5)
    start()
    
def ward_query():
    ward=input("Enter the ward name : ")
    data6=list(conn.execute("SELECT COUNT(pat_id) FROM patient WHERE patient.p_id IN (SELECT person.p_id FROM person WHERE person.w_no=(SELECT ward.w_no FROM ward WHERE ward.w_name=?))",(ward,)))
    conn.commit()
    print(data6)
    start()
    
#CREATING TABLES AND TRIGGER AND INSERTING DATA
create_tables()
'''
insert_sample_ward()
insert_sample_country()
insert_sample_person()
insert_sample_locations()
insert_sample_hospital()
insert_sample_patient()
update_sample_patient()
insert_sample_contacts()
insert_sample_travelfrom()
insert_sample_visited()
insert_sample_interaction()
trigger()
'''

def start():
	print("\n PANDEMIC INFORMATION \n")
	print(" Enter 1 to enter a new person's record")
	print(" Enter 2 for general information about the pandemic")
	print(" Enter 3 to get number of patients in a ward")
	print(" Enter 4 to get number of patients admitted in a hospital")
	print("")
	s=int(input("Please enter a number (1/2/3/4) : "))
	while (s!=1 and s!=2 and s!=3 and s!=4):
		s=int(input("Please enter a valid number : "))
	if (s==1):
		insert_person()
	elif (s==2):
		queries()
	elif (s==3):
		ward_query()
	elif (s==4):
		hospital_query()
        
start()
