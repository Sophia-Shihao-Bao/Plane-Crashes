#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import streamlit as st
from streamlit_option_menu import option_menu
pio.renderers.default='browser'
pd.set_option('display.max_columns', None)



# In[2]:


country_dict = {"British Columbia Canada":"Canada",
                "Canada2":"Canada",
               "Off Northern Germany":"Germany",
               "Over the North Sea":"North Sea",
               "Over the Mediterranean":"Mediterranean Sea",
               "Over the Mediterranean Sea":"Mediterranean Sea",
               "Off Gibraltar":"Gibraltar",
               "Over the English Channel":"English Channel",
               "USSR":"Russia",
               "Over the Gulf of Finland":"Finland",
               "Off Morocco":"Morocco",
               "Buenos Aires":"Brazil",
               "Off Spain":"Spain",
               "Off Algiers":"Algiers",
               "Gulf of Finland":"Finland",
               "South AtlantiOcean":"Atlantic Ocean",
               "AtlantiOcean":"Atlantic Ocean",
               "AtlantiOcean between N.Y. and Bermuda":"Atlantic Ocean",
               "Jersey":"England",
               "Near Moscow":"Russia",
               "Netherlands Indies":"Netherlands",
               "London":"England",
               "Tanganyika":"Tanzania",
               "Near Bogota Colombia":"Colombia",
               "PacifiOcean between Manila and Guam":"Pacific Ocean",
               "Mocambique":"Mozambique",
               "The Netherlands":"Netherlands",
               "South of Gibraltar":"Gibraltar",
               "Off Malta-Luqa":"Malta",
               "Gulf of Oman":"Oman",
               "Scotland":"England",
               "Gulf of Tonkin":"Vietnam",
               "Newfoundland":"Canada",
               "off Australia":"Australia",
               "French Equatorial Africa":"France",
               "Off Malaya":"Malaya",
               "Off the Panama coast":"Panama",
               "Near Hong Kong International Airport":"China",
               "North PacifiOcean":"Pacific Ocean",
               "Hong Kong":"China",
               "French Cameroons":"Cameroon",
               "Labrador":"Canada",
               "NE of Bermuda":"Bermuda",
               "Belgian Congo (Zaire)":"Congo",
               "French Indo-China":"China",
               "PacifiOcean between Hong Kong and Macao":"China",
               "Taiwan":"China",
               "off the Philippine island of Elalat":"Philippine",
               "Manitoba":"Canada",
               "Azores":"Portugal",
               "325 miles east of Wake Island":"Wake island",
               "North Atlantic":"Atlantic Ocean",
               "Cameroons":"Cameroon",
               "French Equitorial Africa":"France",
               "Over the PacifiOcean":"Pacific Ocean",
               "Okinawa":"Japan",
               "Baangladesh":"Bangladesh",
               "Off Guam":"Guam",
               "Gulf of Mexico":"Mexico",
               "Gulf of Sirte":"Libya",
               "Qld. Australia":"Australia",
               "East Germany":"Germany",
               "Off Puerto Rico":"Puerto Rico",
               "Near Tipuani (Bolivia":"Bolivia",
               "Philippine Sea":"Philippines",
               "South Vietnam":"Vietnam",
               "Sao Tomé & Principe":"Sao Tomé",
               "Mt. Helmos. Greece":"Greece",
               "French Somaliland":"France",
               "Off Northen Panama":"Panama",
               "Indian":"India",
               "Northern India":"India",
               "South Africa (Namibia)":"South Africa",
               "Off Chili":"Chili",
               "Near Recife Brazil":"Brazil",
               "Off  Taiwan":"China",
               "Near Villia Greece":"Greece",
               "Western Samoa":"Samoa",
               "Netherlands Antilles":"Netherlands",
               "Tahiti":"France",
               "Sainte Lucia Island":"Saint Lucia",
               "Crete":"Greece",
               "Hunary":"Hungary",
               "Southeastern Bolivia":"Bolivia",
               "Havana. Cuba":"Cuba",
               "Equatorial Guinea":"Guinea",
               "Off Hong Kong":"China",
               "West Samoa":"Samoa",
               "Rhodesia (Zimbabwe)":"Zimbabwe",
               "Rhodesia":"Zimbabwe",
               "British Columbia Canada":"Canada",
               "Over the AtlantiOcean":"Atlantic Ocean",
               "Off Tabones Island  Philippines":"Philippines",
               "Russian":"Russia",
               "Saint Lucia Island":"Saint Lucia",
               "Gulf of Thailand":"Thailand",
               "Off Taiwan":"China",
               "Barquisimeto Venezuela":"Venezuela",
               "Off  Bimini":"Bahamas",
               "110 miles West of Ireland":"Ireland",
               "Soviet Union":"Russia",
               "Islay Island":"England",
               "Leeward Islands":"Puerto Rico",
               "Thiland":"Thailand",
               "Over the Andaman Sea":"Andaman Sea",
               "Eugene Island":"Mexico",
               "Central Mozambique":"Mozambique",
               "Northern Afghanistan":"Afghanistan",
               "Zaïre":"Congo",
               "Milford Sound":"New Zeland",
               "Sierre Leone":"Sierra Leone",
               "Santiago de Cuba":"Cuba",
               "French Polynesia":"France",
               "Great Inagua":"Bahamas",
               "DemocratiRepubliCongo":"Congo",
               "Near Nag":"India",
               "Northern Iraq":"Iraq",
               "United Kingdom":"England",
               "Queensland  Australia":"Australia",
               "Canada2":"Canada",
               "Northern Israel":"Israel",
               "off Angola":"Angola",
               "Azores (Portugal)":"Portugal",
               "Republiof Georgia":"Republic of Georgia",
               "French West Indies":"France",
               "Republiof Djibouti":"Djibouti",
               "Bosnia-Herzegovina":"Bosnia Herzegovina",
               "British Virgin Islands":"England",
               "DemoctratiRepubliCongo":"Congo",
               "DemocratiRepubliCogo":"Congo",
               "Near Karkov":"Russia",
               "Saskatchewan":"Canada",
               "Off São Tomé Island":"São Tomé",
               "DR Congo":"Congo",
               "DemocratiRepubliof Congo":"Congo",
               "BO":"Bolivia",
               "Guernsey":"England",
               "Over the North PacifiOcean":"Pacific Ocean",
               "Morrocco":"Morocco",
               "Aregntina":"Argentina",
               "Jamacia":"Jamaica",
               "Romainia":"Romania",
               "Off Northern Panama":"Panama",
               "Off Turks and Caicos Islands":"Turks and Caicos Islands",
               "Sarawak":"Malaysia",
               "Phillipines":"Philippines",
               "Reunion":"France",
               "UAR":"Egypt",
               "Off Irish coast":"Ireland",
               "Malagasy Republic":"Madagascar",
               "Guadeloupe":"France",
               "Caribbean":"Caribbean Sea",
               "Ile of Man":"England",
               "Philippine":"Philippines",
               "Philipines":"Philippines",
               "Mauretania":"Mauritania",
               "off Bermuda":"Bermuda",
               "Belgium Congo":"Congo",
               "Yukon Territory":"Canada",
               "Off the coast of France":"France",
               "Burma":"Myanmar",
               "PacifiOcean":"Pacific Ocean",
               "North AtlantiOcean":"Atlantic Ocean",
               "Boliva":"Bolivia",
               "Belgian Congo":"Congo",
               "Zaire":"Congo",
               "West Germany":"Germany",
               "Sao Tomé":"São Tomé and Príncipe",
               "UK":"England",
               "Bulgeria":"Bulgaria",
               "Off western Denmark":"Denmark",
               "Trinidad":"Trinidad and Tobago",
               "Off South Africa":"South Africa",
               "Amsterdam":"Netherlands",
               "Vienna":"Austria",
               "Deuch Guyana":"Surinam",
               "Bosnia":"Bosnia and Herzegovina",
               "Tasmania":"Australia",
               "Malaya":"Malaysia",
               "Philippine":"Philippines",
               "Wales":"England",
               "AtlantiOcean off Florida":"US",
               "Off Bahrain":"Bahrain",
               "Over the North Atlantic":"Atlantic Ocean",
               "BaltiSea":"Baltic Sea",
               "Aviateca":"Guatemala",
               "West Pakistan":"Pakistan",
               "Bugaria":"Bulgaria",
               "Northern Ireland":"England",
               "Afghanstan":"Afghanistan",
               "Timor": "Timor-Leste",
               "French West Africa":"Guinea",
               "Yugoslavia":"Serbia"}
