# GRACE Groundwater and Soil Moisture Conditions Dashboard

The GRACE Groundwater and Soil Moisture dashboard is a tool designed to visualize the global time average map of groundwater and moisture annually from 2004 to 2022 (available data for entire years). This dashboard can be utilized to compare variations in groundwater and soil moisture over time using two global maps. Additionally, a time series plot of these two parameters is provided. All these features include interactive capabilities for parameter selection, zooming, and accessing data details. 

The indicators presented are based on terrestrial water storage observations derived from GRACE-FO satellite data and integrated with other observations. The exact data used was the Groundwater storage percentile (GRACEDADM CLSM025GL 7D v3.0) and Surface soil moisture percentile (GRACEDADM CLSM025GL 7D 
v3.0). The Sustainable Development Goal (SDG) to advance is Climate Action. The tool was developed using Python with a framework based on Dash and other Python packages such as Pandas, Numpy, and Rasterio.

Available at https://rsilva.pythonanywhere.com/
Until Thursday 21 March 2024

Dashboard screenshot:

![alt text](https://github.com/RicardoFreireRfs/GRACE_dash/blob/main/visual.png)


More details about the GRACE-FO data:
https://disc.gsfc.nasa.gov/datasets/GRACEDADM_CLSM0125US_7D_4.0/summary

Reference:
Beaudoing, Hiroko, M. Rodell, A. Getirana, and B. Li, NASA/GSFC/HSL (2021), Groundwater and Soil Moisture Conditions from GRACE and GRACE-FO Data Assimilation L4 7-days 0.125 x 0.125 degree U.S. V4.0, Greenbelt, MD, USA, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: 22/12/2023, 10.5067/UH653SEZR9VQ

Houborg, R., M. Rodell, B. Li, R. Reichle, and B. Zaitchik, 2012: Drought indicators based on model assimilated GRACE terrestrial water storage observations, Wat. Resour. Res., 48, W07525, doi:10.1029/2011WR011291
