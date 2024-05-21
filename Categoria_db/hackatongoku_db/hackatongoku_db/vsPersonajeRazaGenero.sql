
CREATE TABLE [dbo].[TPersonaje](
	[id] [int] NOT NULL,
	[name] [varchar](22) NOT NULL,
	[ki] [varchar](15) NOT NULL,
	[maxKi] [varchar](16) NOT NULL,
	[race] [varchar](16) NOT NULL,
	[gender] [varchar](6) NOT NULL,
	[description] [varchar](978) NOT NULL,
	[image] [varchar](87) NOT NULL,
	[affiliation] [varchar](20) NOT NULL,
	[deletedAt] [varchar](30) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

select * from dbo.TPersonaje

---===============================================================
--�	Escribe una consulta que devuelva el conteo de personajes por raza y g�nero. (Valor: 15%)
select race as raza, gender as genero, count(1) as conteo from dbo.TPersonaje
group by race, gender

-- generar el resultado tipo pivote para que se vea como columna raza, m=male y f=female y el conteo en m y f según corresponda

select * 
from (
select race as raza, gender as genero, count(1) as conteo
from dbo.TPersonaje
group by race, gender) as d
pivot( 
	sum(d.conteo) 
	for d.genero 
	in ([Male],[Female])
	) as pvt

---===============================================================
-- •	Escribe una consulta en la que debes crear una variable tipo tabla o tabla temporal, esta debe ser una copia de la tabla TPersonajes, en esta variable tipo tabla debes  actualizar el valor de Ki y maxKi a número. 

declare @TPersonaje table(
    [id] [int] NOT NULL,
    [name] [varchar](22) NOT NULL,
    [ki] [int] NOT NULL,
    [maxKi] [int] NOT NULL,
    race [varchar](16) NOT NULL,
    [gender] [varchar](6) NOT NULL,
	[description] [varchar](978) NOT NULL,
	[image] [varchar](87) NOT NULL,
	[affiliation] [varchar](20) NOT NULL,
	[deletedAt] [varchar](30) NULL
)

-- ki y maxKi son varchar, se deben convertir a int y tienen valores con el formato = 40 Quintillion

INSERT into @TPersonaje
select [id], [name], cast([ki] as int), cast([maxKi] as int),race, gender, [description], [image], [affiliation], [deletedAt]
from dbo.TPersonaje

---===============================================================
-- •	Escribe una consulta que devuelva la brecha que hay entre Ki y maxKi de cada personaje y ordena el resultado ascendentemente por esta brecha. (Valor: 10%) 
SELECT 
    [id], 
    [name], 
    [ki], 
    PATINDEX('%[^0-9.]%', [ki]) AS indexki,
    PATINDEX('%[a-zA-Z]%', [ki]) AS indexMaxki,
    
    CASE 
        WHEN PATINDEX('%[a-zA-Z]%', [ki]) = 0 THEN 
            cast(replace(REPLACE([ki], '.', ''),',','')as decimal(38,2))
		when PATINDEX('%[a-zA-Z]%', [ki])=1 then 0
        ELSE 
            cast(LEFT([ki], PATINDEX('%[a-zA-Z]%', [ki]) - 1) as decimal(38,2))
    END AS valorKi,
	upper(CASE 
        WHEN PATINDEX('%[a-zA-Z]%', [ki]) = 0 THEN 'uno'
		when PATINDEX('%[a-zA-Z]%', [ki])=1 then 'cero'

		else right([ki], len(ki)- PATINDEX('%[^0-9.]%', [ki]) ) end
		)
		as multiploKi,
    
    [maxKi],
    
     CASE 
        WHEN PATINDEX('%[a-zA-Z]%', maxKi) = 0 THEN 
            cast(replace(REPLACE(maxKi, '.', ''),',','')as decimal(38,2))
		when PATINDEX('%[a-zA-Z]%', maxKi)=1 then 0
        ELSE 
            cast(LEFT(maxKi, PATINDEX('%[a-zA-Z]%', maxKi) - 1) as decimal(38,2))
    END AS valorMaxKi,
	upper(CASE 
        WHEN PATINDEX('%[a-zA-Z]%', maxKi) = 0 THEN 'uno'
		when PATINDEX('%[a-zA-Z]%', maxKi)=1 then 'cero'

		else right(maxKi, len(maxKi)- PATINDEX('%[^0-9.]%', maxKi) ) end
		)
		as multiploMaxKi,
    
    [race], 
    [gender], 
    [description], 
    [image], 
    [affiliation], 
    [deletedAt]
	into #separacionNumeroMultiplo
FROM 
    dbo.TPersonaje;




SELECT
    name,
    CASE 
        WHEN multiploKi = 'UNO' THEN valorKi 
        WHEN multiploKi = 'CERO' THEN 0
        WHEN multiploKi LIKE '%housand%' THEN valorKi * 1e3 
        WHEN multiploKi LIKE '%million%' THEN valorKi * 1e6 
        WHEN multiploKi LIKE '%billion%' THEN valorKi * 1e9
        WHEN multiploKi LIKE '%trillion%' THEN valorKi * 1e12 
        WHEN multiploKi LIKE '%quadrillion%' THEN valorKi * 1e15 
        WHEN multiploKi LIKE '%quintillion%' THEN valorKi * 1e18 
        WHEN multiploKi LIKE '%googol%' THEN valorKi * 1
        WHEN multiploKi LIKE '%septillion%' THEN valorKi * 1e24 
        -- Eliminar la línea de googolplex para evitar el desbordamiento
        ELSE 1 
    END AS valorKi,
	CASE 
        WHEN multiploMaxKi = 'UNO' THEN valorMaxKi 
        WHEN multiploMaxKi = 'CERO' THEN 0
        WHEN multiploMaxKi LIKE '%housand%' THEN valorMaxKi * 1e3 
        WHEN multiploMaxKi LIKE '%million%' THEN valorMaxKi * 1e6 
        WHEN multiploMaxKi LIKE '%billion%' THEN valorMaxKi * 1e9
        WHEN multiploMaxKi LIKE '%trillion%' THEN valorMaxKi * 1e12 
        WHEN multiploMaxKi LIKE '%quadrillion%' THEN valorMaxKi * 1e15 
        WHEN multiploMaxKi LIKE '%quintillion%' THEN valorMaxKi * 1e18 
        WHEN multiploMaxKi LIKE '%googol%' THEN valorMaxKi * 1
        WHEN multiploMaxKi LIKE '%septillion%' THEN valorMaxKi * 1e24 
        -- Eliminar la línea de googolplex para evitar el desbordamiento
        ELSE 1 
    END AS valorMaxKi,
	CASE 
        WHEN multiploMaxKi = 'UNO' THEN valorMaxKi 
        WHEN multiploMaxKi = 'CERO' THEN 0
        WHEN multiploMaxKi LIKE '%housand%' THEN valorMaxKi * 1e3 
        WHEN multiploMaxKi LIKE '%million%' THEN valorMaxKi * 1e6 
        WHEN multiploMaxKi LIKE '%billion%' THEN valorMaxKi * 1e9
        WHEN multiploMaxKi LIKE '%trillion%' THEN valorMaxKi * 1e12 
        WHEN multiploMaxKi LIKE '%quadrillion%' THEN valorMaxKi * 1e15 
        WHEN multiploMaxKi LIKE '%quintillion%' THEN valorMaxKi * 1e18 
        WHEN multiploMaxKi LIKE '%googol%' THEN valorMaxKi * 1
        WHEN multiploMaxKi LIKE '%septillion%' THEN valorMaxKi * 1e24 
        -- Eliminar la línea de googolplex para evitar el desbordamiento
        ELSE 1 
    END -
	CASE 
        WHEN multiploKi = 'UNO' THEN valorKi 
        WHEN multiploKi = 'CERO' THEN 0
        WHEN multiploKi LIKE '%housand%' THEN valorKi * 1e3 
        WHEN multiploKi LIKE '%million%' THEN valorKi * 1e6 
        WHEN multiploKi LIKE '%billion%' THEN valorKi * 1e9
        WHEN multiploKi LIKE '%trillion%' THEN valorKi * 1e12 
        WHEN multiploKi LIKE '%quadrillion%' THEN valorKi * 1e15 
        WHEN multiploKi LIKE '%quintillion%' THEN valorKi * 1e18 
        WHEN multiploKi LIKE '%googol%' THEN valorKi * 1
        WHEN multiploKi LIKE '%septillion%' THEN valorKi * 1e24 
        -- Eliminar la línea de googolplex para evitar el desbordamiento
        ELSE 1 
    END as Brecha
	
FROM 
    #separacionNumeroMultiplo
ORDER BY brecha ASC

---===============================================================
-- •	Escribe una consulta que retorne el personaje más poderoso por cada raza (Valor: 10%)

WITH CTE AS (
    SELECT 
        name,
        race,
        valorKi,
        ROW_NUMBER() OVER (PARTITION BY race ORDER BY valorKi DESC) AS rn
    FROM 
        #separacionNumeroMultiplo
)
SELECT 
    name,
    race,
    valorKi
FROM 
    CTE
WHERE 
    rn = 1;

---===============================================================
--•	Escribe una consulta que retorne al dios más débil. 



select name 
from #separacionNumeroMultiplo
where valorKi = (select min(valorKi) from #separacionNumeroMultiplo where race = 'God' )

---===============================================================
--•	Escribe una consulta que muestre el nombre de cada personaje y su nombre inverso, por ejemplo:
-- Kamisama, amasimak 
select name, reverse(name) as nombreInverso from dbo.TPersonaje

---===============================================================
--•	Crea una consulta que retorne cual es la mediana del ki por raza, los nombres de las razas deben mostrarse en columnas como se muestra en el siguiente ejemplo:
-- Raza1 | Raza2 | Raza3 | Raza4 | Raza5
-- 1000  | 2000  | 3000  | 4000  | 5000

-- Calcula el promedio de valorKi por raza
    SELECT 
        name,
        race,
        valorKi
    FROM 
        #separacionNumeroMultiplo
    order by race, name, valorKi asc
