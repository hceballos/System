SELECT
	sum(haber - debe) as 'Saldo segun Balance'
FROM
	MovimientosTabla
WHERE
  cuenta=?
  and fecha between date('NOW', 'START OF YEAR') and date('NOW')