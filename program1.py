
import pandas as pd
import matplotlib.pyplot as pl

ch=1
while ch!=-1:
    print("#"*60)
    print("\t\t\t  Blood Bank")
    print("#"*60)
    print("1. Blood Group ")
    print("2. Customer ")
    print("3. Employee ")
    print("4. Donor ")
    print("-1 Save and Exit ")
    ch=int(input("Enter your choice "))
    if ch==1:
        # Blood Group
        DF=pd.read_csv("bloodgroups.csv", index_col='bloodgroup')
        print("1.  ")
        print("2. Remove a column ")
        print("3. Add a Row ")
        print("4. Remove a Row")
        print("5. Change the status ")
        print("6. Change number of packets ")
        print("7. Sort by Packets - Ascending ")
        print("8. Sort by Packets - Descending ")
        print("9. Display the info")
        print("10. Display details of available blood groups ")
        print("11. Display details of NA blood groups ")
        print("12. Bar chart - Available stock ")
        print("-1. Save the dataframe and Exit ")
        try:
            opt=int(input("Enter the choice "))
            if opt==1:
                ch=input("Enter the column heading ")
                cd=eval(input("Enter column data as a list "))
                DF[ch]=cd
                print(DF)
                print("Column added successfully")
            elif opt==2:
                cr=input("remove the column heading")
                DF.drop(cr, axis=1, inplace=True)
                print(DF)
                print("column remove successfully")
            elif opt==3:
                rh=input("Enter the row heading ")
                rd=eval(input("Enter row data as a list "))
                DF.loc[rh]=rd
                print(DF)
                print("Row added successfully")
            elif opt==4:
                rr=input("remove the row heading")
                DF.drop(rr, inplace=True)
                print(DF)
                print("Row removed successfully")
            elif opt==5:
                rh=input("Enter the blood group")
                a=input("Mention status - available/ na ")
                if rh in DF.index:
                    DF.loc[rh,'status']=a
                    print(DF)
                    print("Status updated")
                else:
                    print('Enter correct blood group')
            elif opt==6:
                rh=input("Enter the blood group")
                a=input("Mention number of packets ")
                if rh in DF.index:
                    DF.loc[rh,'packets']=a
                    print(DF)
                    print("Packets updated")
                else:
                    print('Enter correct blood group')
            elif opt==7:
                print(DF.sort_values(by="packets"))
            elif opt==8:
                print(DF.sort_values(by="packets",ascending=False))
            elif opt==9:
                print(DF)
            elif opt==10:
                print(DF[DF.status=='available'])
            elif opt==11:
                print(DF[DF.status=='na'])
            elif opt==12:
                pl.bar(DF.index,DF.packets,color="b",width=0.5)
                pl.xlabel('Blood Group')
                pl.ylabel('Number of packets available')
                pl.title('Blood Groups Availability Report ')
                pl.show()
            elif ch==13:
                DF.to_csv("blodgroups.csv")
                print("DataFrame saved successfully")
            else:
                print("enter correct option")
        except:
            print("error in operation")
            print("please try again")
    elif ch==2:
        # Customer
        DF=pd.read_csv("customer.csv",index_col='custid')
        print("1.Add a column")
        print("2.Add a row")
        print("3.Sort by cname-Ascending")
        print("4.Sort by cname-Descending")
        print("5.Display the full DataFrame")
        print("6.Generate bar graph")
        print("7.Generate a line graph")
        print("8.Sort on units-Ascending")
        print("9.Sort on units-Descending")
        print("-1.Save the dataframe the exit")
        try:
            opt=int(input("enter a choice "))
            if opt==1:
                ch=input("enter a column heading")
                cv=eval(input("enter the values in the form of a list"))
                DF[ch]=cv
                print(DF)
                print("column added successfully")
            elif opt==2:
                cr=input("enter the row heading")
                cb=eval(input("enter the values in the form of a list"))
                DF.loc[cr]=cb
                print(DF)
                print("Row added successfully")
            elif opt==3:
                print(DF.sort_values(by="cname"))
            elif opt==4:
                print(DF.sort_values(by="cname" ,ascending=False))
            elif opt==5:
                print(DF)
            elif opt==6:
                x=DF.cname
                y=DF.units
                pl.bar(x,y)
                pl.xlabel('Customer name')
                pl.ylabel('units purchased')
                pl.show()
            elif opt==7:
                x=DF.cname
                y=DF.units
                pl.plot(x,y)
                pl.xlabel('Customer name')
                pl.ylabel('units purchased')
                pl.show()
            elif opt==8:
                print(DF.sort_values (by="units"))
            elif opt==9:
                print(DF.sort_values(by="units",ascending=False))
            elif ch==-1:
                DF.to_csv("customer.csv")
                print("DataFrame saved successfully")
            else:
                print("enter  correct option")
        except:
            print("error in operation")
            print("please try again")
    elif ch==3:
        # Employee
        DF=pd.read_csv("emp.csv",index_col='empno')
        print("1.Display the full DataFrame")
        print("2.Add a column")
        print("3.Add a row")
        print("4.Sort on ename- Ascending")
        print("5.Sort on ename -Descending")
        print("6.Sort on salary -Ascending")
        print("7.Sort on salary -Descending")
        print("8.Generate a bar graph")
        print("9.Generate a line graph")
        print("-1.Save the DataFrame and exit")
        try:
            opt=int(input("enter your choice"))
            if opt==1:
                print(DF)
            elif opt==2:
                ca=input("enter column heading")
                cn=eval(input("enter the values in the form of a list"))
                DF[ca]=cn
                print(DF)
                print("column added successfully")
            elif opt==3:
                rn=input("enter the row heading")
                rs=eval(input("enter the  values in the form of a list"))
                DF.loc[rn]=rs
                print(DF)
                print("row added successfully")
            elif opt==4:
                print(DF.sort_values(by="ename"))
            elif opt==5:
                print(DF.sort_values(by="ename",ascending=False))
            elif opt==6:
                print(DF.sort_values(by="salary"))
            elif opt==7:
                print(DF.sort_values(by="salary",ascending=False))
            elif opt==8:
                x=DF.ename
                y=DF.salary
                pl.bar(x,y)
                pl.xlabel('Name of Employee')
                pl.ylabel('Salary')
                pl.title('Pay Scale of Employees')
                pl.show()
            elif opt==9:
                x=DF.ename
                y=DF.salary
                pl.plot(x,y)
                pl.xlabel('Name of Employee')
                pl.ylabel('Salary')
                pl.title('Pay Scale of Employees')
                pl.show()
            elif opt==-1:
                DF.to_csv("emp.csv")
                print("DataFrame saved successfully")
            else:
                print("enter the correct  option")
        except:
            print("error in operation")
            print("please try again")
    elif ch==4:
        # Donor
        DF=pd.read_csv("donor.csv", index_col='regid')
        print("1.Display a full dataframe")
        print("2.Add a column")
        print("3.Add a row")
        print("4.Generate a bar graph")
        print("5.Generate a histogram")
        print("6.Sort on name-Ascending")
        print("7.Sort on name -Descending")
        print("8.Sort on age -Ascending")
        print("9.Sort on age -Descending")
        print("-1.Save the DataFrame and exit")
        try:
            opt=int(input("enter your choice"))
            if opt==1:
                print(DF)
            elif opt==2:
                cq=input("enter the column heading")
                cv=eval(input("enter thee values in the form of a list"))
                DF[cq]=cv
                print(DF)
                print("Column added successfully")
            elif opt==3:
                ra=input("enter the row heading")
                rv=eval(input("enter the values in the form of a list"))
                DF.loc[ra]=rv
                print(DF)
                print("Row added successfully")
            elif opt==4:
                x=DF.name
                y=DF.age
                pl.bar(x,y)
                pl.xlabel('Name')
                pl.ylabel('Age')
                pl.title('Age of Donors ')
                pl.show()
            elif opt==5:
                x=DF.age
                pl.hist(x)
                pl.xlabel('Age Groups')
                pl.ylabel('No. of Donors')
                pl.title('Age Frequency of Donors')
                pl.show()
            elif opt==6:
                print(DF.sort_values(by="name"))
            elif opt==7:
                print(DF.sort_values(by="name",ascending=False))
            elif opt==8:
                print(DF.sort_values(by="age"))
            elif opt==9:
                print(DF.sort_values(by="age",ascending=False))
            elif opt==-1:
                DF.to_csv("donors.csv")
                print("DataFrame saved successfully")
            else:
                print("enter the correct option")
        except:
            print("error in operation")
            print("please try again")
    elif ch==-1:
        break
    else:
        print("Choose the correct option")