state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona","California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
state_typos = ["Deleware","Minnisota","NY","WY","United States","Ilinois","U.S. Samoa","Cailifornia","Washington D.C.","Off the Florida coast","Washingon","Massachusett","Washington DC","New York (Idlewild)","Louisana","Tennesee","Deleware","Near Chicago Illinois","Massachutes","US Virgin Islands","Alakska","Off the Alaska coast","U.S. Virgin Islands","Wisconson","Off Wake Island","AK","IN","Alaksa","CA","Airzona","En route from Argentina  to  California","GA","Calilfornia",
              "Virginia.",
              "Oregon",
              "Near Houma Louisiana",
              "Midway Island Naval Air Station",
              "Oregon",
              "Maryland",
              "Oklohoma",
              "South Dekota",
              "Off the Oregon coast",
              "Off the coast of Maryland",
              "Wake Island",
              "Coloado", "Arazona","D.C."]
listofwrong=["Deleware","Near Chicago Illinois","Massachutes","Near Tipuani (Bolivia","DemocratiRepubliof Congo","Romainia","Louisana", "Sao Tomé & Principe","Philippine Sea","Off Puerto Rico","Guernsey","Morrocco","Midway Island Naval Air Station","New York (Idlewild)","Qld. Australia","Off Guam","Baangladesh","Over the North PacifiOcean","French Equitorial Africa","Cameroons","Off the Oregon coast","Off the coast of Maryland","South Dekota","Off Irish coast","Oklohoma","Mt. Helmos. Greece","Near Novgorod (Russia","Hunary","Formosa Strait","Upper Volta","Khmer Republic","Tahiti","Off the Alaska coast","Near Ardinello di Amaseno","South Yemen","Alakska","325 miles east of Wake Island","US Virgin Islands","Near Villia Greece","Off  Taiwan","Wake Island","Off Chili","South Africa (Namibia)","Reunion","Northern India","Indian","Off Northern Panama","French Somaliland","Western Samoa","Southeastern Bolivia","Sea of Japan","Off South Africa"]
season_dict={"January":"Winter", "February":"Winter",
             "March":"Spring","April":"Spring",
             "May":"Spring","July":"Summer",
             "June":"Summer","August":"Summer",
             "September":"Autumn", "October":"Autumn",
             "November":"Autumn","December":"Winter"}

category_orders_dict = {"day_name":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "month_name":["January","February","March","April","June","July","August","September","October","November","December"], "season_name":["Spring","Summer","Autumn","Winter"]}
path="/Users/sophiabao/文件/onlineclasses/DataQuest/CaseStudy1/"
# In[47]:


plane_raw = pd.read_csv(path+"Airplane_Crashes_and_Fatalities_Since_1908.csv")
plane = plane_raw.copy()
country = plane["Location"].str.split(",").str[-1].str.strip()
plane["country"]=np.where(country.isin(state_names),"US", country)
state_dict = {state:"US" for state in state_typos}
country_dict.update(state_dict)
plane["country1"]=plane["country"].replace(country_dict)
Datetime = pd.to_datetime(plane["Date"])
plane["Datetime"]=Datetime
plane["month"]=plane["Datetime"].dt.month
plane["year"]=plane["Datetime"].dt.year
years = plane["year"]
decades = []
for each in years:
    decade = int(np.floor(each / 10) * 10)
    decades.append(str(decade)+"s")
plane["decades"]=decades
death_ratio = plane["Fatalities"]/plane["Aboard"]
plane["death ratio"]=death_ratio*100
day_name = plane["Datetime"].dt.day_name()
month_name = plane["Datetime"].dt.month_name()
plane["month_name"]=month_name
plane["day_name"]=day_name
plane["season"]=plane["month_name"].replace(season_dict)
plane["DeathRatioCat"]=pd.cut(plane["death ratio"], bins=5, labels=["low","medlow","medium","midhigh","high"])
plane["FatalitiesCat"]=pd.cut(plane["Fatalities"], bins=5, labels=["low","medlow","medium","midhigh","high"])

plane["Survivors"]=np.where(plane["death ratio"]==100, False, True)



