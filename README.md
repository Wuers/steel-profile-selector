#  Steel Profile Selector

## Description
A programme that can support structural engineers in selecting the right steel profile based on the structural requirements entered.
Selection 

It was created in python and using a jupyter notebook to try to take advantage of the creation of a virtual environment and data processing with pandas

The selection is made on the basis of load calculations and material strengths according to the Eurocode. Engineering calculations are not the core of the programme, so the details are described in the code.

## Dependencies
All requirements are listed in requirments.txt. It is advised to create virtual env and use command:

    - pip install -r requirements.txt

to install all packages

## Usage
  Profiles Data:
  
  - You can import a steel profile catalogue e.g. from 
    [eurocodeapplied.com](https://eurocodeapplied.com/design/en1993/ipe-hea-heb-hem-design-properties)
    ![alt text](https://github.com/Wuers/steel-profile-selector/blob/master/img/download_data.jpg?raw=true)

    By using pandas, several spreadsheets can be merged one under the other as files for the application:
    ![alt text](https://github.com/Wuers/steel-profile-selector/blob/master/img/spreadsheet.jpeg?raw=true)
    

    
Structure loads, span and limitation of deflection could be customised in 

     shared_data.py 
  

## Future milestones:

In addition to the use of the above-mentioned tools, the application can be developed using optimisation functions to find the best solutions by comparing thousands of design options.

## Contact
[LinkedIn](https://www.linkedin.com/in/wiktor-sadowski-1385ba207/)

[Github](https://github.com/Wuers)
