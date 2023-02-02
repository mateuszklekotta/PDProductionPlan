QueryString = "SELECT TOP (10) \
                        COLLECTREFPRODID AS Task,\
                        ITEMID,\
                        [WMSIPRODDATEFROM_AXC] AS Start,\
                        [WMSIPRODTIMEFROM_AXC] AS StartTime,\
                        DATEADD(mm,1,WMSIPRODDATEFROM_AXC) AS Finish,\
                        PRODSTATUS,\
                        SECONDS_RET,\
                        CAST(RIGHT(PRODROUTE.QTYCATEGORYID,3) AS float)/100*QTYSCHED/11 AS PROD_TIME\
                        FROM PRODTABLE\
                        LEFT JOIN PRODROUTE ON PRODTABLE.COLLECTREFPRODID = PRODROUTE.PRODID\
                        ORDER BY COLLECTREFPRODID DESC"
