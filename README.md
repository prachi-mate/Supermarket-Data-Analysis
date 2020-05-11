# Supermarket-Data-Analysis
Technologies used:
- Business Intelligence
- Database
- Python
- Tableau

The .csv files are a based on the dataset uploaded by walmart on Kaggle.The dataset is divided into 3 tables: Customer, Product & Transaction (all in .csv format). The tables have their own 'primary key' or 'table_id'. They are combined to form FACT table.
The csv files are loaded into SQL tables on localhost using commands given in file : prachidbcommands.txt  
The SQL is connected with python to display all tables using the python code given in: prachidbconnect.py
OLAP operations that are applied on the Fact table are- Slicing, Roll up, Pivot, Min & max
Machine learning algoritm- KMeans is used to analyse the data. The code is given in : prachikmeans.py and output is shown in prachikmeans.png
Tableau is used to visualize the data in geomaps, line chart, bar chart and motion chart. The tableau file is: prachibivisualization.twb and respective images of visualisations are uploaded as- prachilinev.PNG, prachimotionv.PNG, prachigeov.PNG and prachibarv.PNG
