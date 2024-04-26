#  Rule Based NER (Named Entity Recognition) and Model-Based NER to Identify Government Entities in Court Documents 

![Scales Image](data:image/png;base64,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)

## Project Overview
This project is part of the Spring 2024 Knowledge Centric AI hackathon hosted by [KnowHax](https://www.knowhax.com/).  The business problem being solved is identifying whether a government entity or person was involved in a court case soley utilizing a four column dataset with one column being that of'name' which was the primary column used to create the target labels of 'government' and 'person'.  This custom made target was created in two ways:  one being rules-based utilizing pattern recognition and the other being using a zero-shot large language model called GLiNER-medium-v2.1 found on [HuggingFace](https://huggingface.co/spaces/tomaarsen/gliner_medium-v2.1).  

## Business Problem
The United States Criminal Justice System spends a total of approximately $264B per year.  Limited national data exists about court systems more importantly who is being prosecuted and convicted and the outcomes of those convictions.  [SCALES](https://docs.scales-okn.org/nlp/) seeks to connect data systems within the criminal justics system to evaluate the efficiency of the court systems and subsequent outcomes for research purposes. This project in particular wanted to focus on identifying when governments are involved in suits (for example policing and prison entities) versus persons to help support research efforts about government entity conditions and ciminal justice system resources.   

## Data Overview 
The following was done by the project sponsor-SCALES
- Webscraped dockets from [PACER](https://pacer.uscourts.gov/) (Public Access to Court Electronic Records)
- Extracted named entities from each docket using a custom scraper
- These dockets covered several case lists that can be found [Here](https://docs.scales-okn.org/rdf/) covered national cases from 2002-2020.
- JSON and Turtle files can be downloaded [Here](http://scalesokndata.ci.northwestern.edu/#/home) (need to sign up for a FREE account)
- A CSV file was created with approximately 3.5 million rows from the above files
- Due to computational resources and time constraints the hacakathon team random sampled 100k rows from the CSV file which is found in the 'data' folder of this repo
- The following columns are in the above CSV file
     - **Name**:  A party name that appears in one or more cases
     - **Extra Info**:  Extra Info about the party that may/may not can be used (roughly 50% missing)
     - **Nature-of-suit Subtype**:  Type of case in which the party belongs to (i.e. immigration, criminal, habeaus corpus, etc.)
     - **UIDS**:  Case IDs for the underlying case files
  
  As mentioned above the **name** and **extra_info** columns were predominately used for this NER classifier

## Exploratory Data Analaysis (EDA) 
1. Entire Data File (100k observations) Top 4 Suit Subtypes that comprised 60% of all the data:
![Subtype Plot](images/subtype_countplot.png)

2. Word Cloud of the "formal titles" that existed in the data and thus would be classified as government:
![Dataset Word Cloud Formal Titles](images/df_wordcloud.png)

## Rule Based Methodology 
1. Create Rules that matches patterns within the name and/or extra_info columns to classify 'government' versus 'person'
2. Some examples of rules are as follows:
   - Column(s) contain a 'formal government title' (i.e. Police, District Attornet, Lieutenant, etc.)
   - Column(s) contain 'city of' or 'department of' (rationale these are mostly state counties involved in the suit which is government)
   - Column(s) DO NOT contain 'llc' (these are mostly 'persons')
3. Build a target based on the rules (binary target of label 'government' or 'person')
4. From that target create a predictive rule-based model, Decision Tree, that uses binary features to predict that target
5. Limitations:  The target was created based on finite rules that may not encompass ALL PATTERNS

## Model Performance on Rule Based Methodolgy
The rule based target we created captured a large amount of person entities and based on our hard formal rules we are confident it identified clear government entities from the **name** and **extra_info** columns. However, it had a significant number of rows that did not match any entity, showcasing the limitation of this method. Further rules would need to be investigated and added in, in order to capture more of the missed values. We were not able to capture all patterns due to time contraints.  

The decision tree model had an accuracy of 99% and Recall of 91% on unseen data.  False Negatives occured roughly 0.6% of the time -- the model stated it was a person (0) when in fact it was a government entity (1)

The top features included:  If the 'name' or 'extra_info' columns contained a formal government title and the 'name' field containing "city of":
![Decision Tree Model](images/decision_tree_shortened.png)

## Zero Shot GLiNER LLM Model Methodology and Code: 
1.  Import a foundational spacy NER model that can recognize 18 entities.  Model Documentation[Here](https://spacy.io/models/en#en_core_web_sm)
2.  Add custom labels to identify: 'government' and 'person'
3.  Add the zero shot labels to a sample of 2k observations (due to comptational resources needed a smaller data set)

Code: 
![Zero Shot Code](images/zeroshotmodel_code.png)

Results:  Matched the rule-based target created at 59%

Limitations:  Can generate more than one label for each observation, not good at picking up "formal titles" in front of names and assigning it as "government" 

## Tuned spaCy LLM Model using custom training data 
1.  Use Faker to generate fake English, Spanish, and English Indian names
2.  Create a text file of 'formal titles' (found in data folder) and of person suffixes (l.l.c, .inc, etc.)
3.  Append these files together to generate names with formal titles labeled 'government' and names with person suffixes labeled 'person'
4.  Add this custom data to the LLM pipe

Results: Variable with the worse assigning 'government' to all observations.  This still needs to be investigated but we have good 'starter code' in the notebook/  

## Learnings and Recommendations 
- Creating finite rules to determine a target then running a Machine Learning model against that target performs pretty well 

- The limitations are the difficulty in being able to define almost all the rules needed to create a robust target and having computational resources to train a foundational model with custom training data  

- Even though the zero-shot LLM model was ~59% accurate, it can still be used to identify names that were matched to both labels for further investigation and to help create more rules 

- Custom training data could potentially be used to train the model but computational (cloud) resources would be needed since it has difficulty performing on just a local machine 

## Future Steps 
1.  Create a cloud environment that can train the custom spaCy model
2.  Determine more rules that can separate 'government' from 'person' entities 

## Contact
- Angelica "Jelly" Spratley, MSc (Project and Technical lead):  [LinkedIn](https://www.linkedin.com/in/angelicaspratley/)
- Daniel Burdeno, MSc (Code Quality lead and Technical Assistant):  [LinkedIn](https://www.linkedin.com/in/daniel-burdeno/)
- Dr. Uohna Thiessen (Strategy and Creative lead):  [LinkedIn](https://www.linkedin.com/in/druohna-datascientist/) 
