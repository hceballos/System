--Capital Trabajo Neto sobre Deudas a Corto Plazo(o Pasivo pCirculante) (KTSPC)
--(Activos Circulantes – Pasivo Circulante) / Pasivo Circulante
SELECT
    *
FROM
    (
    SELECT
        sum(debe-haber)*1.0 as CAJAS
    FROM
        movimientosTabla
    WHERE
        cuenta like '1-01-01-%'
    ) CAJAS
    ,
    (
    SELECT
        sum(debe-haber) as BANCOS
    FROM
        movimientosTabla
    WHERE
        cuenta like '1-01-02-%'
    ) BANCOS
    ,
    (
    SELECT
        sum(debe-haber)  as INVERSIONES
    FROM
        movimientosTabla
    WHERE
        cuenta like '1-01-03-%'
    ) INVERSIONES
    ,
    (
    SELECT
        sum(debe-haber)  as CUENTAS_POR_COBRAR
    FROM
        movimientosTabla
    WHERE
        cuenta like '1-01-04-%'
    ) CUENTAS_POR_COBRAR
    ,
    (
    SELECT
        sum(haber - debe) as  PASIVO_CORRIENTE
    FROM
        movimientosTabla
    WHERE
        cuenta like '2-01-%'
    ) PASIVO_CORRIENTE