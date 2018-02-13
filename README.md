# Table of Contents
1. [Summary](README.md#introduction)
2. [Architecture](README.md#architecture)
3. [Configuration](README.md#configuration)
4. [Project Structure](README.md#project-structure)
5. [Sample Data](README.md#sample-data)


# Introduction

This is the code develope fo the Insight challenge were was to build a service to calculate the percentile and other values for committees 
that have receive donations from repeated donors. 

# Architecture

For the soluction we have dived the data processing in diferent function to be able to reuse and separarte from different concerns. This allow 
to improve the quality of the services in the future and facilitateded the mainteinability. We have create two main file the main.py 
and the util.py in which we separate the overall processing from the reusable fucntions.

The main aspect that we look to addres with the sepration of concers are the follwing: 
	
	## Load Configuration
	## Load Data 
	## Clean Data
	## Data Preparation
	## Calculation 
	## Processing
	
![donators-analytics-arch](https://drive.google.com/open?id=1DBm8hJZHdXNCQLwNYPdlNfqQ-QHOv0Wg)


# Configuration

Path of the diferent files handle by the application are define in the main.py. We have see there is an issue handling the relative path
when execute the the test1. So you can modify the file location as needed in the main.py 

  ### percentile: ../input/percentile.txt
  ### itcont: ../input/itcont.txt
  ### repeat_donors: ../input/repeat_donors.txt
  

# Project Structure
The directory structure for your repo should look like this:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── donation-analytics.py
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
            ├── your-own-test_1
                ├── input
                │   └── your-own-input-for-itcont.txt
                |── output
                    └── repeat_donors.txt
					

##### Sample Data

**`percentile.txt`**
> **30**

**`itcont.txt`**

> **C00384516**|N|M2|P|201702039042410894|15|IND|**SABOURIN, JOE**|LOOKOUT MOUNTAIN|GA|**028956146**|UNUM|SVP, CORPORATE COMMUNICATIONS|**01312016**|**484**||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339

> **C00384516**|N|M2|P|201702039042410894|15|IND|**SABOURIN, JOE**|LOOKOUT MOUNTAIN|GA|**028956146**|UNUM|SVP, CORPORATE COMMUNICATIONS|**01312015**|**384**||PR2283904845050|1147350||P/R DEDUCTION ($192.00 BI-WEEKLY)|4020820171370029339

> **C00384516**|N|M2|P|201702039042410893|15|IND|**SABOURIN, JOE**|LOOKOUT MOUNTAIN|GA|**028956146**|UNUM|SVP, CORPORATE COMMUNICATIONS|**01312017**|**230**||PR1890575345050|1147350||P/R DEDUCTION ($115.00 BI-WEEKLY)|4020820171370029335

**`repeat_donors.txt`**

    C00384516|02895|2017|230|230|1