
--select * 
--from [Portafolio-Covid]..[covid-data-deaths]
--where [continent] is not null
--order by 3,4

--select * 
--from [Portafolio-Covid]..[covid-data-vaccinations]
--order by 3,4

/*Seleccion de data*/

--select [location],[date],[total_cases],[new_cases],[total_deaths],[population]
--from [dbo].[covid-data-deaths]
--where [continent] is not null
--order by 1, 2

/*Ver el total de casos vs Total de muertes*/

/* Esta consulta no ejecuta por error en los tipos de datos
--Select [location], [date], [total_cases], [total_deaths],
--		([total_deaths]/[total_deaths]) *100 AS Deathpercentage
--From [dbo].[covid-data-deaths]
--Order by 1,2; */

--SELECT [location], [date], [total_cases], [total_deaths], 
--       CAST([total_deaths] AS float) / CAST([total_cases] AS float) *100 AS Deathpercentage
--FROM [dbo].[covid-data-deaths]
--ORDER BY 1, 2;

/*Probabilidad de morir si nos contagiamos de covid en Ecuador*/

--SELECT [location], [date], [total_cases], [total_deaths], 
--       CAST([total_deaths] AS float) / CAST([total_cases] AS float) *100 AS Deathpercentage
--FROM [dbo].[covid-data-deaths]
--WHERE location LIKE '%Ecuador%'
--and [continent] is not null
--ORDER BY 1, 2;


/*Total de casos vs la Poblacion
  Muestra que porcentaje de poblacion tiene Covid*/

--SELECT [location], [date], [population],[total_cases], 
--       CAST([total_cases] AS float) / CAST( [population]AS float) *100 AS PercentPopulationInfected
--FROM [dbo].[covid-data-deaths]
----WHERE location LIKE '%Ecuador%'
--ORDER BY 1, 2;


/*Paises con tasas de infeccion mas alta en comparacion con la poblacion*/

--SELECT [location], [population], MAX([total_cases]) as HighestInfectionCount, 
--       MAX(CAST([total_cases] AS float)) / CAST([population] AS float) * 100 AS PercentPopulationInfected
--FROM [dbo].[covid-data-deaths]
----WHERE location LIKE '%Ecuador%'
--GROUP BY [location], [population]
--ORDER BY PercentPopulationInfected desc


/*Pa�ses con mayor n�mero de muertes por poblaci�n*/

--SELECT [location], MAX(CAST([total_deaths] as Int)) as TotalDeathCount
--FROM [dbo].[covid-data-deaths]
----WHERE location LIKE '%Ecuador%'
--where [continent] is not null
--GROUP BY [location]
--ORDER BY TotalDeathCount desc

/*Dividimos por continentes*/

-- Contintentes con mayor n�mero de muertos por poblaci�n --

--SELECT [continent], MAX(CAST([total_deaths] as Int)) as TotalDeathCount
--FROM [dbo].[covid-data-deaths]
----WHERE location LIKE '%Ecuador%'
--where [continent] is not null
--GROUP BY [continent]
--ORDER BY TotalDeathCount desc

--SELECT [location], MAX(CAST([total_deaths] as Int)) as TotalDeathCount
--FROM [dbo].[covid-data-deaths]
----WHERE location LIKE '%Ecuador%'
--where [continent] is null
--GROUP BY [location]
--ORDER BY TotalDeathCount desc

/*Numeros globales*/

----Si queremos filtar por fecha el numero de casos

--SELECT [date], SUM([new_cases]) AS [total_cases],SUM(CAST([new_deaths] AS INT)) AS [total_deaths],
--       CASE WHEN SUM([new_cases]) > 0 THEN (SUM(CAST([new_deaths] AS INT)) / NULLIF(SUM([new_cases]), 0)) * 100 
--       ELSE NULL END AS DeathPercentage
--FROM [dbo].[covid-data-deaths]
--WHERE [continent] IS NOT NULL
--GROUP BY [date]
--ORDER BY 1, 2;


-- Verificamos por el numero total de casos en el mundo  

--SELECT SUM([new_cases]) AS [total_cases], SUM(CAST([new_deaths] AS INT)) AS [total_deaths], 
--	   SUM(CAST([new_deaths] AS INT)) /SUM([new_cases]) *100 AS DeathPercentage
--FROM [dbo].[covid-data-deaths]
--where [continent] is not null
--ORDER BY 1, 2;

/*Poblacion total vs Vacunacion*/

SELECT dea.[continent], dea.[location], dea.[date],dea.[population], vac.[new_vaccinations],
SUM(CONVERT(Int, vac.new_vaccinations)) OVER (Partition by dea.location ORDER BY dea.location, dea.Date)
AS RollingPeopleVaccinated
FROM [dbo].[covid-data-deaths] dea
JOIN [dbo].[covid-data-vaccinations] vac
	ON dea.[location] = vac.[location]
	AND dea.[date] = vac.[date] 
WHERE dea.[continent] IS NOT NULL
ORDER BY 2, 3













