SELECT
  fecha as Month,
  (HABER-DEBE) AS Estimation
FROM
  MovimientosTabla
WHERE
  cuenta=?
ORDER BY
  fecha asc