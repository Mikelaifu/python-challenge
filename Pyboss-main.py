import pandas as pd

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
filecsvname = input("what is the filename: ")


# employee_data1.csv & employee_data2.csv

data = pd.read_csv(filecsvname, parse_dates =["DOB"])

data[["First Name", "Last Name"]] = data["Name"].str.split(" ", expand = True) # seperate frist and last name 

for state , abbrev in us_state_abbrev.items()  :
    data["State"] = data["State"].str.replace (str(state), str(abbrev) )# change state name


digit = data["SSN"].str.split("-")
digitlist = []
for row in digit :
    row[0] = "***-"
    row[1] ="**-"
    x = pd.Series([row[0], row[1], row[2]]).str.cat()
    digitlist.append(x)
data["SSN"] = digitlist                                                   # -- change the format of SSN column

# -------------------change the format of DOB----------------------
data["DOB"] = pd.to_datetime(data["DOB"]).dt.strftime('%m/%d/%Y')       # change the format of DOB

 # to moderate the position of columns
data.head()
cols = data.columns.tolist()
cols = cols[-2:] + cols[:-2]
finalcsv = data[cols].drop(columns = "Name")

finalcsv.to_csv("Pyboss_employee.csv", index = False)