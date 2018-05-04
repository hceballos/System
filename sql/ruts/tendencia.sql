SELECT
  fecha as Month,
  (DEBE - HABER) AS Estimation
FROM
  MovimientosTabla
WHERE
  auxiliar =?
ORDER BY
  fecha asc