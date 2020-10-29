## SAT-Analytics

### Overview
This repo contains analytic tools to explore data that is ingested from a World Modeler's Datamart. 

   1. Analytic Tools:
       
      A. Correlation: Return the Pearson's Correlation Coefficient for user selected variable and countries
      
      B. Time Series: Utilize Prophet to fit and forecast time series data from selected ISI variable_ids
      
      C. Download: Download datasets from ISI
      
      D. Search: Search the ISI Datamart for data of interest
      
      E. Visualization: Plot time series data for selected countries and variable id from the ISI Datamart
      
      F. Clustering: TBD
       
   2. Running SAT-Analytics:
   
   In a terminal window:
   
   A. clone repository to some directory: `/your/local/folder/api`
       
   B. `cd /your/local/folder/api`
       
   C. Open `config.ini` and update credentials
       
   D. `pip install -r requirements.txt`
       
   E. Run `python3 -m openapi_server`
       
   F. Open browser and go to: `http://0.0.0.0:8080/ui/`
