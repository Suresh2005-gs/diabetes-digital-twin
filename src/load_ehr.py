# load and clean the Synthea CSVs

"""
It's general Synthea data (Massachusetts patients), not diabetes-specific. 
The first rows are children with wellness visits, so I can't yet tell how many Type 2 Diabetes patients exist. 
Checking that is the next read-only step, and it decides how load_ehr.py filters patients.
patients.csv has identity columns (SSN, DRIVERS, PASSPORT, names, ADDRESS). 
They're synthetic, but we'll drop them in load_ehr.py so the pipeline and dashboard never carry them.
observations.csv stores everything in one long table. 
Each row has a CODE, a DESCRIPTION and a VALUE, and VALUE is text, so HbA1c, glucose, BMI and blood pressure must be filtered by code and converted to numbers.
Date formats are mixed. conditions.csv uses plain dates, and the other files use timestamps ending in Z.
The data is US-based, while the challenge asks for a condition prevalent in India. 
The README should state this honestly, e.g. that the US-synthetic data is a stand-in for the PoC and the pipeline works with any EHR in the same format."""