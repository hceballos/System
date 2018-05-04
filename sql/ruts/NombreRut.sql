SELECT
	nombre
FROM
	MovimientosTabla INNER JOIN COMPLEMENTO
	ON MovimientosTabla.auxiliar = COMPLEMENTO.RUT
WHERE
	auxiliar=?
GROUP BY
	auxiliar