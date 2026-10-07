# PNCP_PROJECT

Trying to find out outiliers on PNCP gov data by doing exploratory data techinics.

I am using PNCP api to access governament data of reverse auction and i want to make a way of vizualize that data to create a way of bring the peaple closer to the reality of price gouging in these public procurements within the Brazil context.

## About the project

This project uses public procurement data from the Brazilian **PNCP (Portal Nacional de Contratações Públicas)**.

The main goal is to collect, organize and explore public procurement data in a simpler way. In the future, the project will try to identify unusual prices and other possible anomalies in public purchases.

An anomaly does not necessarily mean fraud or corruption. The goal is to highlight unusual cases that may deserve more investigation.

The idea is to understand how each part works.

## Data source

The data comes from the public PNCP API.

A procurement can contain many items and each item contains information such as:

- description
- quantity
- unit
- estimated unit price
- estimated total price

A result can contain information such as:

- supplier
- homologated quantity
- homologated unit price
- homologated total price

## Current database model

The first version of the database is being designed with the following tables: orgao, contratacao, item, fornecedor, resultado.

Internal integer IDs are used as primary keys.

## Current stage

The project is currently in its first development stages.

So far I am:

1. learning how the PNCP API works;
2. exploring procurement, item and result endpoints;
3. understanding how the different API objects are related;
4. designing the relational database;
5. learning SQL before connecting the database to Python.

More advanced data analysis and anomaly detection will be added later.

## Future ideas

Some possible future features are:

- download procurement data automatically from the PNCP API;
- store and update the data locally;
- compare prices of similar products;
- detect statistical outliers;
- analyze suppliers and public organizations;
- create visualizations and dashboards;
- make public procurement data easier to understand;
- explore supplier and procurement networks;
- investigate unusual purchasing patterns.

## Important note

A statistical outlier is not proof of fraud, corruption or price gouging.

The project aims to identify unusual patterns in public procurement data and make these cases easier to explore.

