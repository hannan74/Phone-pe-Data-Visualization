#Importing the necessary libraries
import os
import json
import requests
import pandas as pd
import mysql.connector
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
from moviepy.editor import VideoFileClip
from moviepy.editor import VideoFileClip


################################### CLONING FROM GITHUB ###########################################################
#aggregate_transaction

path1 = "D:/Guvi/Capstone/Phonepe/pulse/data/aggregated/transaction/country/india/state/"
aggregate_transaction_list = os.listdir(path1)

column1 = {'State':[], 'Year':[], 'Quater':[], 'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for state in aggregate_transaction_list:
    state_wise = path1+state+"/"
    aggregate_year_list= os.listdir(state_wise)

    for year in aggregate_year_list:
        year_wise= state_wise+year+"/"
        aggregate_file_list = os.listdir(year_wise)

        for file in aggregate_file_list:
            file_wise= year_wise+file

            data1 = open(file_wise,"r")
            Read1 = json.load(data1)

            for i in Read1['data']['transactionData']:
                name = i['name']
                count = i['paymentInstruments'][0]['count']
                amount = i['paymentInstruments'][0]['amount']
                column1['Transaction_type'].append(name)
                column1['Transaction_count'].append(count)
                column1['Transaction_amount'].append(amount)
                column1['State'].append(state)
                column1['Year'].append(year)
                column1['Quater'].append(int(file.strip(".json")))
                
df_aggregate_transaction = pd.DataFrame(column1)

df_aggregate_transaction['State'] = df_aggregate_transaction['State'].str.replace('-',' ')
df_aggregate_transaction['State'] = df_aggregate_transaction['State'].str.title()
df_aggregate_transaction['State'] = df_aggregate_transaction['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')


#aggregate_user

path2 = "D:/Guvi/Capstone/Phonepe/pulse/data/aggregated/user/country/india/state/"
aggregate_user_list = os.listdir(path2)

column2 = {'State':[], 'Year':[], 'Quater':[], 'User_Brand':[], 'User_Brand_count':[], 'Brand_Percentage':[]}


for state in aggregate_user_list:
    state_wise = path2+state+"/"
    aggregate_year_list= os.listdir(state_wise)

    for year in aggregate_year_list:
        year_wise= state_wise+year+"/"
        aggregate_file_list = os.listdir(year_wise)

        for file in aggregate_file_list:
            file_wise= year_wise+file

            data2 = open(file_wise,"r")
            Read2 = json.load(data2)

            try:
                for i in Read2["data"]['usersByDevice']:
                    user_brand = i['brand']
                    user_count = i['count']
                    percentage = i['percentage'] #Percentage of share of current device type compared to all devices.
                    column2['User_Brand'].append(user_brand)
                    column2['User_Brand_count'].append(user_count)
                    column2['Brand_Percentage'].append(percentage)
                    column2['State'].append(state)
                    column2['Year'].append(year)
                    column2['Quater'].append(int(file.strip(".json")))
            except:
                pass

df_aggregate_user = pd.DataFrame(column2)

df_aggregate_user['State'] = df_aggregate_user['State'].str.replace('-',' ')
df_aggregate_user['State'] = df_aggregate_user['State'].str.title()
df_aggregate_user['State'] = df_aggregate_user['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')


#map_transaction

path3= "D:/Guvi/Capstone/Phonepe/pulse/data/map/transaction/hover/country/india/state/"
map_transaction_list = os.listdir(path3)

column3 = {'State':[], 'Year':[], 'Quater':[], 'District':[], 'Transaction_count':[], 'Transaction_amount':[]}

for state in map_transaction_list:
    state_wise = path3+state+"/"
    map_year_list= os.listdir(state_wise)

    for year in map_year_list:
        year_wise= state_wise+year+"/"
        map_file_list = os.listdir(year_wise)

        for file in map_file_list:
            file_wise= year_wise+file

            data3 = open(file_wise,"r")
            Read3 = json.load(data3)

            for i in Read3["data"]['hoverDataList']:
                district_name = i['name']
                transaction_count = i['metric'][0]['count']
                transaction_amount = i['metric'][0]['amount']
                column3['District'].append(district_name)
                column3['Transaction_count'].append(transaction_count)
                column3['Transaction_amount'].append(transaction_amount)
                column3['State'].append(state)
                column3['Year'].append(year)
                column3['Quater'].append(int(file.strip(".json")))

df_map_transaction = pd.DataFrame(column3)

df_map_transaction['State'] = df_map_transaction['State'].str.replace('-',' ')
df_map_transaction['State'] = df_map_transaction['State'].str.title()
df_map_transaction['State'] = df_map_transaction['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')


#map_user

path4 = "D:/Guvi/Capstone/Phonepe/pulse/data/map/user/hover/country/india/state/"
map_user_list = os.listdir(path4)

column4 = {'State':[], 'Year':[], 'Quater':[], 'District':[], 'Registered_Users':[], 'App_Opens':[]}

for state in map_user_list:
    state_wise = path4+state+"/"
    map_year_list= os.listdir(state_wise)

    for year in map_year_list:
        year_wise= state_wise+year+"/"
        map_file_list = os.listdir(year_wise)

        for file in map_file_list:
            file_wise= year_wise+file

            data4 = open(file_wise,"r")
            Read4 = json.load(data4)

            for i in Read4['data']['hoverData'].items():
                district_name = i[0]
                user_count = i[1]['registeredUsers']
                app_opens = i[1]['appOpens']
                column4['District'].append(district_name)
                column4['Registered_Users'].append(user_count)
                column4['App_Opens'].append(app_opens)
                column4['State'].append(state)
                column4['Year'].append(year)
                column4['Quater'].append(int(file.strip(".json")))

df_map_user = pd.DataFrame(column4)

df_map_user['State'] = df_map_user['State'].str.replace('-',' ')
df_map_user['State'] = df_map_user['State'].str.title()
df_map_user['State'] = df_map_user['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')


#top_transaction

path5 = "D:/Guvi/Capstone/Phonepe/pulse/data/top/transaction/country/india/state/"
top_transaction_list = os.listdir(path5)

column5 = {'State':[], 'Year':[], 'Quater':[], 'Pincode':[], 'Transaction_count':[], 'Transaction_amount':[]}

for state in top_transaction_list:
    state_wise = path5+state+"/"
    top_year_list= os.listdir(state_wise)

    for year in top_year_list:
        year_wise= state_wise+year+"/"
        top_file_list = os.listdir(year_wise)

        for file in top_file_list:
            file_wise= year_wise+file

            data5 = open(file_wise,"r")
            Read5 = json.load(data5)

            for i in Read5['data']['pincodes']:
                pincode= i['entityName']
                transaction_count = i['metric']['count']
                transaction_amount = i['metric']['amount']
                column5['Pincode'].append(pincode)
                column5['Transaction_count'].append(transaction_count)
                column5['Transaction_amount'].append(transaction_amount)
                column5['State'].append(state)
                column5['Year'].append(year)
                column5['Quater'].append(int(file.strip(".json")))

df_top_transaction = pd.DataFrame(column5)

df_top_transaction['State'] = df_top_transaction['State'].str.replace('-',' ')
df_top_transaction['State'] = df_top_transaction['State'].str.title()
df_top_transaction['State'] = df_top_transaction['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')


#top_user

path6 = "D:/Guvi/Capstone/Phonepe/pulse/data/top/user/country/india/state/"
top_user_list = os.listdir(path6)

column6 = {'State':[], 'Year':[], 'Quater':[], 'Pincode':[], 'User_count':[]}

for state in top_user_list:
    state_wise = path6+state+"/"
    top_year_list= os.listdir(state_wise)

    for year in top_year_list:
        year_wise= state_wise+year+"/"
        top_file_list = os.listdir(year_wise)

        for file in top_file_list:
            file_wise= year_wise+file

            data6 = open(file_wise,"r")
            Read6 = json.load(data6)

            for i in Read6['data']['pincodes']:
                pincode= i['name']
                user_count = i['registeredUsers']
                column6['Pincode'].append(pincode)
                column6['User_count'].append(user_count)
                column6['State'].append(state)
                column6['Year'].append(year)
                column6['Quater'].append(int(file.strip(".json")))


df_top_user= pd.DataFrame(column6)

df_top_user['State'] = df_top_user['State'].str.replace('-',' ')
df_top_user['State'] = df_top_user['State'].str.title()
df_top_user['State'] = df_top_user['State'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')


######################################### UPLOAD TO MYSQL ###########################################################


#df to sql

#aggregated_transaction

mydb = mysql.connector.connect(host ='localhost',user='root',password='7ApriL@2002',database='phonepe')
mycursor=mydb.cursor()

query1 = '''create table if not exists aggregated_transaction(State varchar(150),
                                                            Year int,
                                                            Quater int,
                                                            Transaction_type varchar(150),
                                                            Transaction_count bigint,
                                                            Transaction_amount bigint)'''

mycursor.execute(query1) 
mydb.commit()

insert_query1 = '''insert into aggregated_transaction (State,
                                                        Year,
                                                        Quater,
                                                        Transaction_type,
                                                        Transaction_count,
                                                        Transaction_amount)
                                                        
                                                        values(%s, %s, %s, %s, %s, %s)'''

list1= df_aggregate_transaction.values.tolist()
mycursor.executemany(insert_query1,list1)
mydb.commit()


#aggregated_user

query2 = '''create table if not exists aggregated_user(State varchar(150),
                                                        Year int,
                                                        Quater int,
                                                        User_Brand varchar(150),
                                                        User_Brand_count bigint,
                                                        Brand_Percentage float)'''

mycursor.execute(query2) 
mydb.commit()

insert_query2 = '''insert into aggregated_user (State,
                                                Year,
                                                Quater,
                                                User_Brand,
                                                User_Brand_count,
                                                Brand_Percentage)
                                                
                                                values(%s, %s, %s, %s, %s, %s)'''

list2= df_aggregate_user.values.tolist()
mycursor.executemany(insert_query2,list2)
mydb.commit()


#map_transaction

query3 = '''create table if not exists map_transaction(State varchar(150),
                                                        Year int,
                                                        Quater int,
                                                        District varchar(150),
                                                        Transaction_count bigint,
                                                        Transaction_amount bigint)'''

mycursor.execute(query3) 
mydb.commit()

insert_query3 = '''insert into map_transaction (State,
                                                Year,
                                                Quater,
                                                District,
                                                Transaction_count,
                                                Transaction_amount)
                                                
                                                values(%s, %s, %s, %s, %s, %s)'''

list3= df_map_transaction.values.tolist()
mycursor.executemany(insert_query3,list3)
mydb.commit()


#map_user

query4 = '''create table if not exists map_user(State varchar(150),
                                                Year int,
                                                Quater int,
                                                District varchar(150),
                                                Registered_Users bigint,
                                                App_Opens bigint)'''

mycursor.execute(query4) 
mydb.commit()

insert_query4 = '''insert into map_user (State,
                                        Year,
                                        Quater,
                                        District,
                                        Registered_Users,
                                        App_Opens)
                                        
                                        values(%s, %s, %s, %s, %s, %s)'''

list4= df_map_user.values.tolist()
mycursor.executemany(insert_query4,list4)
mydb.commit()

#top_transaction

query5 = '''create table if not exists top_transaction(State varchar(150),
                                                        Year int,
                                                        Quater int,
                                                        Pincode bigint,
                                                        Transaction_count bigint,
                                                        Transaction_amount bigint)'''

mycursor.execute(query5) 
mydb.commit()

insert_query5 = '''insert into top_transaction (State,
                                                Year,
                                                Quater,
                                                Pincode,
                                                Transaction_count,
                                                Transaction_amount)
                                                
                                                values(%s, %s, %s, %s, %s, %s)'''

list5= df_top_transaction.values.tolist()
mycursor.executemany(insert_query5,list5)
mydb.commit()

#top_user


query6 = '''create table if not exists top_user(State varchar(150),
                                                Year int,
                                                Quater int,
                                                Pincode bigint,
                                                User_count bigint)'''

mycursor.execute(query6) 
mydb.commit()

insert_query6 = '''insert into top_user (State,
                                        Year,
                                        Quater,
                                        Pincode,
                                        User_count)
                                        
                                        values(%s, %s, %s, %s, %s)'''

list6= df_top_user.values.tolist()
mycursor.executemany(insert_query6,list6)
mydb.commit()


#dataframe 
#from sql to dataframe

mydb = mysql.connector.connect(host ='localhost',user='root',password='7ApriL@2002',database='phonepe')
mycursor=mydb.cursor()

#aggre_transaction

mycursor.execute("SELECT * FROM aggregated_transaction")
df1 = mycursor.fetchall()
mydb.commit()


Aggre_Transaction = pd.DataFrame(df1, columns=("State","Year","Quater","Transaction_type","Transaction_count","Transaction_amount"))

#aggre_user

mycursor.execute("SELECT * FROM aggregated_user")
df2 = mycursor.fetchall()
mydb.commit()


Aggre_User = pd.DataFrame(df2, columns=("State","Year","Quater","User_Brand","User_Brand_count","Brand_Percentage"))

#map_transaction

mycursor.execute("SELECT * FROM map_transaction")
df3 = mycursor.fetchall()
mydb.commit()


Map_Transaction = pd.DataFrame(df3, columns=("State","Year","Quater","District","Transaction_count","Transaction_amount"))

#map_user

mycursor.execute("SELECT * FROM map_user")
df4 = mycursor.fetchall()
mydb.commit()


Map_User = pd.DataFrame(df4, columns=("State","Year","Quater","District","Registered_Users","App_Opens"))

#top_transaction

mycursor.execute("SELECT * FROM top_transaction")
df5 = mycursor.fetchall()
mydb.commit()


Top_Transaction = pd.DataFrame(df5, columns=("State","Year","Quater","Pincode","Transaction_count","Transaction_amount"))

#top_user

mycursor.execute("SELECT * FROM top_user")
df6 = mycursor.fetchall()
mydb.commit()


Top_User = pd.DataFrame(df6, columns=("State","Year","Quater","Pincode","User_count"))


######################################## PLOTTING #################################


###### Transaction Amount Count ####### 

#Year

def Transaction_amount_count_year(df, year):
    plot1_y=df[df["Year"] == year] 
    plot1_y.reset_index(drop=True, inplace=True)

    plot1_y_g = plot1_y.groupby("State")[["Transaction_count","Transaction_amount"]].sum()
    plot1_y_g.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        pl_amount = px.bar(plot1_y_g,x="State",y="Transaction_amount", title=f"{year} TRANSACTION AMOUNT", 
                        color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 700, width= 700)
        st.plotly_chart(pl_amount)
    with col2:
        pl_count = px.bar(plot1_y_g,x="State",y="Transaction_count", title=f"{year} TRANSACTION COUNT", 
                        color_discrete_sequence=px.colors.sequential.Bluered_r, height= 700, width= 700)
        st.plotly_chart(pl_count)

    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response = requests.get(url)
    json_1 = json.loads(response.content)
    ST_Name = []
    for feature in json_1["features"]:
        ST_Name.append(feature["properties"]["ST_NM"])

    ST_Name.sort()

    clo1,clo2 = st.columns(2)
    with clo1:
        pl_india1= px.choropleth(plot1_y_g, geojson=json_1, locations="State", featureidkey="properties.ST_NM", 
                                color="Transaction_amount", color_continuous_scale="Rainbow", 
                                range_color= (plot1_y_g["Transaction_amount"].min(), plot1_y_g["Transaction_amount"].max()),
                                hover_name= "State", title=f"{year} TRANSACTION AMOUNT", fitbounds= "locations",
                                height= 700, width= 700)
        
        pl_india1.update_geos(visible= False)
        st.plotly_chart(pl_india1)

    with clo2:
        pl_india2= px.choropleth(plot1_y_g, geojson=json_1, locations="State", featureidkey="properties.ST_NM", 
                                color="Transaction_count", color_continuous_scale="Rainbow", 
                                range_color= (plot1_y_g["Transaction_count"].min(), plot1_y_g["Transaction_count"].max()),
                                hover_name= "State", title=f"{year} TRANSACTION COUNT", fitbounds= "locations",
                                height= 700, width= 700)
        
        pl_india2.update_geos(visible= False)
        st.plotly_chart(pl_india2)

    return plot1_y

#State
def AgTr_Trans_Type(df,state):

    plot1_y=df[df["State"] == state] 
    plot1_y.reset_index(drop=True, inplace=True)

    plot1_y_g = plot1_y.groupby("Transaction_type")[["Transaction_count","Transaction_amount"]].sum()
    plot1_y_g.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        pl_pie1 = px.pie(data_frame= plot1_y_g, names= "Transaction_type", values= "Transaction_amount", width= 700,
                        title= f"{state.upper()} TRANSACTION AMOUNT", hole= 0.45)
        st.plotly_chart(pl_pie1)

    with col2:
        pl_pie2 = px.pie(data_frame= plot1_y_g, names= "Transaction_type", values= "Transaction_count", width= 700,
                        title= f"{state.upper()} TRANSACTION COUNT", hole= 0.45)
        st.plotly_chart(pl_pie2)

#Quater
def Transaction_amount_count_year_quater(df, quater):
    plot1_y=df[df["Quater"] == quater] 
    plot1_y.reset_index(drop=True, inplace=True)

    plot1_y_g = plot1_y.groupby("State")[["Transaction_count","Transaction_amount"]].sum()
    plot1_y_g.reset_index(inplace=True)

    col1,col2= st.columns(2)

    with col1:
        pl_amount = px.bar(plot1_y_g,x="State",y="Transaction_amount", title=f"{plot1_y['Year'].min()} YEAR {quater} QUATER TRANSACTION AMOUNT", 
                        color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 700, width= 700)
        st.plotly_chart(pl_amount)
    
    with col2:
        pl_count = px.bar(plot1_y_g,x="State",y="Transaction_count", title=f"{plot1_y['Year'].min()} YEAR {quater} QUATER TRANSACTION COUNT", 
                        color_discrete_sequence=px.colors.sequential.Bluered_r, height= 700, width= 700)
        st.plotly_chart(pl_count)

    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response = requests.get(url)
    json_1 = json.loads(response.content)
    ST_Name = []
    for feature in json_1["features"]:
        ST_Name.append(feature["properties"]["ST_NM"])

    ST_Name.sort()

    col1,col2 = st.columns(2)
    with col1:
        pl_india1= px.choropleth(plot1_y_g, geojson=json_1, locations="State", featureidkey="properties.ST_NM", 
                                color="Transaction_amount", color_continuous_scale="Rainbow", 
                                range_color= (plot1_y_g["Transaction_amount"].min(), plot1_y_g["Transaction_amount"].max()),
                                hover_name= "State", title=f"{plot1_y['Year'].min()} YEAR {quater} QUATER TRANSACTION AMOUNT", fitbounds= "locations",
                                height= 700, width= 700)
        
        pl_india1.update_geos(visible= False)
        st.plotly_chart(pl_india1)

    with col2:
        pl_india2= px.choropleth(plot1_y_g, geojson=json_1, locations="State", featureidkey="properties.ST_NM", 
                                color="Transaction_count", color_continuous_scale="Rainbow", 
                                range_color= (plot1_y_g["Transaction_count"].min(), plot1_y_g["Transaction_count"].max()),
                                hover_name= "State", title=f"{plot1_y['Year'].min()} YEAR {quater} QUATER TRANSACTION COUNT", fitbounds= "locations",
                                height= 700, width= 700)
        
        pl_india2.update_geos(visible= False)
        st.plotly_chart(pl_india2)

    return plot1_y


#aggregated user chart
#aggre user - year

def Aggre_User_Br_Cou_Y(df, year):
    plot2_y = df[df["Year"]== year]
    plot2_y.reset_index(drop = True, inplace= True)
    plot2_y_g = pd.DataFrame(plot2_y.groupby("User_Brand")["User_Brand_count"].sum())
    plot2_y_g.reset_index(inplace = True)

    pl_bar1 = px.bar(plot2_y_g, x= "User_Brand", y= "User_Brand_count", title = f"{year} BRANDS AND THEIR COUNT",
                        width = 1200, color_discrete_sequence= px.colors.sequential.dense_r)
    st.plotly_chart(pl_bar1)

    return plot2_y


#aggre user- year - quarter
def Aggre_User_br_cou_Y_Quar(df, quater):
    plot2_y_q = df[df["Quater"]== quater]
    plot2_y_q.reset_index(drop = True, inplace= True)

    plot2_y_q_g = pd.DataFrame(plot2_y_q.groupby("User_Brand")["User_Brand_count"].sum())
    plot2_y_q_g.reset_index(inplace=True)

    pl_bar2 = px.bar(plot2_y_q_g, x= "User_Brand", y= "User_Brand_count", title = f"{quater}-QUARTER BRANDS AND THEIR COUNT",
                        width = 1200, color_discrete_sequence= px.colors.sequential.Greens_r)
    st.plotly_chart(pl_bar2)

    return plot2_y_q

#Aggre user year-quarter-state
def Aggre_User_br_cou_Y_Quar_State(df, state):
    plot2_y_q_s = df[df["State"]== state]
    plot2_y_q_s.reset_index(drop = True, inplace= True)

    pl_line1= px.line(plot2_y_q_s, x= "User_Brand", y= "User_Brand_count", hover_data= "Brand_Percentage", title= f"{state.upper()}- BRAND COUNT AND PERCENTAGE",
                    color_discrete_sequence= px.colors.sequential.Jet_r, width= 1200, markers= True)
    st.plotly_chart(pl_line1)


#Map_Transaction District
def MapTr_District(df,state):

    plot1_y=df[df["State"] == state] 
    plot1_y.reset_index(drop=True, inplace=True)

    plot1_y_g = plot1_y.groupby("District")[["Transaction_count","Transaction_amount"]].sum()
    plot1_y_g.reset_index(inplace=True)

    col1,col2= st.columns(2)
    with col1:
        pl_bar1 = px.bar(plot1_y_g, x="Transaction_amount", y="District", orientation= "h", height= 650,
                        title = f"{state.upper()}-DISTRICT AND TRANSACTION AMOUNT", color_discrete_sequence= px.colors.sequential.Mint_r)
        st.plotly_chart(pl_bar1)

    with col2:
        pl_bar2 = px.bar(plot1_y_g, x="Transaction_count", y="District", orientation= "h", height= 650,
                        title = f"{state.upper()}-DISTRICT AND TRANSACTION COUNT", color_discrete_sequence= px.colors.sequential.Bluered_r)
        st.plotly_chart(pl_bar2)


#Map User-Year 

def Map_User_year(df, year):

    map_user_y = df[df["Year"]== year]
    map_user_y.reset_index(drop = True, inplace= True)

    map_user_y_g = map_user_y.groupby("State")[["Registered_Users", "App_Opens"]].sum()
    map_user_y_g.reset_index(inplace = True)

    m_u_pl_line1 = px.line(map_user_y_g, x="State", y=["Registered_Users", "App_Opens"], title= f"{year} - REGISTERED USER & APP OPENS",
                        height= 800, width= 1200, markers= True)
    st.plotly_chart(m_u_pl_line1)

    return map_user_y

#Map User-Year - Quater

def Map_User_year_quater(df, quater):

    map_user_y_q = df[df["Quater"]== quater]
    map_user_y_q.reset_index(drop = True, inplace= True)

    map_user_y_q_g = map_user_y_q.groupby("State")[["Registered_Users", "App_Opens"]].sum()
    map_user_y_q_g.reset_index(inplace = True)

    m_u_pl_line2 = px.line(map_user_y_q_g, x="State", y=["Registered_Users", "App_Opens"], title= f"{df['Year'].min()} - {quater} QUATER REGISTERED USER & APP OPENS",
                        height= 800, width= 1200, markers= True, color_discrete_sequence= px.colors.sequential.Jet_r)
    st.plotly_chart(m_u_pl_line2)

    return map_user_y_q


#Map User-Year - Quater - State

def Map_User_year_quater_state(df, state):
    map_user_y_q_s = df[df["State"]== state]
    map_user_y_q_s.reset_index(drop = True, inplace= True)

    col1,col2= st.columns(2)
    with col1:

        pl_mu_bar1= px.bar(map_user_y_q_s, x="Registered_Users", y="District", orientation= "h", height= 700, 
                        color_discrete_sequence= px.colors.sequential.Mint_r, title= f"{state.upper()} - REGISTERED USERS")
        st.plotly_chart(pl_mu_bar1)

    with col2:

        pl_mu_bar2= px.bar(map_user_y_q_s, x="App_Opens", y="District", orientation= "h", height= 700, 
                        color_discrete_sequence= px.colors.sequential.Rainbow, title= f"{state.upper()} - APP OPENS")
        st.plotly_chart(pl_mu_bar2)


#Top Transaction Year State with Quater and pincode combined

def Top_Trans_year_state(df, state):

    top_trans_y = df[df["State"]== state]
    top_trans_y.reset_index(drop = True, inplace= True)

    top_trans_y_g = top_trans_y.groupby("Pincode")[["Transaction_count", "Transaction_amount"]].sum()
    top_trans_y_g.reset_index(inplace = True)

    col1,col2= st.columns(2)
    with col1:
        pl_tt_bar1= px.bar(top_trans_y, x="Quater", y="Transaction_amount", height= 750, hover_data= "Pincode", 
                        color_discrete_sequence= px.colors.sequential.Oranges_r , title= f"{df['Year'].min()} - {state.upper()} - TRANSACTION AMOUNT")
        st.plotly_chart(pl_tt_bar1)

    with col2:
        pl_tt_bar2= px.bar(top_trans_y, x="Quater", y="Transaction_count", height= 750, hover_data= "Pincode", 
                        color_discrete_sequence= px.colors.sequential.GnBu_r , title= f"{df['Year'].min()} - {state.upper()} - TRANSACTION COUNT")
        st.plotly_chart(pl_tt_bar2)


#Top User - year - grouping : State and quater

def Top_User_year(df, year):
    top_user_y = df[df["Year"]== year]
    top_user_y.reset_index(drop = True, inplace= True)

    top_user_y_g = pd.DataFrame(top_user_y.groupby(["State", "Quater"])["User_count"].sum())
    top_user_y_g.reset_index(inplace = True)

    pl_tu_bar1= px.bar(top_user_y_g, x="State", y="User_count", height= 800, width= 1200, color= "Quater", 
                    color_discrete_sequence= px.colors.sequential.Pinkyl_r , hover_name= "State", title= f"{year} - USER COUNT")
    st.plotly_chart(pl_tu_bar1)

    return top_user_y


#Top user year State

def Top_user_year_state(df, state):
    top_user_y_s = df[df["State"]== state]
    top_user_y_s.reset_index(drop = True, inplace= True)

    pl_tu_bar2= px.bar(top_user_y_s, x="Quater", y="User_count", height= 800, width= 1200, color= "User_count", 
                    color_continuous_scale= px.colors.sequential.Magenta_r , hover_name= "Pincode", title= f"{state.upper()} - USER COUNT")
    st.plotly_chart(pl_tu_bar2)



################# INSIGHTS #######################

def insights_top_aggre_map_tran_amo(table_name):
    mydb = mysql.connector.connect(host ='localhost',user='root',password='7ApriL@2002',database='phonepe')
    mycursor=mydb.cursor()

    query1= f'''select State, sum(Transaction_amount) as Transaction_Amount from {table_name} 
                group by State 
                order by Transaction_amount desc 
                limit 10;'''

    mycursor.execute(query1)
    table1= mycursor.fetchall()
    mydb.commit()

    df1= pd.DataFrame(table1, columns=("STATES", "TRANSACTION_AMOUNT"))
    st.write(df1)

    qu_bar1 = px.bar(df1, x="STATES" ,y="TRANSACTION_AMOUNT", title=f"TRANSACTION AMOUNT OF TOP 10 STATES", hover_name= "STATES",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl_r, height= 700, width= 1200)
    return st.plotly_chart(qu_bar1)


#What are the Pincodes having Top 10 User Count in Top_users?

def insights_topusers_user_count():
    mydb = mysql.connector.connect(host ='localhost',user='root',password='7ApriL@2002',database='phonepe')
    mycursor=mydb.cursor()

    query2= '''select State, Pincode, sum(User_count) as Total_User_Count from top_user 
                group by Pincode, State 
                order by Total_User_Count desc 
                limit 10;'''

    mycursor.execute(query2)
    table2= mycursor.fetchall()
    mydb.commit()

    df2= pd.DataFrame(table2, columns=("STATES", "PINCODE", "TOTAL_USER_COUNT"))
    st.write(df2)

    qu2_bar1 = px.bar(df2, x="STATES" ,y="TOTAL_USER_COUNT", title=f"TOTAL USER COUNT OF TOP 10 STATES", hover_name= "PINCODE",
                        color_discrete_sequence=px.colors.sequential.Bluered_r , height= 700, width= 1200)
    return st.plotly_chart(qu2_bar1)


#What are the the Pincodes having Top 10 Transaction_Amount and Transaction_Count in Top_Transaction?

def insights_toptrans_amount_count():
    mydb = mysql.connector.connect(host ='localhost',user='root',password='7ApriL@2002',database='phonepe')
    mycursor=mydb.cursor()

    query3 = '''select State, Pincode, sum(Transaction_amount) as Transaction_amount from top_transaction
                group by Pincode, State 
                order by Transaction_amount desc 
                limit 10;'''

    mycursor.execute(query3)
    table3= mycursor.fetchall()
    mydb.commit()

    col1,col2= st.columns(2)
    with col1:
        df3= pd.DataFrame(table3, columns=("STATES", "PINCODE", "TRANSACTION_AMOUNT"))
        st.write('TRANSACTION  AMOUNT')
        st.write(df3)

        qu3_bar1 = px.bar(df3, x="STATES" ,y="TRANSACTION_AMOUNT", title=f"TOTAL TRANSACTION AMOUNT OF TOP 10 STATES", hover_name= "PINCODE",
                            color_discrete_sequence=px.colors.sequential.Pinkyl_r , height= 750, width= 750)
        st.plotly_chart(qu3_bar1)

    query3_1 = '''select State, Pincode, sum(Transaction_count) as Transaction_count from top_transaction
                group by Pincode, State 
                order by Transaction_count desc 
                limit 10;'''

    mycursor.execute(query3_1)
    table3_1= mycursor.fetchall()
    mydb.commit()

    with col2:
        df3_1= pd.DataFrame(table3_1, columns=("STATES", "PINCODE", "TRANSACTION_COUNT"))
        st.write('TRANSACTION  COUNT')
        st.write(df3_1)

        qu3_bar2 = px.bar(df3_1, x="STATES" ,y="TRANSACTION_COUNT", title=f"TOTAL TRANSACTION COUNT OF TOP 10 STATES", hover_name= "PINCODE",
                            color_discrete_sequence=px.colors.sequential.Plasma_r , height= 750, width= 750)
        st.plotly_chart(qu3_bar2)



#4.What are the the Districts having Top 10 User_Count and App_Opens by Users in Map_User?

def insights_mapuser_user_opens():
    mydb = mysql.connector.connect(host ='localhost',user='root',password='7ApriL@2002',database='phonepe')
    mycursor=mydb.cursor()

    query4 = '''select State, District, sum(Registered_Users) as Registered_Users from map_user
                group by State, District 
                order by Registered_Users desc
                limit 10;'''

    mycursor.execute(query4)
    table4= mycursor.fetchall()
    mydb.commit()

    col1,col2= st.columns(2)
    with col1:
        df4= pd.DataFrame(table4, columns=("STATES", "DISTRICT", "REGISTERED_USERS"))
        st.write(df4)

        qu4_bar1 = px.bar(df4, x="DISTRICT" ,y="REGISTERED_USERS", title=f"TOTAL REGISTERED USERS OF TOP 10 DISTRICTS", hover_name= "STATES",
                            color_discrete_sequence=px.colors.sequential.Blackbody_r , height= 750, width= 800)
        st.plotly_chart(qu4_bar1)


    query4_1 = '''select State, District, sum(App_Opens) as App_Opens from map_user
                group by State, District 
                order by App_Opens desc
                limit 10;'''

    mycursor.execute(query4_1)
    table4_1= mycursor.fetchall()
    mydb.commit()

    with col2:
        df4_1= pd.DataFrame(table4_1, columns=("STATES", "DISTRICT", "APP_OPENS"))
        st.write(df4_1)

        qu4_bar2 = px.bar(df4_1, x="DISTRICT" ,y="APP_OPENS", title=f"TOTAL APP OPENS BY USERS OF TOP 10 DISTRICTS", hover_name= "STATES",
                            color_discrete_sequence=px.colors.sequential.BuGn_r , height= 750, width= 800)
        st.plotly_chart(qu4_bar2)


#'5.What are the the Districts having Top 10 Transaction_amount in Map_Transaction?'

def insights_maptrans_amount_districtwise():
    mydb = mysql.connector.connect(host ='localhost',user='root',password='7ApriL@2002',database='phonepe')
    mycursor=mydb.cursor()

    query5= '''select State, District, sum(Transaction_amount) as Transaction_amount from map_transaction
                group by State, District
                order by Transaction_amount desc
                limit 10;'''

    mycursor.execute(query5)
    table5= mycursor.fetchall()
    mydb.commit()

    df5 = pd.DataFrame(table5, columns= ("STATES", "DISTRICT", "TRANSACTION_AMOUNT"))
    st.write(df5)

    qu5_bar1=  px.bar(df5, x="DISTRICT" ,y="TRANSACTION_AMOUNT", title=f"TOTAL TRANSACTION AMOUNT OF TOP 10 DISTRICT", hover_name= "STATES",
                            color_discrete_sequence=px.colors.sequential.Agsunset_r , height= 750, width= 1100)
    st.plotly_chart(qu5_bar1)


#6.What are the States of Total Top 10 User_Brand_count in Aggregated_User?

def insights_aggreuser_usercount():
    query6 = '''select State, sum(User_Brand_count) as User_count from aggregated_user
                group by State
                order by User_count desc
                limit 10;'''

    mycursor.execute(query6)
    table6= mycursor.fetchall()
    mydb.commit()

    df6= pd.DataFrame(table6, columns= ("STATES", "USER_COUNT"))
    st.write(df6)

    qu6_bar1= px.bar(df6, x="USER_COUNT" ,y="STATES", title=f"TOTAL USER COUNT OF TOP 10 STATE", hover_name= "STATES", orientation= "h", 
                                color_discrete_sequence=px.colors.sequential.Purp_r , height= 750, width= 1100)
    st.plotly_chart(qu6_bar1)   


#'7.What are the the States having Top 10 Transaction_count in Map_Transaction?'

def insights_maptrans_count():
    query7= '''select State, sum(Transaction_count) as Transaction_count from map_transaction
                    group by State
                    order by Transaction_count desc
                    limit 10;'''

    mycursor.execute(query7)
    table7= mycursor.fetchall()
    mydb.commit()

    df7 = pd.DataFrame(table7, columns= ("STATES", "TRANSACTION_COUNT"))
    st.write(df7)

    qu7_bar1=  px.bar(df7, y="STATES" ,x="TRANSACTION_COUNT", title=f"TOTAL TRANSACTION COUNT OF TOP 10 STATE", hover_name= "STATES", orientation="h", 
                            color_discrete_sequence=px.colors.sequential.Purples_r , height= 750, width= 1100)
    st.plotly_chart(qu7_bar1)


#8.What are the Mobile Brands having Top 10 User_Count in Aggregated_User?'

def insights_agguser_brandcount():
    query8 = '''select User_Brand, sum(User_Brand_count) as User_Count from aggregated_user
                group by User_Brand 
                order by User_Count desc 
                limit 10;'''

    mycursor.execute(query8)
    table8= mycursor.fetchall()
    mydb.commit()

    df8 = pd.DataFrame(table8, columns= ("USER_BRAND", "USER_COUNT"))
    st.write(df8)

    qu8_bar1=  px.bar(df8, y="USER_COUNT" ,x="USER_BRAND", title=f"TOTAL USER COUNT OF TOP 10 BRANDS", hover_name= "USER_BRAND",  
                            color_discrete_sequence=px.colors.sequential.solar_r , height= 750, width= 1100)
    st.plotly_chart(qu8_bar1)


#9.Which Quarter has the highest number of Transaction_amount in Aggregated_Transaction?

def insights_aggretrans_amount_quater():
    query9= '''select Quater, sum(Transaction_amount) as Transaction_amount from aggregated_transaction
                group by Quater 
                order by Transaction_amount desc;'''

    mycursor.execute(query9)
    table9= mycursor.fetchall()
    mydb.commit()

    df9 = pd.DataFrame(table9, columns= ("QUATER", "TRANSACTION_AMOUNT"))
    st.write(df9)

    qu9_bar1=  px.bar(df9, y="QUATER" ,x="TRANSACTION_AMOUNT", title=f"TOTAL TRANSACTION AMOUNT BASED ON QUATER",  
                            color_discrete_sequence=px.colors.sequential.Teal_r , height= 750, width= 1100)
    st.plotly_chart(qu9_bar1)


#'10.Top 10 User_Count using Year-wise in Top_User?'

def insights_topuser_count_year():
    query10= '''select Year, sum(User_count) as User_count from top_user 
                group by Year 
                order by User_count desc;'''

    mycursor.execute(query10)
    table10 = mycursor.fetchall()
    mydb.commit()

    df10 = pd.DataFrame(table10, columns= ("YEAR", "USER_COUNT"))
    st.write(df10)
    qu10_bar1=  px.bar(df10, y="YEAR" ,x="USER_COUNT", title=f"TOTAL USER COUNT BASED ON YEAR",  orientation= "h",
                            color_discrete_sequence=px.colors.sequential.Viridis_r , height= 750, width= 1100)
    st.plotly_chart(qu10_bar1)


############################## FOR VIDEO CLIP ######################################

video_path = "D:\Guvi\Capstone\pulse-video.mp4"
clip = VideoFileClip(video_path)



##################################### Streamlit ###################################
mydb = mysql.connector.connect(host ='localhost',user='root',password='7ApriL@2002',database='phonepe')
mycursor=mydb.cursor()

st.set_page_config(layout='wide')
st.backgroundColor = '6739B7'

st.header(':violet[Phonepe Pulse Data Visualization ]',anchor=False)
st.write('**(Note)**:-This data between **2018** to **2023** in **INDIA**')
st.balloons()


with st.sidebar:
    st.title(":green[CAPSTONE PROJECT-2]")
    st.header("Introduction about Myself")
    st.caption("Name : Mohamed Hannan. S")
    st.caption("Course : Master in DataScience")
    st.caption("Batch : MDE88")

options = option_menu(
                menu_title = "Explore",
                options=["Home", "Data Exploration","Insights"],
                icons=["house-fill","clipboard-data-fill","file-earmark-bar-graph-fill" ],
                default_index = 0,
                menu_icon="cast",
                orientation="horizontal",
                key="navigation_menu",
                styles={
                        "font_color": "#DC143C",   
                        "border": "2px solid #DC143C", 
                        "padding": "10px 25px"   
                    }
            )




if options == "Home":

    st.image(Image.open(r"D:\Guvi\Capstone\v-emhrqu_400x400.png"),width= 100)
    st.subheader("PHONEPE: Indian digital payments and financial services company")

    st.divider()

    st.write("**Welcome to the PhonePe Pulse Data. This application provides insights and analysis of PhonePe data "
            "across various categories such as transactions and users.**")
    st.markdown("")
 
    st.markdown("")


    st.video("D:\Guvi\Capstone\pulse-video.mp4")

    st.divider()

    st.write("Explore the **DATA EXPLORATION** page to analyze aggregated and map data. "
            "Get insights and answers to specific questions on the **INSIGHTS** page.")
    st.markdown("")
    st.markdown("")
    st.info("**Navigate through the tabs to explore different analyses and insights.**")


    st.divider()
    st.markdown("Developed by **MOHAMED HANNAN**")

elif options == "Data Exploration":
    tab1,tab2,tab3 = st.tabs(["📊:green[AGGREGATED CHART]","📊:green[MAP CHART]","📊:green[TOP CHART]"])

    with tab1:
        type1 = st.radio("Select the Type:",["Transaction Analysis", "User Analysis"])

        if type1 == "Transaction Analysis":
            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("SELECT THE DESIRED YEAR", Aggre_Transaction["Year"].min(), Aggre_Transaction["Year"].max(), Aggre_Transaction["Year"].min())

            tr_amco_y = Transaction_amount_count_year(Aggre_Transaction, years)

            col5,col6 = st.columns(2)
            with col5:
                states = st.selectbox("Select the Desired State", tr_amco_y["State"].unique())

            AgTr_Trans_Type(tr_amco_y, states)

            col3,col4= st.columns(2)
            with col3:
                quaters = st.slider("SELECT THE DESIRED QUARTER", tr_amco_y["Quater"].min(), tr_amco_y["Quater"].max(), tr_amco_y["Quater"].min())

            Aggre_Trans_year_quater = Transaction_amount_count_year_quater(tr_amco_y, quaters)

            col7,col8 = st.columns(2)
            with col7:
                states = st.selectbox("Select the State", Aggre_Trans_year_quater["State"].unique())

            AgTr_Trans_Type(Aggre_Trans_year_quater, states)

        elif type1 == "User Analysis":

            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("SELECT THE DESIRED YEAR", Aggre_User["Year"].min(), Aggre_User["Year"].max(), Aggre_User["Year"].min())

            Agg_us_bc_y= Aggre_User_Br_Cou_Y(Aggre_User, years)

            col3,col4= st.columns(2)
            with col3:
                quaters = st.slider("SELECT THE DESIRED QUARTER", Agg_us_bc_y["Quater"].min(), Agg_us_bc_y["Quater"].max(), Agg_us_bc_y["Quater"].min())

            Agg_us_bc_y_q=  Aggre_User_br_cou_Y_Quar(Agg_us_bc_y, quaters)

            col5,col6 = st.columns(2)
            with col5:
                states = st.selectbox("Select the Desired State", Agg_us_bc_y_q["State"].unique())

            Aggre_User_br_cou_Y_Quar_State(Agg_us_bc_y_q, states)
            

    with tab2:
        type2 = st.radio("Select the Desired Type:",["Transaction Analysis", "User Analysis"]) #map

        if type2 == "Transaction Analysis":
            
            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("SELECT THE DESIRED YEAR ", Map_Transaction["Year"].min(), Map_Transaction["Year"].max(), Map_Transaction["Year"].min())

            map_tr_am_co_y= Transaction_amount_count_year(Map_Transaction, years) 

            col5,col6 = st.columns(2)
            with col5:
                states = st.selectbox("Select the Desired_State", map_tr_am_co_y["State"].unique())

            MapTr_District(map_tr_am_co_y, states)

            col3,col4= st.columns(2)
            with col3:
                quaters = st.slider("SELECT THE DESIRED_QUARTER", map_tr_am_co_y["Quater"].min(), map_tr_am_co_y["Quater"].max(), map_tr_am_co_y["Quater"].min())

            Map_Trans_year_quater = Transaction_amount_count_year_quater(map_tr_am_co_y, quaters)

            col7,col8 = st.columns(2)
            with col7:
                states = st.selectbox("Select the STATE", Map_Trans_year_quater["State"].unique())

            MapTr_District(Map_Trans_year_quater, states)


        elif type2 == "User Analysis":

            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("SELECT THE DESIRED_YEAR", Map_User["Year"].min(), Map_User["Year"].max(), Map_User["Year"].min())

            map_us_year= Map_User_year(Map_User, years)

            col3,col4= st.columns(2)
            with col3:
                quaters = st.slider("Select The DESIRED QUARTER", map_us_year["Quater"].min(), map_us_year["Quater"].max(), map_us_year["Quater"].min())

            map_us_year_quater = Map_User_year_quater(map_us_year, quaters)

            col5,col6 = st.columns(2)
            with col5:
                states = st.selectbox("Select the Desired_State", map_us_year_quater["State"].unique())

            Map_User_year_quater_state(map_us_year_quater, states)


    with tab3:
        type3 = st.radio("SELECT THE TYPE:",["Transaction Analysis", "User Analysis"])

        if type3 == "Transaction Analysis":
            
            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("Select The DESIRED YEAR ", Top_Transaction["Year"].min(), Top_Transaction["Year"].max(), Top_Transaction["Year"].min())

            top_tran_tr_amco_y= Transaction_amount_count_year(Top_Transaction, years)

            col5,col6 = st.columns(2)
            with col5:
                states = st.selectbox("Select the DESIRED_STATE", top_tran_tr_amco_y["State"].unique())

            Top_Trans_year_state(top_tran_tr_amco_y, states)

            col3,col4= st.columns(2)
            with col3:
                quaters = st.slider("Select the DESIRED QUARTER", top_tran_tr_amco_y["Quater"].min(), top_tran_tr_amco_y["Quater"].max(), top_tran_tr_amco_y["Quater"].min())

            Top_Trans_year_quater = Transaction_amount_count_year_quater(top_tran_tr_amco_y, quaters)


        elif type3 == "User Analysis":

            col1,col2 = st.columns(2)
            with col1:
                years = st.slider("Select The DESIRED_YEAR ", Top_User["Year"].min(), Top_User["Year"].max(), Top_User["Year"].min())

            Top_user_Year= Top_User_year(Top_User, years)

            col5,col6 = st.columns(2)
            with col5:
                states = st.selectbox("Select The DESIRED_STATE", Top_user_Year["State"].unique())

            Top_user_year_state(Top_user_Year, states)


elif options == "Insights":
    st.markdown("# ")
    st.subheader(":red[Select one of the options to have Insights on Phonepe Data]", anchor=False)
    all_questions = st.selectbox("Select the Questions",
                           ('1.What is the Total Transaction Amount of Aggregated_Transactions in Top 10 States?',
                           '2.What are the Pincodes having Top 10 User Count in Top_users?',
                           '3.What are the the Pincodes having Top 10 Transaction_Amount and Transaction_Count in Top_Transaction?',
                           '4.What are the the Districts having Top 10 User_Count and App_Opens by Users in Map_User?',
                           '5.What are the the Districts having Top 10 Transaction_amount in Map_Transaction?',
                           '6.What are the States of Total Top 10 User_count in Aggregated_User?',
                           '7.What are the States having Top 10 Transaction_count in Map_Transaction?',
                           '8.What are the Mobile Brands having Top 10 User_Count in Aggregated_User?',
                           '9.Which Quarter has the highest number of Transaction_amount in Aggregated_Transaction?',
                           '10.Top 10 User_Count using Year-wise in Top_User?'))
    st.divider()

    if all_questions == '1.What is the Total Transaction Amount of Aggregated_Transactions in Top 10 States?':
         
        insights_top_aggre_map_tran_amo("aggregated_transaction")


    elif all_questions == '2.What are the Pincodes having Top 10 User Count in Top_users?':

        insights_topusers_user_count()

    elif all_questions == '3.What are the the Pincodes having Top 10 Transaction_Amount and Transaction_Count in Top_Transaction?':

        insights_toptrans_amount_count()

    elif all_questions == '4.What are the the Districts having Top 10 User_Count and App_Opens by Users in Map_User?':

        insights_mapuser_user_opens()

    elif all_questions == '5.What are the the Districts having Top 10 Transaction_amount in Map_Transaction?':

        insights_maptrans_amount_districtwise()

    elif all_questions == '6.What are the States of Total Top 10 User_count in Aggregated_User?':

        insights_aggreuser_usercount()

    elif all_questions == '7.What are the States having Top 10 Transaction_count in Map_Transaction?':

        insights_maptrans_count()

    elif all_questions == '8.What are the Mobile Brands having Top 10 User_Count in Aggregated_User?':

        insights_agguser_brandcount()

    elif all_questions == '9.Which Quarter has the highest number of Transaction_amount in Aggregated_Transaction?':

        insights_aggretrans_amount_quater()
    
    elif all_questions == '10.Top 10 User_Count using Year-wise in Top_User?':

        insights_topuser_count_year()



