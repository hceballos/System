SELECT
  sum(haber - debe) as 'Saldo segun Balance'
FROM
	MovimientosTabla
WHERE
	cuenta=?