country_continents = pd.read_html(path+"Country.html", match="Countries or Areas")
df = pd.concat(country_continents, ignore_index=True)
df = df[['Country or Area', 'Continent']]
df = df.set_index('Country or Area')
country_continents_dict = df.to_dict(orient='dict').get("Continent")
country_continents_dict.update({"England":"Europe", "US":"North America", "Russia":"Europe", "North Sea":"Europe", "English Channel":"Europe", "Mediterranean Sea":"Europe", "Atlantic Ocean":"Ocean", "Pacific Ocean":"Ocean", "Czechoslovakia":"Europe", "Venezuela":"South America", "Bolivia":"South America", "Iran":"Asia", "Syria":"Asia", "Algiers": "Africa","New Guinea":"Oceania", "South Korea":"Asia", "Ivory Coast":"Africa","Tanzania":"Africa","Indian Ocean":"Ocean", "Sea of Japan":"Asia", "Persian Gulf":"Asia", "Vietnam":"Asia", "Laos":"Asia", "Himalayas":"Asia","North Korea":"Asia"})
plane["Continent"] = plane["country1"].map(country_continents_dict)
problems = plane.loc[plane["Continent"].isnull(),["country1"]]

# In[4]:


summarydf=plane[~plane["Summary"].isnull()].copy()
summarydf["hijacked"] = summarydf["Summary"].str.contains("hija[ck]", case=False).astype(bool)
summarydf["ocean"] = summarydf["Summary"].str.contains("ocean|sea", case=False)
summarydf["freshwater"] = summarydf["Summary"].str.contains("lake|river", case=False)
summarydf["storm"] = summarydf["Summary"].str.contains("bad weather|storm|lightning|thumderstorm", case=False)
summarydf["explosion"] = summarydf["Summary"].str.contains("explo[ts]ion|exploded|explode", case=False)
summarydf["gas"] = summarydf["Summary"].str.contains("Hydrogen|Nitrogen|Oxygen", case=False)
summarydf["shot"] = summarydf["Summary"].str.contains("shot", case=False)
summarydf["unknown"] = summarydf["Summary"].str.contains("unknown", case=False)
summarydf["fire"]=summarydf["Summary"].str.contains("fire|flames", case=False)
summarydf["british"] = summarydf["Summary"].str.contains("british", case=False)
summarydf["french"] = summarydf["Summary"].str.contains("french", case=False)
summarydf["system"] = summarydf["Summary"].str.contains("system|softwere|softweare", case=False)
summarydf["mechanical"] = summarydf["Summary"].str.contains("machine|hardweare|hardwere", case=False)
summarydf["error"] = summarydf["Summary"].str.contains("error|pilot|control|operate", case=False) #intresting thing to check with Jason.
summarydf["groundworkers"] = summarydf["Summary"].str.contains("ground|earth", case=False)
summarydf["comunication"] = summarydf["Summary"].str.contains("comunication|brodcast|FM", case=False)
summarydf["landing"] = summarydf["Summary"].str.contains("landing|landed", case=False)

summarydf["liftoff"] = summarydf["Summary"].str.contains("lift off|liftoff", case=False)
summarydf["freshwater1"] = summarydf["freshwater"].replace({True:"Freshwater ", False:" "})
summarydf["ocean1"] = summarydf["ocean"].replace({True:"Ocean ", False:" "})
summarydf["storm1"] = summarydf["storm"].replace({True:"Storm ", False:" "})
summarydf["explosion1"] = summarydf["explosion"].replace({True:"Explosion ", False:" "})
summarydf["shot1"] = summarydf["shot"].replace({True:"Shot ", False:" "})
summarydf["unknown1"] = summarydf["unknown"].replace({True:"Unknown ", False:" "})
summarydf["fire1"] = summarydf["fire"].replace({True:"Fire ", False:" "})
summarydf["british1"] = summarydf["british"].replace({True:"British ", False:" "})
summarydf["french1"] = summarydf["french"].replace({True:"French ", False:" "})
summarydf["liftoff1"] = summarydf["liftoff"].replace({True:"Liftoff ", False:" "})
summarydf["hijacked1"] = summarydf["hijacked"].replace({True:"Hijacked ", False:" "})
summarydf["system1"] = summarydf["system"].replace({True:"System_Error ", False:" "})
summarydf["mechanical1"] = summarydf["mechanical"].replace({True:"Mechanical_Error ", False:" "})
summarydf["error1"] = summarydf["error"].replace({True:"Pilot_Error ", False:" "})
summarydf["groundworkers1"] = summarydf["groundworkers"].replace({True:"Ground_Worker_Error ", False:" "})
summarydf["comunication1"] = summarydf["comunication"].replace({True:"Communication ", False:" "})
summarydf["landing1"] = summarydf["landing"].replace({True:"Landing_Error ", False:" "})

together = summarydf.filter(regex="1$").drop("country1",axis=1).sum(axis=1).str.strip().str.split(" ")
summarydf["CombinedWords"] = together.apply(lambda x: ",".join([i for i in x if i != ""])).replace({"":np.nan}).str.replace("_", " ")
summarydf["WordCat"]=np.where(summarydf["CombinedWords"].isnull(), "NaN",
                              np.where(summarydf["CombinedWords"].str.contains(","),
                            "Multiple", summarydf["CombinedWords"]))


# In[5]:


adding = ["#ddccff"]
custom_padlette_notdone=px.colors.qualitative.Set3
custom_padlette=custom_padlette_notdone.append(adding)

# print firendly names:
pretty_cat_names = {"Location":"Location", "country1":"Country", "day_name":"Day of the Week", "month_name":"Month Name", "decades":"Decades", "season":"Season", "DeathRatioCat":"Death Ratio Category", "FatalitiesCat":"Number of Deaths (Category)", "Survivors":"Any Survivors", "freshwater1":"Freshwater", "ocean1":"Ocean","storm1":"Storm","explosion1":"Explosion", "shot1":"Shot", "unknown1":"Unknown", "fire1":"Fire", "british1":"British", "french1":"French", "liftoff1":"Liftoff", "hijacked1":"Hijacked", "system1":"System Error", "mechanical1":"Mechanical Error", "error1":"Pilot Error", "groundworkers1":"Ground Worker Error", "comunication1":"Comunication Error", "landing1":"Landing Error", "Wordcat":"Word Category", "Continent":"Continent"}
pretty_num_names = {"Fatalities":"Number of Passenger Deaths", "Aboard":"Number of Passengers", "Ground":"Number of Deaths on the Ground", "death ratio":"Percent of Passengers Deaths", "month":"Month Number", "year":"Year","Datetime":"Date"}

all_pretty_names = pretty_cat_names.copy()
all_pretty_names.update(pretty_num_names)
# # Graphs
# ## Fatalities Graphs

