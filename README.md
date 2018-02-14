# Table of Contents
1. [Summary](README.md#introduction)
2. [Architecture](README.md#architecture)
3. [Project Structure](README.md#project-structure)
4. [Configuration](README.md#configuration)
5. [Sample Data](README.md#sample-data)
6. [Result](README.md#result)
7. [Author](README.md#author)


# Introduction

This is the code develope fo the Insight challenge were was to build a service to calculate the percentile and other values for committees 
that have receive donations from repeated donors. 

I want to let you know that wining the opportunity to participate within your intership or not this challenge as been a grerat 
practice to my experince with the data science. For me the challage has been way to improve in my python skills that in the last 
month i have been study and develop which is a great win.

Thanks for the opportunity and have a great analysis.

# Architecture

For the soluction we have dived the data processing in diferent functions to be able to reuse and separarte from different concerns. 
This allow improve the quality of services and facilitateded the mainteinability. We have create two main file the main.py 
and the util.py in which we separate the overall processing from the reusable functions.

The main aspect that we look to address with the sepration of concers approach are: 
	
	## Load Configuration
	## Load Data 
	## Clean Data
	## Data Preparation
	## Calculation 
	## Processing
	
![donators-analytics-arch](https://github.com/avionero/donation-analytics/blob/master/images/donator-analytics-arch.PNG)

# Project Structure
The directory structure of the project develope:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── main.py
    │   └── util.py	
    │   └── path_config(.txt file)
	├── images
    │   └── donator-analytics-arch.png
	│   └── donator-analytics-result.png
    ├── input
    │   └── percentile.txt
    │   └── itcont.txt
    ├── output
    |   └── repeat_donors.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── percentile.txt
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── repeat_donors.txt
					
# Configurations and Execution

To run the program configure the file path as input parameters inside the run.sh script and execute it with the following command, "./run.sh",
within the project directory.

Each path in the run.sh script should be define as follow and in same order as show below.

  ### itcont: ./input/itcont.txt
  ### percentile: ./input/percentile.txt
  ### repeat_donors: ./output/repeat_donors.txt
  
  
##### Sample Data

**`percentile.txt`**
> **30**

**`itcont.txt`**

> **C00384516**|N|M2|P|201702039042410894|15|IND|**SABOURIN, JOE**|LOOKOUT MOUNTAIN|GA|**028956146**|UNUM|SVP, CORPORATE COMMUNICATIONS|**01312016**|**484**||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339

> **C00384516**|N|M2|P|201702039042410894|15|IND|**SABOURIN, JOE**|LOOKOUT MOUNTAIN|GA|**028956146**|UNUM|SVP, CORPORATE COMMUNICATIONS|**01312015**|**384**||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339

> **C00384516**|N|M2|P|201702039042410893|15|IND|**SABOURIN, JOE**|LOOKOUT MOUNTAIN|GA|**028956146**|UNUM|SVP, CORPORATE COMMUNICATIONS|**01312017**|**230**||PR1890575345050|1147350||P/R DEDUCTION ($115.00 BI-WEEKLY)|4020820171370029335

**`repeat_donors.txt`**

    C00384516|02895|2017|230|230|1
	
# Result

The below image despict the successful test result after execute the project with the run_tests.sh which execute the main project. 

![donators-analytics-result](https://github.com/avionero/donation-analytics/blob/master/images/donator-analytics-result.PNG)

# Author

Felix Lopes - prtechs@gmail.com
