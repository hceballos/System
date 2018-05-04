--Prueba Ácida = (Caja + Bancos + Acciones + Deudores + Dctos. por Cobrar) / Pasivo circulante
SELECT
    ((CAJAS + BANCOS + INVERSIONES + CUENTAS_POR_COBRAR) / PASIVO_CORRIENTE) as Acido
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
        sum(haber - debe)  as  PASIVO_CORRIENTE
    FROM
        movimientosTabla
    WHERE
        cuenta like '2-01-%'
    ) PASIVO_CORRIENTE