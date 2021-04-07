# Oracle

Duck uses Oracle's [DBMS_REDACT](https://docs.oracle.com/en/database/oracle/oracle-database/21/arpls/DBMS_REDACT.html)
package to achive online data masking and redaction. The `DBMS_REDACT` package provides an interface to Oracle Data Redaction, which enables you to mask (redact) data that is returned from queries issued by low-privileged users or an application.

## Connection

- Make sure you have the oracle instant client.
- Set `LD_LIBRARY_PATH` to the location of the instant client. Example;
```sh
export LD_LIBRARY_PATH=/path/to/instantclient_12_2
```