# Summary:
# Death ratio are between 1 and 0
# December and August are high death months
# The number of deaths during the week are aprox the same
# Explosion, hijacked and unknown reasons caused the most deaths
# USA has the most death counts in total
# More recent decades caused more deaths

st.set_page_config(layout="wide")
with st.sidebar: 
	selected = option_menu(
		menu_title = 'Navigation Pane',
		options = ['Abstract', 'Background Information', 'Data Cleaning', 
		'Exploratory Analysis','Data Analysis', 'Conclusion', 'Bibliography'],
		menu_icon = 'alarm',
		icons = ["activity","watch","windows","wifi","tools", "pen", "pc"],
		default_index = 0,
		)

if selected == 'Abstract':
	st.title('Abstract')

	st.markdown('This case study uses a dataset provided by THE DEVASTATOR on Kaggle and analyzes the factors that influence plane crashes. After making assumptions and conducting simulations to prove them, conclusions were made that the amount of deaths in plane crashes are caused by multipule factors. Select from the sidebar to see the full case study.')
	st.markdown('')
	st.markdown('')
	st.markdown('')
	st.markdown('')
	st.caption('Made by Shihao Bao')
    
if selected=="Background Information":
    st.title("Background Information")
    st.markdown("Nowadays, the rate of plane crashes is very low. However, plane crashes are disasters and causes depressing consequences to the people on the plane and on the grounds once they happen. “I want to express sympathy to the families who lost loved ones to this terrible tragedy.” said Graham Dallas, at a media briefing after the Boeing B-17G and Bell p-63F planes collided. after finding out on a magazine that plane crashes are caused from different, interesting reasons I decided to investigate further about how to prevent these kinds of disasters. ")
    st.markdown("I found a dataset on Kaggle about plane crashes. It is very interesting and included many it had data from the beginning of the 1900s. Please see the dataset below:")
    st.dataframe(plane_raw)
    
if selected=="Data Cleaning":
    st.title("Data Cleaning")
    st.markdown("I edited the dataset and added new columns into it to make it more easier to understand at get more data from the dataset. Here are my steps.")
    st.subheader("Raw Dataset")
    st.dataframe(plane)
    st.markdown("As we can see, the dataset is hard to understand, let me explain the columns for you.")
    st.markdown("Date: Date of accident, in the format - January 01, 2001")
    st.markdown("Time: Local time, in 24 hr. format unless otherwise specified")
    st.markdown("Location: Location of the crash")
    st.markdown("Operator: Airline or operator of the craft")
    st.markdown("Flight: Flight number assigned bythe aircraft operator")
    st.markdown("Route: Complete or partial route flown prior to the accident")
    st.markdown("Type: aircraft type")
    st.markdown("Registration: ICAO registration of the aircraft")
    st.markdown("CN/IN: Construction or serial number / Line or fuselage number")
    st.markdown("Aboard: total number of people on the aircraft")
    st.markdown("Fatalities: total number of deaths")
    st.markdown("Ground: total number of people killed on the ground because of the crash")
    st.markdown("Summary: Brief description of the accident and cause if known")
    st.markdown("")
    st.markdown("")
    st.dataframe(plane)
    st.markdown("Here is the dataset that I modified a little bit to make more columns that shows more infromation. I added the country, country1, Datetime, month, year, decades, death ratio, month_name, day_name, season, DeathRatioCat and Survivors columns to the dataset.")
    st.markdown("Here are their definitions:")
    st.markdown("country: the first version of country column, some countries are misspelled and some are not countries")
    st.markdown("country1: the final version of the country column, after editing misspelled and mislocated names.")
    st.markdown("Datetime: the datetime version of the 'Date' column, this makes it easier to plot graphs with")
    st.markdown("month: the month number got from the 'Datetime' column")
    st.markdown("year: year isolated from the 'Datetime' column")
    st.markdown("decades: seperated 'year' values into decades for easier reference")
    st.markdown("death ratio: the value of 'Aboard' divided by the value of 'fatalities'")
    st.markdown("month_name: the 'month' column transformed into a name. ex. 1 = january")
    st.markdown("day_name: used the date in 'Datetime' to get the day of the week of the plane crash.")
    st.markdown("season: the season of the crash, by evaluating the 'month_name' column")
    st.markdown("DeathRatioCat: the deathratio category, calculated using the pd.cut() function. ex. deathratio = 1 DeathRatioCat = 'high'")
    st.markdown("Survivors: True/False column, see if the 'deathratio' is 1. If there is surviviors, then the column is 'true', if there is no survivors, the column is 'false'")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("The following are some of the codes that cleaned the original dataset into the one showed above.")
    st.code("""country = plane['Location''].str.split("','").str[-1].str.strip()
plane['country']=np.where(country.isin(state_names),'US', country)
state_dict = {state:'US' for state in state_typos} country_dict.update(state_dict)
plane['country1']=plane['country'].replace(country_dict)""")
    st.markdown("This piece of code shows how I added and cleaned out the country column onto the 'Plane' dataset so we can make more intresting graphs regarding plane crash location.")
    st.code("""country_continents = pd.read_html(path+"Country.html", match="Countries or Areas")
    df = pd.concat(country_continents, ignore_index=True)
    df = df[['Country or Area', 'Continent']]
    df = df.set_index('Country or Area')
    country_continents_dict = df.to_dict(orient='dict').get("Continent")
    country_continents_dict.update({"England":"Europe", "US":"North America", "Russia":"Europe", "North Sea":"Europe", "English Channel":"Europe", "Mediterranean Sea":"Europe", "Atlantic Ocean":"Ocean", "Pacific Ocean":"Ocean", "Czechoslovakia":"Europe", "Venezuela":"South America", "Bolivia":"South America", "Iran":"Asia", "Syria":"Asia", "Algiers": "Africa","New Guinea":"Oceania", "South Korea":"Asia", "Ivory Coast":"Africa","Tanzania":"Africa","Indian Ocean":"Ocean", "Sea of Japan":"Asia", "Persian Gulf":"Asia", "Vietnam":"Asia", "Laos":"Asia", "Himalayas":"Asia","North Korea":"Asia"})
    plane["Continent"] = plane["country1"].map(country_continents_dict)""")
    st.markdown("The piece of code above shows how I made a column of contry names into continents for more group graphs")
    st.code("""for each in years:
        decade = int(np.floor(each / 10) * 10)
        decades.append(str(decade)+"s")
    plane["decades"]=decades""")
    st.markdown("The code above shows how I separated years into decades for better categorical organization")
    st.subheader("Final dataset")
    st.dataframe(summarydf)
    
    st.code("""summarydf=plane[~plane["Summary"].isnull()].copy()
    summarydf["hijacked"] = summarydf["Summary"].str.contains("hija[ck]", case=False).astype(bool)
    summarydf["hijacked1"] = summarydf["hijacked"].replace({True:"hijacked ", False:" "})""")
    st.markdown("The code above is what lead to the 'reasons of plane crash' columns. We just need to see if there is a keyword in the 'Summary' text. The code above is the detection for one of the columns.")
    






