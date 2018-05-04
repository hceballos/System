SELECT
    sum(debe-haber) as 'Saldo segun Balance'
FROM
    MovimientosTabla
WHERE
    cuenta=?
GROUP BY
    cuenta
HAVING
    cuenta