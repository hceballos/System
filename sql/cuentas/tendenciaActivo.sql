SELECT
  fecha as Month,
  (DEBE - HABER) AS Estimation
FROM
  MovimientosTabla
WHERE
  cuenta =?
ORDER BY
  fecha asc