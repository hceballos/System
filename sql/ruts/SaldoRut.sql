SELECT
  sum(debe - haber) as 'Saldo segun Balance'
FROM
  MovimientosTabla
WHERE
  auxiliar=?