if selected=="Exploratory Analysis":
    st.title("Exploratory Analysis")
    st.markdown("This is where you can experiment with the dataset by making your own plotly charts. You can change the variables that makes the chart using dropdown menus, once changed,the system would automaticly change the chart for you. Specific instructions for diffrent charts are below their subheaders. Have fun trying out scatter plots, histograms, sunbursts, and choropleths! Try and see what intresing patterns you may come up with.")
    
    
    st.subheader("Scatter Plots")
    st.markdown("Scatter plots are grapha in which the values of two variables are plotted along two axes, the pattern of the resulting points revealing any correlation present. You can chose your variables from the respective drodown menu. Have Fun!")
    col1,col2 = st.columns([3,6])
    
    with col1.form("Scatter_plot_form"):
        x1 = st.selectbox(
         'Select the X value of the scatterplot', 
         [pname for name, pname in all_pretty_names.items() if name in ["Aboard", "Fatalities","Ground", "month", "year", "decades", "death ratio", "month_name", "day_name", "season", "DeathRatioCat", "FatalitiesCat","Continent"]])
    	
        y1 = st.selectbox(
         'Select the Y value of the scatterplot',
         [pname for name, pname in pretty_num_names.items() if name != "Datetime"])
        
        color1 = st.selectbox("Select the variable the color would be based on", 
    [pname for name,pname in all_pretty_names.items() if name in ["Type","Aboard","Fatalities","Ground","month_name","day_name","season","DeathRatioCat",
    "FatalitiesCat","Survivors","hijacked","ocean","freshwater","storm","explosion","gas",
    "shot","unknown","fire","british","french","system","mechanical","error"
    "groundworkers","comunication","landing","liftoff","WordCat"]])
        
        logscale1 = st.checkbox("Do you want a log scale?",False, key = 4)
        x1_name = [name for name, pname in all_pretty_names.items() if pname == x1]
        y1_name = [name for name, pname in all_pretty_names.items() if pname == y1]
        color1_name = [name for name, pname in all_pretty_names.items() if pname == color1]
        submitted = st.form_submit_button("Click to display Scatter plot")
        if submitted:
            col2.plotly_chart(px.scatter(summarydf, x=x1_name[0], y=y1_name[0], color=color1_name[0], labels=all_pretty_names, category_orders = category_orders_dict, log_y = logscale1))
    
    
    
    
    st.subheader("Histogram")
    st.markdown("A histogram is a diagram consisting of rectangles whose area is proportional to the frequency of a variable and whose width is equal to the class interval. You can choose your variable in the dropdown menu below. In addition, plotly histograms allows some special additions to be made, those are also in their respective dropdown menus.")
    col3,col4 = st.columns([3,6])
    with col3.form("Histogram_Form"):
        x2 = st.selectbox(
         'Select the X value of the graph',
         [pname for name, pname in all_pretty_names.items() if name in["Aboard", "Fatalities","Ground", "month", "year", "decades", "death ratio", "month_name", "day_name", "season", "DeathRatioCat", "FatalitiesCat","Continent"]])
        color3 = st.selectbox("Select the Color variable", [pname for name, pname in all_pretty_names.items() if name in["year", "decades", "month_name", "day_name", "season", "DeathRatioCat", "FatalitiesCat"]], key=5)
        barmode = st.selectbox("please select the barmode value of the graph, defult is relative", ("relative", "group", "overlay"))
        barnorm = st.selectbox("please select the barnorm value of the graph, defult is none", ("", "percent", "fraction"))
        marginal = st.selectbox("Select the marginal for the graph, defult is none. If set, a subplot is drawn alongside the main plot, visualizing the distribution.", ("", "rug", "box", "violin", "histogram"))
        x2_name = [name for name, pname in all_pretty_names.items() if pname == x2]
        color3_name = [name for name, pname in all_pretty_names.items() if pname == color3]
        submitted = st.form_submit_button("Click to display Histogram")
        if submitted:        
            col4.plotly_chart(px.histogram(summarydf, x=x2_name[0], barmode = barmode,barnorm=barnorm,color=color3_name[0],labels=all_pretty_names,category_orders=category_orders_dict))
    
    
    
    
    st.subheader("Box Plot")
    st.markdown("A box plot is a graphical rendition of statistical data based on the minimum, first quartile, median, third quartile, and maximum. It is usefull to show the distrubution of data.")
    col5,col6 = st.columns([3,6])
    
   
    with col5.form("Box_Plot_Form"):
      x3 = st.selectbox(
        'Select the X value of the graph',
        [pname for name, pname in all_pretty_names.items() if name in["year", "decades", "month_name", "day_name", "season", "DeathRatioCat", "FatalitiesCat","Continent"]], key=1)
      y3 = st.selectbox("Select the Y value of the graph", [pname for name, pname in all_pretty_names.items() if name in["Aboard", "Fatalities","Ground", "death ratio"]], key = 2)
      color2 = st.selectbox("Select the Color variable", [pname for name, pname in all_pretty_names.items() if name in["year", "decades", "month_name", "day_name", "season", "DeathRatioCat", "FatalitiesCat"]], key=3)
      logscale = st.checkbox("Do you want a log scale?",False, key = 4)
      x3_name = [name for name, pname in all_pretty_names.items() if pname == x3]
      y3_name = [name for name, pname in all_pretty_names.items() if pname == y3]
      color2_name = [name for name, pname in all_pretty_names.items() if pname == color2]
       # Every form must have a submit button.
      submitted = st.form_submit_button("Click to display box plot")
      if submitted:
        col6.plotly_chart(px.box(summarydf, x=x3_name[0], y=y3_name[0], color=color2_name[0], labels=all_pretty_names, category_orders=category_orders_dict, log_y = logscale))

    




    st.subheader("Sunbursts")
    st.markdown("The sunburst chart is ideal for displaying hierarchical data. Each level of the hierarchy is represented by one ring or circle with the innermost circle as the top of the hierarchy. You can choose your levels in the dropdown menus below. Please note that if the two variables are the same ot are similar, the graph would not work. The values that the porportions are based on is also one of the dropdown menus. You can click on the first level of any of the variables to see a more detailed graph.")
    col7,col8=st.columns([3,6])
    
    
    with col7.form("sunburst_form"):
        layer1 = st.selectbox("Select the first layer of the sunburst graph", ("month_name","day_name","season","DeathRatioCat",
        "FatalitiesCat","Survivors","hijacked","ocean","freshwater","storm","explosion","gas",
        "shot","unknown","fire","british","french","system","mechanical","error"
        "groundworkers","comunication","landing","liftoff","WordCat","Continent"))
        
        layer2 = st.selectbox("Select the second layer of the sunburst graph", ("day_name", "month_name","season","DeathRatioCat",
        "FatalitiesCat","Survivors","hijacked","ocean","freshwater","storm","explosion","gas",
        "shot","unknown","fire","british","french","system","mechanical","error"
        "groundworkers","comunication","landing","liftoff","WordCat"))
        
        value = st.selectbox("select the value the graph is gong to be based on", [pname for name, pname in all_pretty_names.items() if name in["Aboard","Fatalities","Ground"]])
        
        
        layer1_name = [name for name, pname in all_pretty_names.items() if pname == layer1]
        layer2_name = [name for name, pname in all_pretty_names.items() if pname == layer2]
        value_name = [name for name, pname in all_pretty_names.items() if pname == value]
        submitted = st.form_submit_button("Click to display Sunburst")
        if submitted:
            col8.plotly_chart(px.sunburst(summarydf, path=[layer1, layer2], values=value_name[0], labels=all_pretty_names))


    
    st.subheader("Choropleths")
    st.markdown("Chrorpleths are graphs that show infromation on a map, it requiers location infromation and a value. You can chose a animation value that measures crashes over time, a value that the scales and color data would be based on, the projection of the map, and the scope that the map focuses on.")
    col9,col10=st.columns([3,6])
    
    with col9.form("Choropleth_Form"):
        animation_value = st.selectbox("Please select the variable that the animation would be based on", [pname for name, pname in all_pretty_names.items() if name in["month_name","day_name","season"]])
        color2 = col9.selectbox("please select the variable that the color would be based on", 
                                [pname for name, pname in all_pretty_names.items() if name 
                                 in["Aboard","Fatalities","Ground"]])
        projection = st.selectbox("please select the projection of the map", ('equirectangular', 'mercator', 'orthographic', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4', 'azimuthal equal area', 'azimuthal equidistant', 'conic equal area', 'conic conformal', 'conic equidistant', 'gnomonic', 'stereographic', 'mollweide', 'hammer', 'transverse mercator', 'winkel tripel', 'aitoff', 'sinusoidal'))
        
        
        animation_value_name = [name for name, pname in all_pretty_names.items() if pname == animation_value]
        color2_name = [name for name, pname in all_pretty_names.items() if pname == color2]
        
        scope = st.selectbox("Please select the focus the map is on, defult is world", ('world', 'usa', 'europe', 'asia', 'africa', 'north america','south america'))
        
        submitted = st.form_submit_button("Click to display Choropleth")
        if submitted:
        
            col10.plotly_chart(px.choropleth(summarydf.groupby(["country1",animation_value_name[0]])[color2_name[0]].sum().reset_index().sort_values(animation_value_name[0]), 
                      locations="country1", 
                      locationmode="country names", 
                      color= color2_name[0],
                      color_continuous_scale=px.colors.sequential.Peach,
                      projection= projection,
                      scope= scope,
                      animation_frame= animation_value_name[0], category_orders = category_orders_dict, labels=all_pretty_names))
    
    
    
    

if selected=="Data Analysis":
    st.title("Data Analysis")
    st.markdown("On this page, I would show you some of my conclusions that I drew from the dataset and graphs that I made.")
    st.markdown("")
    
    st.subheader("Gathering Infromation")
    real2 = px.scatter(summarydf, x="decades", y="Aboard", color="DeathRatioCat")
    real2.update_traces(marker_line_width=0.5, marker_line_color= "black")
    real2.update_layout(yaxis=dict(title_text="Aboard", title_font_size=16), 
                          xaxis=dict(title_text="Decades", title_font_size=16, dtick=10),
                         legend_font_family="Times New Roman",
                         legend_title="Month")
    st.plotly_chart(real2)
    st.markdown("This scatter plot shows the disturbution of plane crashed over the years of the dataset with the color as the categroy of the death ratio. As we can see, in later years, more planes has flown but the death ratio has significantly decreased, this proves that plane crashes(even though they happen) are much more safer than before.")
    
    real3 = px.histogram(summarydf, x="decades")
    real3.update_traces(marker_line_width=1, marker_line_color= "black")
    real3.update_layout(yaxis=dict(title_text="Count", title_font_size=16), 
                          xaxis=dict(title_text="Decades", title_font_size=16))
    st.plotly_chart(real3)
    st.markdown("This histogram again reanforses the point made above about more plane crashes(because more plane rides) in more recent decades. However, it is worth noting that the number of plane crashes rises till 1970 and starts going downhill from then. I believe that this is because of the inproved security of planes since 1970.")
    
    real4 = px.choropleth(summarydf.groupby(["country1","season"])["Fatalities"].sum().reset_index().sort_values("season"), 
                  locations="country1", 
                  locationmode="country names", 
                  color="Fatalities",
                  color_continuous_scale=px.colors.sequential.Peach,
                  projection="orthographic",
                 animation_frame="season",
                 category_orders=category_orders_dict)
    st.plotly_chart(real4)
    st.markdown("This choropleth shows the disturbision of plane crashes around the world using country locations. I added a animation bar, as this can show the plane crashes for diffrent seasons. The color variable is based on the number of deaths added together for that season in that country. We can see from the color scale that autumn is a high risk time for plane crashes, and because less planes flew, spring has a lower death count. From all countries, the US has a reletively large addition of death counts in all seasons, this is to expected as the US has a developed economy and more planes flew to, and from it.")
    
    st.subheader("Causes of plane crashes")
    real1 = px.sunburst(summarydf[summarydf["WordCat"]!="NaN"], path=["WordCat"], labels=pretty_cat_names)
    st.plotly_chart(real1)
    st.markdown("For this chart, I made a sunburst graph that shows the proportion of plane crashes that happened because of a diffrent reason. I removed the NaNs from the graph to make the data be more clear, as NaNs were a good proportion of the data. From this chart, we can see that 'multipule' resons caused plan crashes followed by 'Pilot Error'.")
    
    real5 = px.histogram(summarydf, x="DeathRatioCat")
    real5.update_traces(marker_line_width=1, marker_line_color= "black")
    real5.update_layout(yaxis=dict(title_text="Count", title_font_size=16), 
                          xaxis=dict(title_text="Death Ratio Category", title_font_size=16))
    st.plotly_chart(real5)
    st.markdown("As we can see from the histogram above, the death rato (number of passengers divided by death number) category has values from low to high. The 'high' category has the most amount of values. This shows that although plane crashes happen rarely in recent years, it is still a really dizastrous event if it happens.")

if selected=="Conclusion":
    st.title("Conclusion")
    st.markdown("Data shows that plane crashes are mostly caused by multipule factors, and followed by pilot error. While plane crashes are relatively rare, they can have significant consequences for passengers, crew, and the surrounding community. Continued efforts to improve safety and prevent crashes are essential.")

if selected=="Bibliography":
    st.title("Bibliography")
    st.markdown("""Works Cited “Airplane Crashes and Fatalities.” Www.kaggle.com, www.kaggle.com/datasets/thedevastator/airplane-crashes-and-fatalities.""")
# In[6]:


fig2 = px.choropleth(summarydf.groupby(["country1","month"])["Fatalities"].sum().reset_index().sort_values("month"), 
              locations="country1", 
              locationmode="country names", 
              color="Fatalities",
              color_continuous_scale=px.colors.sequential.Peach,
              projection="orthographic",
             animation_frame="month",
             category_orders={"month_name":["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]})
fig3 = px.choropleth(summarydf.groupby(["country1","day_name"])["Fatalities"].sum().reset_index().sort_values("day_name"), 
              locations="country1", 
              locationmode="country names", 
              color="Fatalities",
              color_continuous_scale=px.colors.sequential.Peach,
              projection="orthographic",
             animation_frame="day_name",
             category_orders={"day_name":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]})
fig30 = px.sunburst(summarydf, path=['WordCat','Survivors'])

# Graph1: Death ratio

# In[7]:



# Graph2: Death Ratio with month color scheme

# In[8]:


fig20 = px.scatter(plane, x="Fatalities", y="Ground", color="month", hover_name="index")


# Graph3: Ratio Death to ground death

# In[9]:


date_deaths = px.scatter(summarydf, x="Datetime", y="Fatalities", color="french",
                         color_discrete_map={False:"#33cc33",True:"#ff0000"},
                        hover_name="country",
                        hover_data=["Aboard"])


# Graph4: Death according to date

# In[10]:


date_death = px.scatter(summarydf, x="Datetime", y="Fatalities", color="french",
                         color_discrete_sequence=px.colors.qualitative.G10[5:7])

# Graph 5: Death according to datetime with diffrent color scheme



# In[13]:

fig4 = px.choropleth(summarydf.groupby(["country1","month_name"])["Fatalities"].sum().reset_index().sort_values("month_name"), 
              locations="country1", 
              locationmode="country names", 
              color="Fatalities",
              color_continuous_scale=px.colors.sequential.Peach,
              projection="orthographic",
             animation_frame="month_name",
             category_orders={"month_name":["January","February","March","April","June","July","August","September","October","November","December"]})


# In[14]:


boxplot = px.histogram(summarydf[summarydf["WordCat"]!="NaN"],x="WordCat",y="death ratio",
                       hover_data=["Summary"],
                       color="DeathRatioCat",
                       color_discrete_sequence=px.colors.qualitative.Set3, barnorm="percent",
                       barmode="group",
                       histfunc="avg",
                      facet_col='decades', facet_col_wrap=4)
boxplot = boxplot.update_traces(marker_line_width=1, marker_line_color= "black")
boxplot.update_traces(hoverlabel_bordercolor="black")
boxplot.update_layout(yaxis=dict(title_text="Percent", title_font_size=16, title_font_color="Blue"), 
                      xaxis=dict(title_text="Death Ratio", title_font_size=16, title_font_color="Red"))


# In[15]:


fig5 = px.choropleth(plane.groupby("country1")["Fatalities"].sum().reset_index(), 
              locations="country1", 
              locationmode="country names", 
              color="Fatalities",
              color_continuous_scale=px.colors.sequential.ice,
              projection="sinusoidal")


fig31 = px.histogram(summarydf, x="Continent")
fig32 = px.scatter(summarydf, x="decades", y="Continent")

# In[16]:


fig6 = px.choropleth(plane.groupby("country1")["Fatalities"].sum().reset_index(), 
              locations="country1", 
              locationmode="country names", 
              color="Fatalities",
              color_continuous_scale=px.colors.sequential.Peach,
              projection="orthographic")


# In[17]:


fig7 = px.choropleth(plane.groupby(["country1","decades"])["Fatalities"].sum().reset_index().sort_values("decades"), 
              locations="country1", 
              locationmode="country names", 
              color="Fatalities",
              color_continuous_scale=px.colors.sequential.Peach,
              projection="orthographic",
             animation_frame="decades")


# In[18]:


fig8 = px.histogram(summarydf, x="Fatalities",barmode="group",barnorm="fraction")


# In[19]:


fig9 = px.histogram(plane, x="Fatalities",barmode="group",histfunc="max",nbins=100)
fig9.update_traces(marker_line_width=1)


# In[20]:


date_deaths = px.scatter(summarydf, x="year", y="Fatalities", color="death ratio",
                         color_continuous_scale=px.colors.sequential.Agsunset,
                        hover_name="country",
                        hover_data=["Aboard"],
                        opacity=0.5)


# In[56]:


fig10 = px.scatter(plane, x="year", y="Aboard", color="Survivors")


# # Word Category

# Summary
# 

# In[52]:


boxplot = px.bar(summarydf[summarydf["WordCat"]!="NaN"].groupby(["WordCat","DeathRatioCat"])["Fatalities"].sum().reset_index(),
                       x="WordCat",y="Fatalities",
                       color="DeathRatioCat",
                       color_discrete_sequence=px.colors.qualitative.Set3,
                       barmode="group",
                        text="Fatalities")
boxplot = boxplot.update_traces(marker_line_width=1, marker_line_color= "black")
boxplot.update_traces(hoverlabel_bordercolor="black")
boxplot.update_layout(yaxis=dict(title_text="Percent", title_font_size=16, title_font_color="Blue"), 
                      xaxis=dict(title_text="Death Ratio", title_font_size=16, title_font_color="Red"))


# In[22]:


boxplot1 = px.histogram(summarydf,x="fire", y="death ratio",marginal="rug", hover_data=["Summary"], color="fire",
                      color_discrete_sequence=px.colors.qualitative.Set3, histfunc="avg")








boxplot2 = boxplot.update_traces(marker_line_width=1, marker_line_color= "#e6ffe6")
boxplot2.update_traces(hoverlabel_bordercolor="black")
boxplot2.update_layout(yaxis=dict(title_text="Death Ratio", title_font_size=16, title_font_color="Blue"), 
                      xaxis=dict(title_text="Fire", title_font_size=16, title_font_color="Green"))


# In[23]:


decade_word1 = px.histogram(summarydf[summarydf["WordCat"]!=("NaN")], x="decades", color="WordCat", 
                           color_discrete_sequence=px.colors.qualitative.Set3,
                          barmode="group",
                          barnorm="percent")
decade_word1.update_traces(marker_line_width=1, marker_line_color= "gold")
decade_word1.update_layout(yaxis=dict(title_text="Percent", title_font_size=16), 
                          xaxis=dict(title_text="Decades", title_font_size=16, dtick=10))


# In[49]:


boxplot3 = px.histogram(summarydf[summarydf["WordCat"]!="NaN"],x="death ratio",marginal="rug", hover_data=["Summary"], color="WordCat", barnorm="percent", barmode="group", nbins=10)
boxplot = boxplot.update_traces(marker_line_width=1, marker_line_color= "black")
boxplot.update_traces(hoverlabel_bordercolor="black")

boxplot3.update_layout(yaxis=dict(title_text="Percent", title_font_size=16, title_font_color="Blue"), 
                      xaxis=dict(title_text="Death Ratio", title_font_size=16, title_font_color="Red"))


# In[25]:


monthhist = px.histogram(summarydf[summarydf["WordCat"]!=("NaN")], x="month_name", color="WordCat",
                         color_discrete_sequence=px.colors.qualitative.Set3,
                        barmode="group",
                        barnorm="percent")
monthhist.update_traces(marker_line_width=1, marker_line_color= "yellow")
monthhist.update_layout(yaxis=dict(title_text="Percent", title_font_size=16), 
                          xaxis=dict(title_text="Month Name", title_font_size=16, dtick=10),
                         legend_bordercolor="#ffb3b3",
                         legend_borderwidth=1.5,
                         legend_font_family="PT Sans Narrow",
                         legend_title="Word Category")


# In[26]:


fig11 = px.scatter(summarydf, x='death ratio', y='month', color='WordCat', facet_col='decades', facet_col_wrap=4)


# ## Date time

# Summary:
# More recent decades caused more deaths
# Winter has the most deaths

# In[27]:


decade_word2 = px.histogram(summarydf, x="decades", color="day_name", 
                           color_discrete_sequence=px.colors.qualitative.Set3,
                          barmode="group",
                          barnorm="percent")
decade_word2.update_traces(marker_line_width=1, marker_line_color= "silver")
decade_word2.update_layout(yaxis=dict(title_text="Percent", title_font_size=16), 
                          xaxis=dict(title_text="Decades", title_font_size=16, dtick=10),
                         legend_bordercolor="#ffb3da",
                         legend_borderwidth=1.5,
                         legend_font_family="Overpass",
                         legend_title="Day")


# In[28]:


decade_word3 = px.histogram(summarydf, x="decades", color="month_name", 
                           color_discrete_sequence=px.colors.qualitative.Set3,
                          barmode="group",
                          barnorm="percent")
decade_word3.update_traces(marker_line_width=1, marker_line_color= "gold")
decade_word3.update_layout(yaxis=dict(title_text="Percent", title_font_size=16), 
                          xaxis=dict(title_text="Decades", title_font_size=16, dtick=10),
                         legend_bordercolor="#ccccff",
                         legend_borderwidth=1.5,
                         legend_font_family="Times New Roman",
                         legend_title="Month")


# In[29]:


fig12 = px.choropleth(summarydf.groupby(["country1","season"])["Fatalities"].sum().reset_index().sort_values("season"), 
              locations="country1", 
              locationmode="country names", 
              color="Fatalities",
              color_continuous_scale=px.colors.sequential.Peach,
              projection="orthographic",
             animation_frame="season",
             category_orders={"season":["Spring","Summer","Autumn","Winter"]})



# In[32]:


fig13 = px.sunburst(summarydf, path=['season','WordCat'], values="Fatalities")


# In[33]:


fig14 = px.sunburst(summarydf, path=['season','WordCat'], values="Ground")


# In[34]:


fig15 = px.sunburst(summarydf, path=['day_name','WordCat'], values="Fatalities")


# In[35]:


fig16 = px.sunburst(summarydf.groupby(["day_name","WordCat"])['death ratio'].mean().reset_index(),
            path=['day_name','WordCat'], values="death ratio", branchvalues='total')


# In[36]:


fig17= px.sunburst(summarydf,
            path=['day_name','WordCat'], values="death ratio", branchvalues='total')


# In[37]:


fig18 = px.sunburst(summarydf, path=['season','day_name','WordCat'], values="death ratio", branchvalues='total')


# Thursday has the most overall death ratio, but saturday has the highest average death ratio

# In[38]:


fig19 = px.box(summarydf, x="death ratio")



fig20 = px.sunburst(summarydf, path=['season','Survivors'])
fig21 = px.sunburst(summarydf, path=['day_name','Survivors'])
# # Writing Part

# ## Abstract

# This case study uses a dataset provided by THE DEVASTATOR on Kaggle and analyzes the factors that influence plane crashes. After making assumptions and conducting simulations to prove them, conclusions were made that the amount of deaths in plane crashes are caused by multipule factors. Select from the sidebar to see the full case study.

# ## Background info

# Nowadays, the rate of plane crashes is very low. However, plane crashes are disasters and causes depressing consequences to the people on the plane and on the grounds once they happen. “I want to express sympathy to the families who lost loved ones to this terrible tragedy.” said Graham Dallas, at a media briefing after the Boeing B-17G and Bell p-63F planes collided. after finding out on a magazine that plane crashes are caused from different, interesting reasons I decided to investigate further about how to prevent these kinds of disasters. 
# 
# 
# I found a dataset on Kaggle about plane crashes. It is very interesting and included many it had data from the beginning of the 1900s. Please see the dataset below:
# 
# 
# A very useful column of the dataset for my investigation was the Summary column, as it shows the reasons of the plane crash. 
