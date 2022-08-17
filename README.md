# Banking-System
GUI for  banking system with functionalities like creating a new account, login in existing account, changing the password,  deposit and withdrawal of money



System Requirements :
* A Python IDE
* Oracle 11G



Required Modules:
* cx_Oracle
* PIL
* captcha
* tkinter
* random



terminal command to download :

-> cx_Oracle : python -m pip install cx_Oracle --upgrade

-> captcha : pip install captcha

-> PIL : python3 -m pip install --upgrade Pillow



Other Pre-requisite :

-> To store the data into data base first of all we have to create a table in data base. A table using    following query should be created in database.

        • create table bank(account_no varchar2(10),username 
        varchar2(20), password varchar2(20),age number(3),gender 
        varchar2(10),account_type varchar2(10),balance number(15), 
        primary key(account_no));
 
