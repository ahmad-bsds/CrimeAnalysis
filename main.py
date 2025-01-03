try:
    import pandas as pd
    from datetime import datetime
    def transform_and_save(file_path):
        # Read the CSV file using pandas
        df = pd.read_csv(file_path)

        #-----------------
        
        # Drop specified columns
        df.drop(['Crm Cd 2', 'Crm Cd 3', 'Crm Cd 4', 'Cross Street', 'LOCATION', 'Status', 'Crm Cd 1'], axis=1, inplace=True)

        #------------------
        #Missing Values:

        df[['Weapon Used Cd']] = df[['Weapon Used Cd']].fillna('Not applicable.')

        # Specify the patterns and their corresponding mocode:
        pattern_mocode_mapping = {
            'Bunco, Attempt': '1701',
            'THREATENING PHONE CALLS/LETTERS': '1421 1912 2000',
            'THEFT FROM MOTOR VEHICLE - ATTEMPT': '1300',
            'SHOPLIFTING - ATTEMPT': '0325 0344 1822',
            'SHOPLIFTING - PETTY THEFT \(\$950 \& UNDER\)': '1300 1822 0344 1606',
            'THEFT FROM PERSON - ATTEMPT': '1822',
            'SHOPLIFTING-GRAND THEFT \(\$950.01 \& OVER\)': '0300',
            'RECKLESS DRIVING': '1300 1800',
            'INDECENT EXPOSURE': '0500',
            'Sexual Penetration W/Foreign Object': '0500',
            'Lewd/Lascivious Acts With Child': '0500',
            'RAPE, ATTEMPTED': '0500',
            'VEHICLE - STOLEN': '0330',
            'THEFT FROM MOTOR VEHICLE - PETTY \(\$950 & UNDER\)': '1300',
            'THEFT OF IDENTITY': '0933',
            'VEHICLE - ATTEMPT STOLEN': '0916',
            'THEFT FROM MOTOR VEHICLE - GRAND \(\$950.01 AND OVER\)': '1344',
            'THEFT PLAIN - PETTY \($950 & UNDER\)': '0334',
            'BATTERY - SIMPLE ASSAULT': '0416',
            'LEWD CONDUCT': '0563',
            'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT': '0406',
            'LETTERS, LEWD  -  TELEPHONE CALLS, LEWD': '0520',
            'INTIMATE PARTNER - SIMPLE ASSAULT': '0527',
            'INTIMATE PARTNER - AGGRAVATED ASSAULT': '0500',
            'KIDNAPPING - GRAND ATTEMPT': '0418',
            'ORAL COPULATION': '1512',
            'ARSON': '2000',
            'OTHER MISCELLANEOUS CRIME': '1501',
            'SEX OFFENDER REGISTRANT OUT OF COMPLIANCE': '0500',
            'RESISTING ARREST': '1501',
            'RAPE, FORCIBLE': '0545',
            'OTHER ASSAULT': '0416',
            'STALKING': '0347',
            'PROWLER': '1318',
            'SHOPLIFTING - PETTY THEFT \($950 & UNDER\)': '0300',
            'PEEPING TOM': '0500',
            'ROBBERY': '0365',
            'SEX,UNLAWFUL\(INC MUTUAL CONSENT, PENETRATION W/ FRGN OBJ': '0533',
            'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT': '0406',
            'ASSAULT WITH DEADLY WEAPON ON POLICE OFFICER': '0406',
            'ATTEMPTED ROBBERY': '0365',
            'BATTERY POLICE \(SIMPLE\)': '0416',
            'BIKE - STOLEN': '1300',
            'BATTERY WITH SEXUAL CONTACT': '0500',
            'BEASTIALITY, CRIME AGAINST NATURE SEXUAL ASSLT WITH ANIM': '0500',
            'BOAT - STOLEN': '1311',
            'BOMB SCARE': '0403',
            'BRANDISH WEAPON': '0334',
            'BLOCKING DOOR INDUCTION CENTER': '0300',
            'BRIBERY': '1271',
            'BURGLARY': '0900',
            'BURGLARY, ATTEMPTED': '0900',
            'BURGLARY FROM VEHICLE': '0900',
            'CHILD ABUSE \(PHYSICAL\) - AGGRAVATED ASSAULT': '0800',
            'BUNCO, PETTY THEFT': '0800',
            'BUNCO, GRAND THEFT': '0800',
            'BURGLARY FROM VEHICLE, ATTEMPTED': '0900', 
            'VEHICLE, STOLEN - OTHER \(MOTORIZED SCOOTERS, BIKES, ETC\)': '1300',
            #---------------------
            'VANDALISM - MISDEAMEANOR \(\$399 OR UNDER\)': '1111',
            'CRIMINAL THREATS - NO WEAPON DISPLAYED': '2222',
            'SEX OFFENDER REGISTRANT OUT OF COMPLIANCE': '3333',
            'THEFT-GRAND \(\$950.01 & OVER\)EXCPT,GUNS,FOWL,LIVESTK,PROD': '4444',
            'CHILD NEGLECT \(SEE 300 W.I.C.\)': '5555',
            'EMBEZZLEMENT, GRAND THEFT \(\$950.01 & OVER\)': '6666',
            'CRM AGNST CHLD \(13 OR UNDER\) \(14-15 & SUSP 10 YRS OLDER\)': '7777',
            'DOCUMENT WORTHLESS \(\$200 & UNDER\)': '8888',
            'FAILURE TO YIELD': '9999',
            'VEHICLE - ATTEMPT STOLEN': '0000',
            'TRESPASSING': '1111',
            'CHILD ABUSE \(PHYSICAL\) - AGGRAVATED ASSAULT': '2222',
            'DEFRAUDING INNKEEPER/THEFT OF SERVICES, OVER \$950.01': '3333',
            'DEFRAUDING INNKEEPER/THEFT OF SERVICES, \$950 & UNDER': '4444',
            'DEFRAUDING INNKEEPER/THEFT OF SERVICES, \$950 & UNDER': '4444',
            'DOCUMENT FORGERY / STOLEN FELONY': '5555',
            'DISCHARGE FIREARMS/SHOTS FIRED': '6666',
            'DRIVING WITHOUT OWNER CONSENT \(DWOC\)': '7777',
            'VANDALISM - FELONY \(\$400 & OVER, ALL CHURCH VANDALISMS\)': '8888',
            'UNAUTHORIZED COMPUTER ACCESS': '9999',
            'CHILD PORNOGRAPHY': '0000',
            'THEFT PLAIN - PETTY \(\$950 & UNDER\)': '1111',
            'CHILD ABUSE \(PHYSICAL\) - SIMPLE ASSAULT': '2222',
            'THEFT, PERSON': '3333',
            'VIOLATION OF COURT ORDER': '4444',
            'VIOLATION OF RESTRAINING ORDER': '5555',
            'HUMAN TRAFFICKING - INVOLUNTARY SERVITUDE': '6666',
            'CHILD STEALING': '7777',
            'THROWING OBJECT AT MOVING VEHICLE': '8888',
            'RESISTING ARREST': '9999',
            'VIOLATION OF TEMPORARY RESTRAINING ORDER': '0000',
            'DISTURBING THE PEACE': '1111',
            'EXTORTION': '2222',
            'CRIMINAL HOMICIDE': '3333',
            'THEFT PLAIN - ATTEMPT': '4444',
            'REPLICA FIREARMS\(SALE,DISPLAY,MANUFACTURE OR DISTRIBUTE\)': '5555',
            'CREDIT CARDS, FRAUD USE \(\$950 & UNDER': '6666',
            'ILLEGAL DUMPING': '7777',
            'FALSE POLICE REPORT': '8888',
            'CHILD ANNOYING \(17YRS & UNDER\)': '9999',
            'FALSE IMPRISONMENT': '0000',
            'CONTEMPT OF COURT': '1111',
            'HUMAN TRAFFICKING - COMMERCIAL SEX ACTS': '2222',
            'COUNTERFEIT': '3333',
            'CREDIT CARDS, FRAUD USE \(\$950.01 & OVER\)': '4444',
            'PROWLER': '5555',
            'CRUELTY TO ANIMALS': '6666',
            'SHOTS FIRED AT INHABITED DWELLING': '7777',
            'WEAPONS POSSESSION/BOMBING': '8888',
            'CONSPIRACY': '9999',
            'CONTRIBUTING': '0000',
            'DOCUMENT WORTHLESS \(\$200.01 & OVER\)': '1111',
            'PICKPOCKET': '2222',
            'SHOTS FIRED AT MOVING VEHICLE, TRAIN OR AIRCRAFT': '3333',
            'DISRUPT SCHOOL': '4444',
            'SODOMY/SEXUAL CONTACT B/W PENIS OF ONE PERS TO ANUS OTH': '5555',
            'PANDERING': '6666',
            'PIMPING': '7777',
            'PETTY THEFT - AUTO REPAIR': '8888',
            'EMBEZZLEMENT, PETTY THEFT \(\$950 & UNDER\)': '9999',
            'GRAND THEFT / INSURANCE FRAUD': '0000',
        }
        # Iterate through the pattern_mocode_mapping and update 'Mocodes' based on the patterns
        for pattern, mocode in pattern_mocode_mapping.items():
            # Select rows where 'Crm Cd Desc' contains the pattern and 'Mocodes' is null
            rows_to_update = df['Crm Cd Desc'].str.contains(pattern, case=False, na=False) & df['Mocodes'].isnull()

            # Fill NA values in 'Mocodes' for selected rows
            df.loc[rows_to_update, 'Mocodes'] = mocode

        
        # Identify rows where 'Crime Cd' contains 'VEHICLE-STOLEN'
        pattern = r'ARSON'
        rows_to_update = df['Crm Cd Desc'].str.contains(pattern, case=False, na=False) & df['Weapon Desc'].isnull()
        df.loc[rows_to_update, 'Weapon Desc'] = 'Fire'
        rows_to_update = df['Crm Cd Desc'].str.contains(pattern, case=False, na=False) & df['Weapon Used Cd'].isnull()
        df.loc[rows_to_update, 'Weapon Used Cd'] = 'Fire.'

        # Identify rows where 'Crime Cd' contains 'VEHICLE-STOLEN'
        pattern = r'VEHICLE, STOLEN - OTHER \(MOTORIZED SCOOTERS, BIKES, ETC\)'

        #replace for short.
        df['Crm Cd Desc'] = df['Crm Cd Desc'].str.replace(pattern, 'TWO-WHEEL-STOLEN')

        #-------------------------------------------------
        #Transform values:
        df['Vict Descent'] = df['Vict Descent'].fillna('unknown')
        df['Vict Sex'] = df['Vict Sex'].fillna('unknown')

        df['Vict Descent'] = df['Vict Descent'].replace('-', 'unknown/none')
        df['Vict Descent'] = df['Vict Descent'].replace('A', 'Other Asian')
        df['Vict Descent'] = df['Vict Descent'].replace('B', 'Black')
        df['Vict Descent'] = df['Vict Descent'].replace('C', 'Chinese')
        df['Vict Descent'] = df['Vict Descent'].replace('D', 'Cambodian')
        df['Vict Descent'] = df['Vict Descent'].replace('F', 'Filipino')
        df['Vict Descent'] = df['Vict Descent'].replace('G', 'Guamanian')
        df['Vict Descent'] = df['Vict Descent'].replace('H', 'Hispanic/Latin/Mexican')
        df['Vict Descent'] = df['Vict Descent'].replace('I', 'American Indian/Alaskan Native')
        df['Vict Descent'] = df['Vict Descent'].replace('J', 'Japanese')
        df['Vict Descent'] = df['Vict Descent'].replace('K', 'Korean')
        df['Vict Descent'] = df['Vict Descent'].replace('L', 'Laotian')
        df['Vict Descent'] = df['Vict Descent'].replace('O', 'Other')
        df['Vict Descent'] = df['Vict Descent'].replace('P', 'Pacific Islander')
        df['Vict Descent'] = df['Vict Descent'].replace('S', 'Samoan')
        df['Vict Descent'] = df['Vict Descent'].replace('U', 'Hawaiian')
        df['Vict Descent'] = df['Vict Descent'].replace('V', 'Vietnamese')
        df['Vict Descent'] = df['Vict Descent'].replace('W', 'White')
        df['Vict Descent'] = df['Vict Descent'].replace('X', 'Unknown')
        df['Vict Descent'] = df['Vict Descent'].replace('Z', 'Asian Indian')

        df['Vict Sex'] = df['Vict Sex'].replace('-', 'unknown')
        df['Vict Sex'] = df['Vict Sex'].replace('X', 'unknown')
        df['Vict Sex'] = df['Vict Sex'].replace('F', 'Female')
        df['Vict Sex'] = df['Vict Sex'].replace('M', 'Male')
        df['Vict Sex'] = df['Vict Sex'].replace('H', 'Homo-sexual')

        # Identify rows where 'Crime Cd' contains 'VEHICLE-STOLEN'
        df['Premis Cd'] = df['Premis Cd'].astype('string')

        pattern = r'256'
        vehicle_stolen_rows = df['Premis Cd'].str.contains(pattern, case=False, na=False)

        # Fill NA values in 'Monocodes' for rows identified above
        df['Premis Desc'] = df['Premis Desc'].mask(vehicle_stolen_rows, 'APARTMENT, MULTI-FAMILY STRUCTURE \(4 OR MORE UNITS\)')


        pattern = r'418'
        vehicle_stolen_rows = df['Premis Cd'].str.contains(pattern, case=False, na=False)

        # Fill NA values in 'Monocodes' for rows identified above
        df['Premis Desc'] = df['Premis Desc'].mask(vehicle_stolen_rows, 'Public')

        # Identify rows where 'Crime Cd' contains 'VEHICLE-STOLEN'
        pattern = r'972'
        vehicle_stolen_rows = df['Premis Cd'].str.contains(pattern, case=False, na=False)

        # Fill NA values in 'Monocodes' for rows identified above
        df['Premis Desc'] = df['Premis Desc'].mask(vehicle_stolen_rows, 'SINGLE-FAMILY HOUSE (DETACHED)')

        # Identify rows where 'Crime Cd' contains 'VEHICLE-STOLEN'
        pattern = r'973'
        vehicle_stolen_rows = df['Premis Cd'].str.contains(pattern, case=False, na=False)

        # Fill NA values in 'Monocodes' for rows identified above
        df['Premis Desc'] = df['Premis Desc'].mask(vehicle_stolen_rows, 'SINGLE-FAMILY HOUSE (ATTACHED)')

        # Identify rows where 'Crime Cd' contains 'VEHICLE-STOLEN'
        pattern = r'974'
        vehicle_stolen_rows = df['Premis Cd'].str.contains(pattern, case=False, na=False)

        # Fill NA values in 'Monocodes' for rows identified above
        df['Premis Desc'] = df['Premis Desc'].mask(vehicle_stolen_rows, 'Candominium')

        # Identify rows where 'Crime Cd' contains 'VEHICLE-STOLEN'
        pattern = r'976'
        vehicle_stolen_rows = df['Premis Cd'].str.contains(pattern, case=False, na=False)
        df['Premis Desc'] = df['Premis Desc'].mask(vehicle_stolen_rows, 'Town House')

        df['Premis Desc'] = df['Premis Desc'].fillna('Unknown')

        df.drop(['Premis Cd'], axis=1, inplace=True)        
        df.drop(['Weapon Used Cd'], axis=1, inplace=True)

        df['Weapon Desc'] = df['Weapon Desc'].fillna('No/UNKNOWN WEAPON/OTHER WEAPON')
        #df['Weapon Desc'] = df['Weapon Desc'].str.replace('UNKNOWN WEAPON/OTHER WEAPON', 'No/UNKNOWN WEAPON/OTHER WEAPON')

        ######################....................######################
        df = df.map(lambda x: x.title() if isinstance(x, str) else x)


        # Split mocodes:
        df['Mocodes'] = df['Mocodes'].astype('str') 
        max_splits = df['Mocodes'].str.count(' ').max() + 1
        column_names = [f'Mocodes_{i}' for i in range(1, max_splits + 1)]
        df[column_names] = df['Mocodes'].str.split(' ', expand=True).fillna(0).astype(str)

        # Create a list of the old column names
        old_column_names = [
        "DR_NO",
        "Date Rptd",
        "DATE OCC",
        "TIME OCC",
        "AREA",
        "AREA NAME",
        "Rpt Dist No",
        "Part 1-2",
        "Crm Cd",
        "Crm Cd Desc",
        "Vict Age",
        "Vict Sex",
        "Vict Descent",
        "Premis Cd",
        "Premis Desc",
        "Weapon Used Cd",
        "Weapon Desc",
        "Status",
        "Status Desc",
        "Crm Cd 1",
        "LOCATION",
        "LAT",
        "LON",
        ]

        # Create a list of the new column names
        new_column_names = [
        "DR_NO",
        "Date_Rptd",
        "DATE_OCC", 
        "TIME_OCC",
        "AREA",
        "AREA_NAME",
        "RPT_DIST_NO",
        "PART_1_2",
        "CRMCD",
        "CRMCD_DESC",
        "VICT_AGE",
        "VICT_SEX",
        "VICT_DESCENT",
        "PREMIS_CD",
        "PREMIS_DESC",
        "WEAPON_USED_CD",
        "WEAPON_DESC",
        "STATUS",
        "STATUS_DESC",
        "CRM_CD",
        "LOCATION",
        "LAT",
        "LON",
        ]

        # Create a dictionary that maps old column names to new column names
        column_mapping = dict(zip(old_column_names, new_column_names))

        # Rename the columns
        df = df.rename(columns=column_mapping)


        # Changing datatypes:
        df['DR_NO'] = df['DR_NO'].astype('int64')
        df['Date_Rptd'] = pd.to_datetime(df['Date_Rptd'])
        df['DATE_OCC'] = pd.to_datetime(df['DATE_OCC'])
        df['AREA'] = df['AREA'].astype('int64')
        df['RPT_DIST_NO'] = df['RPT_DIST_NO'].astype('int64')
        df['PART_1_2'] = df['PART_1_2'].astype('int64')
        df['CRMCD'] = df['CRMCD'].astype('str')
        df['VICT_AGE'] = df['VICT_AGE'].astype('int64')
        df['VICT_SEX'] = df['VICT_SEX'].astype('str') 
        df['VICT_DESCENT'] = df['VICT_DESCENT'].astype('str') 
        df['LAT'] = df['LAT'].astype('float64')
        df['LON'] = df['LON'].astype('float64')

        # transforming time:
        

        def convert_to_12h_format(time_str):
            try:
                # Ensure the input time string has at least 4 characters
                time_str = str(time_str).rjust(4, '0')

                # Check if the time string contains a colon
                if ':' not in time_str:
                    # If not, insert a colon between the hour and minute components
                    time_str = f'{time_str[:2]}:{time_str[2:]}'

                # Parse the input time string in 24-hour format
                time_object = datetime.strptime(time_str, '%H:%M')

                # Format the time in 12-hour format
                time_12h = time_object.strftime('%I:%M %p')

                return time_12h
            except ValueError:
                raise ValueError("Invalid time format")


        # Apply the custom function to each cell in the specified columns
        df['TIME_OCC'] = df['TIME_OCC'].apply(convert_to_12h_format)


        # Classification dictionary for the specified categories
        crmcd = {
            '435': 'Simple Assaults',
            '436': 'Simple Assaults',
            '437': 'Simple Assaults',
            '622': 'Simple Assaults',
            '623': 'Simple Assaults',
            '624': 'Simple Assaults',
            '625': 'Simple Assaults',
            '626': 'Simple Assaults',
            '627': 'Simple Assaults',
            '647': 'Simple Assaults',
            '763': 'Simple Assaults',
            '928': 'Simple Assaults',
            '930': 'Simple Assaults',
            '310': 'Burglary',
            '320': 'Burglary',
            '510': 'Motor Vehicle Theft (MVTGTA)',
            '520': 'Motor Vehicle Theft (MVTGTA)',
            '433': 'Motor Vehicle Theft (MVTGTA)',
            '330': 'Burglary',
            '331': 'Breaking and Entering of a Vehicle (BTFV)',
            '410': 'Burglary',
            '420': 'Breaking and Entering of a Vehicle (BTFV)',
            '421': 'Breaking and Entering of a Vehicle (BTFV)',
            '350': 'Personal Theft',
            '351': 'Personal Theft',
            '352': 'Personal Theft',
            '353': 'Personal Theft',
            '450': 'Personal Theft',
            '451': 'Personal Theft',
            '452': 'Personal Theft',
            '453': 'Personal Theft',
            '341': 'Other Theft',
            '343': 'Other Theft',
            '345': 'Other Theft',
            '440': 'Other Theft',
            '441': 'Other Theft',
            '442': 'Other Theft',
            '443': 'Other Theft',
            '444': 'Other Theft',
            '445': 'Other Theft',
            '470': 'Other Theft',
            '471': 'Other Theft',
            '472': 'Other Theft',
            '473': 'Other Theft',
            '474': 'Other Theft',
            '475': 'Other Theft',
            '480': 'Other Theft',
            '485': 'Other Theft',
            '487': 'Other Theft',
            '491': 'Other Theft',
            '110': 'Homicide',
            '113': 'Homicide',
            '121': 'Rape',
            '122': 'Rape',
            '815': 'Rape',
            '820': 'Rape',
            '821': 'Rape',
            '210': 'Robbery',
            '220': 'Robbery',
            '230': 'Aggravated Assaults',
            '231': 'Aggravated Assaults',
            '235': 'Aggravated Assaults',
            '236': 'Aggravated Assaults',
            '250': 'Aggravated Assaults',
            '251': 'Aggravated Assaults',
            '761': 'Other', # Brandish Weapon
            '926': 'Aggravated Assaults', 
            '845': 'Other', # Sex Offender Registrant Out Of Compliance.
            '745': 'Burglary',
            '740': 'Robbery',
            '648': 'Aggravated Assaults',
            '354': 'Other', # theft of Identity.
            '662': 'Other Theft',
            '860': 'Rape', 
            '956': 'Other', # Letters; Lewd  -  Telephone Calls; Lewd
            '886': 'Other', # Disturbing the peace.
            '922': 'Other Theft',
            '755': 'Other', #Bombscare.
            '649': 'Other Theft',
            '850': 'Robbery',
            '668': 'Other Theft',
            '920': 'Other', # kidnapping.
            '910': 'Other', # kidnapping.
            '661': 'Other', #Un-authorized computer access.
            '237': 'Other', # Child Neglect (See 300 W.I.C.)
            '903': 'Personal Theft',
            '666': 'Other Theft',
            '805': 'Other', #Pimping.
            '434': 'Other', # false imprisonment.
            '670': 'Robbery',
            '951': 'Other Theft', # Defrauding Innkeeper/Theft Of Services; $950 & Under
            '660': 'Simple Assaults',
            '654': 'Other', #Credit card fraud.
            '933': 'Other', # pecha kerna.
            '652': 'Burglary', # Document Worthless ($200 & Under)
            '950': 'Personal Theft',
            '822': 'Other', #humman traffiking.
            '932': 'Other', #peeping tom.
            '921': 'Other', #humman traffiking.
            '906': 'Other', # Firearm restraining.
            '943': 'Other', # Cruelty To Animals
            '439': 'Other', # false police report.
            '806': 'Other', #Pandering.
            '949': 'Other', #Dumping.
            '522': 'Breaking and Entering of a Vehicle (BTFV)',
            '446': 'Personal Theft',
            '438': 'Other', # rackless driving.
            '944': 'Other', # Conspiracy.
            '954': 'Other', # contributing.
            '756': 'Other', #weapon bombing.
            '942': 'Other', #Briebry.
            '347': 'Other Theft',
            '880': 'Other', # Disrupt school.
            '931': 'Other', #Replica firearm.
            '865': 'Other', #Drugs; To A Minor
            '349': 'Personal Theft',
            '870': 'Other', # Other child abandonment.
            '948': 'Other', #Bigamy
            '884': 'Other', # failure to disperse.
            '830': 'Rape',
            '432': 'Other', # Blocking Door Induction Center.
            '946': 'Other', # Other Miscellaneous Crime.
            '900': 'Other', # court violence.
            '888': 'Robbery',
            '901': 'Other', # Violation Of Restraining Order
            '940': 'Simple Assaults',
            '810': 'Other', # Sex;Unlawful(Inc Mutual Consent; Penetration W/ Frgn Obj
            '812': 'Other', #crime against child
            '902': 'Other', # Violation Of Temporary Restraining Order
            '664': 'Personal Theft',
            '753': 'Aggravated Assaults', # firearm short fired.
            '760': 'Rape', # lewd with child.
            '762': 'Rape',
            '813': 'Robbery',
            '890': 'Aggravated Assaults',
            '814': 'Other', # Sexual abuse.
            '651': 'Burglary',
            '653': 'Other', #credit card fraud.
            '924': 'Other',#Telephone Property - Damage
            '840': 'Other', # animal sex.
            '904': 'Other', # firearms protection .....
            '882': 'Other', #Inciat a riot.', 
            '740': 'Burglary',
            '903': 'Personal Theft',
            '666': 'Other Theft',
            '520': 'Motor Vehicle Theft (MVTGTA)',
            '670': 'Robbery',
            '438': 'Other Theft',
            '756': 'Robbery',
            '347': 'Simple Assaults',
        }

       


        # Replace codes with categories
        df['CRMCD'] = df['CRMCD'].replace(crmcd)


        # commas create trouble in csv. i.e while loading in redshift.
        # This code will replace , with ;


        df.drop(['Mocodes'], axis=1, inplace=True)
        df.drop(['AREA'], axis=1, inplace=True)

        # List of columns to replace ',' with ';'
        columns_to_replace = ['DR_NO', 'Date_Rptd', 'DATE_OCC', 'TIME_OCC', 'AREA_NAME',
                                       'RPT_DIST_NO', 'PART_1_2', 'CRMCD_DESC', 'VICT_AGE',
                                       'VICT_SEX', 'VICT_DESCENT', 'PREMIS_DESC', 'WEAPON_DESC', 'STATUS_DESC',
                                       'LAT', 'LON', 'Mocodes_1', 'Mocodes_2', 'Mocodes_3', 'Mocodes_4',
                                       'Mocodes_5', 'Mocodes_6', 'Mocodes_7', 'Mocodes_8', 'Mocodes_9',
                                       'Mocodes_10']

        # List of columns to process
        columns_to_process = ['Mocodes_1', 'Mocodes_2', 'Mocodes_3', 'Mocodes_4', 'Mocodes_5',
                               'Mocodes_6', 'Mocodes_7', 'Mocodes_8', 'Mocodes_9', 'Mocodes_10']

        # Custom function to extract the first two characters and handle zero values
        def process_value(value):
            if str(value)[:] == '0':
                return 0
            else:
                return int(str(value)[:2])

        # Apply the custom function to each cell in the specified columns
        for column in columns_to_process:
           df[column] = df[column].apply(process_value)

        # Replace ',' with ';'
        df[columns_to_replace] = df[columns_to_replace].replace(',', ';', regex=True)

        df.rename(columns={'CRMCD': 'CRIME_CATEGORIES'}, inplace=True)

        # Write the modified DataFrame back to the CSV file
        df.to_csv(file_path, index=False)

        


    # Specify the path to the CSV file
    file_path = r'D:\CrimeData\lacrime.csv'

    # Call the transform_and_save function
    transform_and_save(file_path)
    print("Operation successfull.")
except ImportError:
    print("Error!")

