SELECT
  fecha as Month,
  (debe - haber) AS Estimation
FROM
  MovimientosTabla
WHERE
  cuenta=?
ORDER BY
  fecha asc