# 7.1 HW Questions 


1. Using EVregistry, Write a query to select the `ModelYear`, `Make`, and `Model` off all of the vehicles in the registry.

## Question 1
```SQL

SELECT ModelYear, Make, Model
FROM EVRegistry;

```


2. Using the EVRegistry table, Write a query that lists all of the unique types of EV's. your reult set should have one column, `ElectricVehicleType`.

## Question 2
```SQL

SELECT DISTINCT(ElectricVehicleType)
FROM EVRegistry;

```

3. Using the EVRegistry, Write a query that shows all of the information on Battery Electric Vehicles (BEV) that are in the registry.

## Question 3
```SQL

SELECT 
	ElectricVehicleType, 
	ElectricRange
FROM EVRegistry
WHERE ElectricVehicleType LIKE "Battery%";

```

4. Using the EVRegistry, write a query that returns the `Make` and `Model` of all of the EV's that have a BaseMSRP between 20000 and 35000?

## Question 4
```SQL

SELECT Make, Model
FROM EVRegistry
WHERE BaseMSRP BETWEEN 20000 AND 35000;

```


# 7.2 HW Questions 

1. Using EVRegistry, write a query to find a record  where the `City` attribute is NULL. Return all of the available columns. 

## Question 1
```SQL

SELECT *
FROM EVRegistry
WHERE City IS NULL;

```



2. Write a query to find the `make`, `model`, and `ElectricVehicleType` where the VIN number has  that ends in '3E1EA1J'.

## Question 2
```SQL

SELECT 
	Make, 
	Model, 
	ElectricVehicleType
FROM EVRegistry
WHERE VIN LIKE "%3E1EA1J";

```

3. Select the `ModelYear`, `make`, `model`, `ElectricVehicleType`, and `range` of the Tesla vehicles or cheverolet vehicles in the registry. Order the result set by Make and Model year in from newest to oldest.

## Question 3
```SQL

SELECT 
	ModelYear,
	Make,
	Model,
	ElectricVehicleType,
	ElectricRange
FROM EVRegistry
WHERE Make LIKE "Chevrolet" OR
	MAKE LIKE "Tesla"
ORDER BY 1,2 DESC;

```


4. Using EVCharging, Write a query to find out how many many times those stations were used. Order them by the most used to the least used and limit the output to 5 records.


## Question 4
```SQL

SELECT stationId, count(userId) as user_ct
FROM EVCharging
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;

```


5.  Using EVCharging, For the folks who charged longer than 0.5 hours, show the min and max of the charging time for each user. Your output columns should be `userid`, `minTime`, and `maxTime`. Order this result set by the last two columns respectively. 


## Question 5
```SQL

SELECT 
	userId, 
	min(chargeTimeHrs) AS min_time, 
	max(chargeTimeHrs) AS max_time
FROM EVCharging
GROUP BY userId
HAVING min_time > .5
ORDER BY 2,3;

```

# 7.3 HW Questions

1. Using EVCharging, Which day of the week has the highest average charging time? Round the answer to 2 decimal points.

	- Based on the following code, Wed has the highest average charge time hrs.

```SQL

SELECT
	weekday, round(avg(chargeTimeHrs),2) as avg_charge_time
FROM EVCharging
GROUP BY 1
ORDER BY 2 DESC;

```

2. Using, EV charging, Find the total power consumed from charging EV's by each User. Return the `userId` and name the calculated column, `totalPower`. Round the answer to 2 deciaml points and list the out put in highest to lowest order. Limit the order to the top 15 users.


```SQL

SELECT
	userId,
	round(sum(kwhTotal),2) as total_pwr
FROM EVCharging
GROUP BY userId
ORDER BY 2 DESC
LIMIT 15;

```


3. Using dimfacility and factCharge, write a query to find out which type of facility (GROUP BY) has the most amount of charging stations. Return `type Facility` and name the calculated column `numStation`. Order the result set from highest to lowest number of charging stations.  

	- Based on the following code, R&D buildings have the most amount of charging stations.

```SQL

SELECT
	df.typeFacility,
	count(stationID) as num_station
FROM factCharge fc
INNER JOIN dimFacility df
	ON fc.facilityID = df.FacilityKey
GROUP BY 1
ORDER BY 2 DESC;


```


4. In your own words, Briefly explain Primary Keys and Foreign Keys. 

	- Primary Keys are unique identifiers for each record within a column/attribute and a Foreign Key(s) help bridge the connections between multiple tables and maintain data integrity.

<br>

5. Using EV Charging, For the folks who charged longer than one hour, show the min and max of the charging time for each user. Your output columns should be `userid`, `minTime`, and `maxTime`. Order this result set by the last two columns respectively. HINT: USE `HAVING`

```SQL

SELECT
	userId,
	min(chargeTimeHrs) as min_chrg_time,
	max(chargeTimeHrs) as max_chrg_time
FROM EVCharging
GROUP BY 1
HAVING chargeTimeHrs > 1
ORDER BY 2, 3 DESC;


```