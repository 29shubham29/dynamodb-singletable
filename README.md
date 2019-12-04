# DynamoDb Single Table design.

## Why single table design?
* Single table helps us to easily organize our data in a single table 
* This makes it easy for us to query a single table not using more tables for making it like relational database systems.

## Design pattern:
* We define a generic term for partition key i.e "pk" or "partition" and sort Key i.e "sk" or "sort"
* Now use a index whose partition key will be the primary key's sort key and just make a composite key by combining other attributes like user#location#data