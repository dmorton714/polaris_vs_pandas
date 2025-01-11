# polaris_vs_pandas

Backend test to determine how I will build the backend of a project. 

# results

- Polars: 346 milliseconds ± 11.5 milliseconds per loop
- Pandas: 6.78 seconds ± 166 milliseconds per loop

Polars is significantly faster than Pandas in this case, with a runtime of around 346 ms, compared to 6.78 seconds for Pandas.

**Polars is approximately 19.6 times faster**

The database contains 25 cols with 2 million rows inside of 3 tables. 

polars and Duck DB will be the backend. 

concurrent processes may be an issue. 

