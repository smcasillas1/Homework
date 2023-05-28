
# Capstone - Analysis of Ohio Crime from 2020 - 2022

## Capstone Context and Business Case:

    Context: Often times people move because of a work requirement, seeking a different level of cost of living, and/or they enjoy what a particular city or state has to offer, entertainment-wise. However, I know in my case I have never truly understood how safe/unsafe an area has been when deciding to move to a desired city/state.

    My intent with this project is to finally conduct an analysis on the types of crime that occurs in Ohio. This project can be beneficial to anyone who would like to understand crimes in Ohio - current/future Ohio residents and/or State/Local Government officials who want to understand how crime has trended from 2020-2022. The latter audience can also use this information to understand what types of laws, resources, and/or police training/staffing may be needed to deter/reduce the types of crimes that have occurred.

    Capstone questions I want to answer:

    1. What are the major types of crime that occurs in Ohio state by City/County?
    2. Are there certain types of crimes that are more common in small, medium, and large cities?
    3. What is the year-over-year trend of crime throughout the buckeye state?
    4. Are there any surprises from the crime datasets?


## Audience

    My audience will be any current or potentially new Ohio residents interested in the crime rates thrhoughout the city, area to which they currently live or anticipate on living. Also, those who work for the State of Ohio government may try to understand crime data trends to understand if there needs to be additional governmental programs or legislation with the hopes of deterring/reducing crime.

## Datasets

    I will need datasets from Criminal Justice related agencies either at the Ohio State or Federal Government levels which will have crime data by city for the years I would like to analyze. I have completed my search via an applicable Ohio state governmental website and found crime related datasets at:

        1. Crime data from Office of Criminal Justice Services:
            a. Website of Source Files: <https://dpsoibrspext.azurewebsites.net/?handler=Search>
            b. Actual .csv data files:
                b1. OIBRS_Crime_Data_2020
                b2. OIBRS_Crime_Data_2021
                b3. OIBRS_Crime_Data_2022
        2. City and County Mapping Source:
            a. <https://www.whereig.com/usa/zipcodes/ohio.html>


    I selected the crime source data mentioned above because it comes directly from Ohio State government and it has each reported crime type that occurred by city. Also, I selected the City and County mapping source because it has a website table that includes the county to which each Ohio city belongs to. This will be helpful in assigning each City to it's respective County hereby providing additional level of reporting detail.

## Dataset Plans

    My plan with the data I've found is to combine both datasets in a way that I'm able to produce several data visualizations that will show the yearly total of crimes with year over year trends, types of crimes that occurred in small/medium/large cities, and show city/county level crime concentration.

    This will be possible by:

        1. Consolidating/Appending each year of crime data included in each .csv file
        2. Webscraping the Ohio City and County mapping and exporting it to a .csv file
        3. Clean the data files accordingly.
        4. Merging clean copies of the consolidated crime data and the city/county mapping files together so that I can have all of the necessary data together in one place.
        5. Import them into Tableau to create desired visualizations.