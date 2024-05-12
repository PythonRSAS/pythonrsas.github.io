---
layout: post
tag: transition migration
category: "climate risk"
title: "EEIO Transition Matrix"
description: Credit rating migration is an analytic tools for analyzing credit risk
author: Sarah Chen
image: images/posts/rating_migration.PNG
---


EEIO (Environmentally Extended Input-Output) models can utilize transition matrices as part of analysis. Transition matrices are often employed in dynamic input-output models to represent changes over time in the structure of an economy. 

In the context of EEIO modeling, a transition matrix could be used to depict changes in technology, consumption patterns, or environmental policies that affect the environmental intensity of economic activities. By incorporating a transition matrix into the EEIO model, analysts can simulate how these changes propagate through the economy and influence environmental impacts over time.

For example, researchers might use a transition matrix to model the gradual adoption of cleaner technologies or the implementation of carbon pricing policies. This would allow them to assess how these changes affect emissions, resource use, and other environmental indicators across different sectors of the economy.

Overall, while not every EEIO model may incorporate a transition matrix, it can be a valuable tool for analyzing dynamic changes in environmental impacts and policy scenarios over time.

# Example
Let's consider a hypothetical economy with 3 sectors: agriculture, manufacturing, and services. We want to assess how the adoption of cleaner technologies affects carbon emissions in each sector over a *five-year period*.

1. **Define the initial input-output matrix**
First, we define the initial input-output matrix <span class="coding">(I)</span> which represents the interdependencies between sectors in the base year:

```
Initial Input-Output Matrix (I):
[0.3 0.2 0.5]
[0.1 0.6 0.3]
[0.4 0.3 0.3]
```

* **2. define the transition matrix**
Next, we define the transition matrix (T), which represents how the technology in each sector evolves over time. For simplicity, let's assume that each sector's carbon intensity decreases by 10% every year:

```code
Transition Matrix (T):
[0.9 0   0  ]
[0   0.9 0  ]
[0   0   0.9]

```

* **3. iterate over each year**  Now, we iterate over each year to calculate the input-output matrix for that year:

```
Year 1:
I_1 = T * I
   = [[0.9 0   0  ]    [[0.3 0.2 0.5]
      [0   0.9 0  ]  *  [0.1 0.6 0.3]
      [0   0   0.9]]    [0.4 0.3 0.3]]

   = [[0.27 0.18 0.45]
      [0.09 0.54 0.27]
      [0.36 0.27 0.27]]

Year 2:
I_2 = T * I_1
   = T * [[0.27 0.18 0.45]
          [0.09 0.54 0.27]
          [0.36 0.27 0.27]]

   = ... (repeat for subsequent years)
```
  
* **4. Compute total emission**: Finally, we calculate the total carbon emissions for each year by multiplying the input-output matrix by the carbon intensity vector <span class="coding">(C)</span>, which represents the amount of carbon emitted per unit of output in each sector:

```code

Carbon Intensity Vector (C):
[0.1]
[0.2]
[0.3]

Year 1 Emissions:
Emissions_1 = I_1 * C
            = [[0.27 0.18 0.45]
               [0.09 0.54 0.27]
               [0.36 0.27 0.27]] * [0.1                                      0.2                                      0.3]

            = [0.158               0.198               0.225]

```

Repeat this process for each year to assess how carbon emissions change over time as a result of the transition in technology. This example demonstrates how you can use a transition matrix within an EEIO model to analyze dynamic changes in environmental impacts.

# Example in Python

This Python code defines the initial input-output matrix (I), transition matrix (T), and carbon intensity vector (C). It then iterates over each year, calculates the input-output matrix for that year using the transition matrix, calculates the total emissions for the year, and prints the results.

You can modify the values of the input-output matrix, transition matrix, carbon intensity vector, and number of years to customize the example according to your specific scenario. Additionally, you can extend this example by incorporating more complex dynamics or additional environmental factors as needed.


<div class="code-head"><span>code</span>rating migration</div> 

