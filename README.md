# Climate_change_impacts_on_maize_production_in_East_Africa
In this repository, we present the data and the files used to produce the figure on trends in temperature, precipitation, and maize yield in Eastern Africa (Rwanda, Kenya, Uganda, Tanzania, Somalia, South Sudan, Burundi, and Democratic Republic of the Congo).

A docker container executable on different platforms has been created to facilitated the reproducibility of the figure. 
This Docker container generates visualizations of historical temperature, precipitation trends in East Africa from 1750 to 2023, and maize yields from 1961 to 2022. It integrats years with extreme events such as droughts and floods, along with notable El Niño and La Niña events. 

Container Overview 
This container processes historical datasets of annual temperature and annual precipitation (1750–2023) and  Maize Yield dataset (1961–2022) . The output is saved as an image file: figure2_output.png. This figure visualizes the following trends:  
•	Annual Temperature Trends (1750–2023), 
•	Annual Precipitation Trends (1750–2023), highlighting El Niño and La Niña year,  
•	Maize Yield Trends (1961–2022), highlighting floods and drought 
•	Maize yield in East Africa compared to the global maize yield average. 

How to Use This Container
Pull the Docker Image: 
docker pull minani/figure2-container:latest   
Run the Container with Data Mounted:
docker run -v $(pwd)/data:/app/data -v $(pwd):/app minani/figure2-container:latest   
Check Output: 
figure2_output.png  

License 
This project is released under the MIT License    

Contributing
Feel free to open issues or pull requests on the Github: https://github.com/jeanmarieminani/Climate_change_impacts_on_maize_production_in_East_Africa   

Contact 
For questions or feedback, reach out at: jeanmarie.minani2@gmail.com 

