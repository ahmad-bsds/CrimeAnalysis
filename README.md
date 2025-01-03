# Los Angeles Crime Analysis

Welcome to the **Los Angeles Crime Analysis** project repository! This project combines robust ETL processes, advanced data warehousing, and insightful analytics to empower data-driven decisions and visualize trends in crime data for Los Angeles.

---

## Repository Overview

This repository contains the following files:

1. **`report.pdf`**: A comprehensive PDF report detailing the objectives, methodology, and findings of the Los Angeles Crime Analysis project.

2. **`dashboard.pibx`**: A Power BI file showcasing a dynamic and interactive dashboard. Explore the visualization of crime trends, hotspots, and patterns in Los Angeles.

3. **`script.py`**: A Python script designed for ETL (Extract, Transform, Load) processes. The script processes raw crime data, transforms it for analysis, and uploads the cleaned dataset to the Snowflake data warehouse. It is built to integrate seamlessly with Talend for scalable data workflows.

---

## Key Features

### 1. ETL Process

The `script.py` file handles:

- **Data Extraction**: Retrieves raw crime data from multiple sources.
- **Data Transformation**: Cleans, normalizes, and enriches the data to prepare it for analysis.
- **Data Loading**: Loads the processed data into the Snowflake data warehouse, enabling centralized and efficient storage.

### 2. Data Warehousing

With Snowflake as the backbone of our data warehouse, we ensure:

- Scalability and performance for large datasets.
- Secure and reliable storage for all processed data.
- Easy access for advanced analytics and visualization tools.

### 3. Data Analytics and Visualization

The Power BI dashboard in `dashboard.pibx` provides:

- Interactive visualizations to uncover trends and patterns.
- Key insights into crime types, time-based occurrences, and geographic distribution.
- User-friendly navigation for stakeholders and decision-makers.

---

## Use Cases

This project is designed for:

- **Law Enforcement Agencies**: Gain actionable insights to allocate resources effectively.
- **Policy Makers**: Inform policies and initiatives aimed at reducing crime rates.
- **Data Analysts**: Explore the interplay of various factors contributing to crime trends.

---

## Getting Started

### Prerequisites

1. **Talend**: For automating the ETL workflow.
2. **Python**: Required to run the `script.py` file.
3. **Snowflake**: As the target data warehouse.
4. **Power BI**: To view and interact with the dashboard.

### Steps to Run the Project

1. Clone the repository.
   ```bash
   git clone https://github.com/ahmad-bsds/CrimeAnalysis.git
   ```
2. Install necessary Python packages for the ETL script.
3. Configure Talend to use the `script.py` for the ETL process.
4. Load the `dashboard.pibx` in Power BI to explore the visualizations.

---

## Future Enhancements

- Integration of real-time crime data for live dashboard updates.
- Enhanced predictive analytics using machine learning algorithms.
- Expansion to analyze crime trends in other cities.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