```python

import numpy as np

# Define initial input-output matrix
I = np.array([[0.3, 0.2, 0.5],
              [0.1, 0.6, 0.3],
              [0.4, 0.3, 0.3]])

# Define transition matrix
T = np.array([[0.9, 0,   0],
              [0,   0.9, 0],
              [0,   0,   0.9]])

# Define carbon intensity vector
C = np.array([0.1, 0.2, 0.3])

# Define number of years
num_years = 5

# Iterate over each year
for year in range(num_years):
    # Calculate input-output matrix for current year
    I_year = np.dot(T, I) if year > 0 else I
    
    # Calculate total emissions for current year
    emissions = np.dot(I_year, C)
    
    print(f"Year {year + 1} Emissions:", emissions)
    
    # Update input-output matrix for next year
    I = I_year

```



<div class="code-head"><span>code</span>rating migration</div> 

For a practical example using real data, let's consider the input-output matrix for the United States economy, along with carbon intensity data for different sectors. We'll simulate the reduction in carbon emissions over a certain period by applying a transition matrix that represents the adoption of cleaner technologies.

Please note that obtaining real data for all sectors and years can be complex, so we'll simplify by providing example data for illustrative purposes.

```python

import numpy as np

# Example Input-Output Matrix (Simplified)
# This matrix represents the transactions between different sectors of the economy
# Each row represents the inputs required by each sector to produce one unit of output
# Each column represents the outputs produced by each sector
# Data source: U.S. Bureau of Economic Analysis (BEA) or similar
input_output_matrix = np.array([
    [0.4, 0.3, 0.3],  # Agriculture
    [0.2, 0.5, 0.3],  # Manufacturing
    [0.1, 0.2, 0.7]   # Services
])

# Example Carbon Intensity Vector (Simplified)
# This vector represents the carbon emissions per unit of output for each sector
# Data source: Environmental Protection Agency (EPA) or similar
carbon_intensity_vector = np.array([0.1, 0.2, 0.15])  # in tons of CO2 per unit of output

# Define number of years
num_years = 10

# Define transition matrix
# For this example, we assume a 5% reduction in carbon intensity each year
transition_matrix = np.diag([0.95, 0.95, 0.95])  # Diagonal matrix with 0.95 on the main diagonal

# Initialize input-output matrix for the first year
current_input_output_matrix = input_output_matrix

# Calculate emissions for each year
for year in range(num_years):
    # Apply transition matrix to update input-output matrix
    current_input_output_matrix = np.dot(transition_matrix, current_input_output_matrix)
    
    # Calculate total emissions for current year
    emissions = np.dot(current_input_output_matrix, carbon_intensity_vector)
    
    print(f"Year {year + 1} Emissions:", emissions)


```

# Real Example 
[USEEIO matrix](https://catalog.data.gov/dataset?q=useeio)
USEEIOv1.1_Matrices.xlsx


# Data for EEIO model

Obtaining carbon intensity data for different sectors typically involves accessing environmental databases, government reports, academic studies, or industry reports. Here are some potential sources where you might find carbon intensity data:

1. **Government Environmental Agencies**: Environmental agencies often collect and publish data on carbon emissions and environmental impacts. For example, in the United States, the Environmental Protection Agency (EPA) provides various datasets and reports related to greenhouse gas emissions by sector.

2. **International Organizations**: Organizations such as the United Nations Environment Programme (UNEP), the International Energy Agency (IEA), and the World Bank may provide global or regional data on carbon emissions and sectoral carbon intensity.

3. **Academic Research**: Academic studies often analyze carbon intensity and greenhouse gas emissions across different sectors. Scholarly journals, research papers, and academic databases can be valuable sources of such data.

4. **Industry Reports and Databases**: Some industries publish reports or maintain databases containing information on carbon emissions and environmental impacts specific to their sectors. For example, energy companies may provide data on the carbon intensity of energy production.

5. **Life Cycle Assessment (LCA) Databases**: LCA databases, such as Ecoinvent, often contain data on the environmental impacts of various products and processes, including carbon emissions. These databases can be valuable sources of sector-specific carbon intensity data.

6. **National Statistical Agencies**: National statistical agencies sometimes include environmental data in their reports and datasets. For instance, they may publish information on energy consumption and emissions by sector.

7. **Non-Governmental Organizations (NGOs)**: Environmental NGOs and research organizations may conduct studies and publish reports on carbon emissions and sectoral carbon intensity.

When accessing carbon intensity data, it's essential to consider factors such as the scope and coverage of the data, the methodology used for measurement and calculation, and the currency and reliability of the sources. Additionally, you may need to perform data validation and verification to ensure its suitability for your specific analysis or modeling purposes.


# References
[EPA](https://www.epa.gov/ghgreporting)